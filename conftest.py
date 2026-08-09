import pytest
import allure
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright,APIRequestContext

# ========================================================================
#  REGISTER INI KEYS
# ========================================================================
def pytest_addoption(parser):
    """
    Registers INI keys so we can fall back to them. 
    We do NOT use parser.addoption for CLI flags already in the playwright plugin.
    """
    parser.addini("browser", help="Default browser")
    parser.addini("headed", help="Default headed mode (true/false)")
    parser.addini("base_url", help="Default base URL")
    parser.addini("video", help="Video recording setting")
    parser.addini("screenshot", help="Screenshot setting")
    parser.addini("tracing", help="Tracing setting")
    parser.addini("api_base_url", help="API url setting")


    parser.addoption("--base_url", action="store", help="Base URL")
    parser.addoption("--api_base_url", action="store", help=" API Base URL")
    # parser.addoption("--browser", help="Default browser")
    # parser.addoption("--headed", help="Default headed mode (true/false)")
    # parser.addoption("--base_url", help="Default base URL")
    # parser.addoption("--video", help="Video recording setting")
    # parser.addoption("--screenshot", help="Screenshot setting")
    # parser.addoption("--tracing", help="Tracing setting")


# HOOK TO TRACK TEST RESULTS

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


#-----------------------------------------------------
# FIXTURE 1:starting playwright instance and returning playwright instance to create context
#-------------------------------------------------------
@pytest.fixture(scope="session")
def playwright_instance():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

# ----------------------------------------------------------------------------
# FIXTURE 2 - browser context
# ----------------------------------------------------------------------------
@pytest.fixture(scope="session")
def browser_context(request,playwright_instance):
    # Read test configuration
    browser_name=request.config.getoption("--browser")
    if browser_name is None:
        browser_name=request.config.getini("browser")

    
    headed_flag = request.config.getoption("--headed")
    if headed_flag is None:
        headed_flag=request.config.getini("headed")

    
    video_option = request.config.getoption("--video")
    if video_option is None:
        video_option=request.config.getoption("video")

    print(f"\n[EXECUTION] Browser: {browser_name} | Headed: {headed_flag}")

    #playwright = sync_playwright().start()
    launch_args = {"headless": not headed_flag}
    
    # Clean the string for comparison
    b_type = str(browser_name).lower().strip()

    if b_type == "firefox":
        browser = playwright_instance.firefox.launch(**launch_args)
    elif b_type == "webkit":
        browser = playwright_instance.webkit.launch(**launch_args)
    else:
        browser = playwright_instance.chromium.launch(**launch_args)

    context_args = {}
    if video_option in ["on", "retain-on-failure"]:
        Path("reports/videos").mkdir(parents=True, exist_ok=True)
        context_args["record_video_dir"] = "reports/videos"
    
    context = browser.new_context(**context_args)
    yield context

    context.close()
    browser.close()
    #playwright.stop()


# ----------------------------------------------------------------------------
# FIXTURE 3 - page and launch application 
# ----------------------------------------------------------------------------
@pytest.fixture
def page(request, browser_context):
    """
    Creates a new browser page for each test.
    - Navigates to the base URL
    - Starts tracing (if enabled)
    - Captures screenshots, traces, and videos for failed tests
    - Attaches all artifacts to Allure report
    """
    # Read test configuration
    base_url=request.config.getoption("--base_url")
    if base_url is None:
        base_url=request.config.getini("base_url")
    
    screenshot_option=request.config.getoption("--screenshot")
    if screenshot_option is None:
        screenshot_option=request.config.getini("screenshot")

    tracing_option=request.config.getoption("--tracing")
    if tracing_option is None:
        tracing_option=request.config.getini("tracing")

    
    video_option = request.config.getoption("--video")
    if video_option is None:
        video_option=request.config.getoption("video")

    print(f"[INFO] Navigating to: {base_url}")

    # Start tracing if enabled
    if tracing_option in ["on", "retain-on-failure"]:
        print("[TRACE] Tracing enabled - capturing screenshots and actions")
        browser_context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Create and navigate to base URL
    page = browser_context.new_page()
    page.goto(base_url)
    
    # Yield the page to the test
    yield page

    # ------------------------------------------------------------------------
    # After the test: manage artifacts (screenshots, videos, traces)
    # ------------------------------------------------------------------------
    test_name = request.node.name
    test_failed = hasattr(request.node, "rep_call") and request.node.rep_call.failed

    print(f"[RESULT] Test '{test_name}' result: {'[FAIL]' if test_failed else '[PASS]'}")

    # Save and attach trace
    if tracing_option in ["on", "retain-on-failure"]:
        trace_path = f"reports/traces/{test_name}_trace.zip"
        browser_context.tracing.stop(path=trace_path)
        print(f"[SAVE] Trace saved: {trace_path}")


    # Take screenshot if test failed
    if test_failed and screenshot_option in ["on", "only-on-failure"]:
        screenshot_path = f"reports/screenshots/{test_name}.png"
        page.screenshot(path=screenshot_path)
        print(f"[SAVE] Screenshot saved: {screenshot_path}")

        # Attach to Allure report
        allure.attach.file(
            screenshot_path,
            name=f"{test_name}_screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        print("[ATTACH] Screenshot attached to Allure report")

    # Attach video if available and test failed
    if test_failed and video_option in ["on", "retain-on-failure"]:
        video_path = page.video.path() if page.video else None
        if video_path and Path(video_path).exists():
            allure.attach.file(
                video_path,
                name=f"{test_name}_video",
                attachment_type=allure.attachment_type.WEBM
            )
            print("[ATTACH] Video attached to Allure report")
    page.close()


# ----------------------------------------------------------------------------
# FIXTURE 4 - api reuwst context for api automation
# ----------------------------------------------------------------------------
@pytest.fixture
def request_context(playwright_instance,request):
    api_base_url=request.config.getoption("--api_base_url")
    if api_base_url is None:
        api_base_url=request.config.getini("api_base_url")
    api_context=playwright_instance.request.new_context(base_url=api_base_url)
    yield api_context
    api_context.dispose()
