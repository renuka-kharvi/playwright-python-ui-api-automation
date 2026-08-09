# Setup and Execution Instructions

## Prerequisites

Make sure the following are installed:

- Python 3.12+
- Git
- Playwright
- Allure CLI (optional, for Allure reporting)

# 1.Clone the Repository

-git clone <repository-url>
-cd  project firectory


# 2.Create a Virtual Environment
-python -m venv .venv
.venv\Scripts\Activate.ps1

3.Install Dependencies
pip install -r requirements.tx

4 Install Playwright Browsers
playwright install chromium
playwright install firefox

# Test Execution

Run All Tests  
     pytest

Run UI Tests Only
     pytest -m ui
    
Run API Tests Only
    pytest -m api

Run UI and API Tests
    pytest -m "ui or api"

# reporting

All reproting details added in pytest.ini

reports/
├── logs/
├── screenshots/
├── traces/
└── videos/


Open report for both UI and API

 allure serve .\reports\allure-results\



 # Framework / Design Approach

This project uses a modular and maintainable automation framework built with
Python, Pytest, and Playwright. The framework supports both UI and API
automation within the same project.

## Design Approach

The framework follows a layered architecture with clear separation of
responsibilities.

### 1. Page Object Model (POM)

UI automation follows the Page Object Model design pattern.

Each application page has a dedicated Page Object containing:

- Page locators
- Page-specific actions


For example:


pages/
├── base_page.py
├── home_page.py
├── search_page.py
├── item_page.py
└── cart_page.py

# 2. Base Page for Reusable Actions

Common Playwright operations are implemented in BasePage.
Page Objects inherit from BasePage and reuse these common methods instead
of duplicating code.


# 3. API Service Layer

API automation follows a service-layer approach.
BaseAPI contains reusable HTTP methods such as:
get_api()
post_api()
put_api()
delete_api()

Specific API classes, such as BitcoinAPI, contain business-specific
endpoints and operations.
This keeps API implementation details separate from test cases.

# 4. UI and API Test Independence

UI and API tests use separate fixtures.

               playwright_instance
                           |
             +-------------+-------------+
             |                           |
          browser_context                   request_context
             |                           
             v                   
          page

# 5. External Test Data
    Test data is maintained separately from the test implementation.
               testdata/
                ├── ui_data/
                │   └── add_to_cart.json
                │
                └── api_data/
                    └── bitcoin.json


#6. Centralized Logging

Python's built-in logging module is used for execution logging.

The logger is centralized in: utilities/logger.py  , Logs are written to:reports/logs/

# 7. Pytest Fixtures

Common test setup and teardown are maintained in:conftest.py

Fixtures are responsible for:

Starting Playwright
Creating browser instances
Creating browser contexts
Creating pages
Creating API request contexts
Cleaning up resources

# 8. Pytest Markers

Tests are categorized using custom markers: 
@pytest.mark.ui
@pytest.mark.api

ex - pytest -m ui  
pytest -m api

pytest -m "ui or api"

# 9. Failure Handling and Reporting

The framework captures debugging artifacts for UI failures:
reports/

├── screenshots/
├── traces/
├── videos/
└── logs/
└── allure-results
└── myreport.html

Allure and HTML reports provide visibility into test execution and failures.

This makes it easier to troubleshoot failures in both local and CI/CD
environments.

# 10 centerlized .env and config 
if any credential or secreate key you can add in .env  and read that in config.py

# pytest.ini
 All addopts can add in pytest.ini ,execute automation using command pytest


# 11. Scalability

The framework is designed so that new functionality can be added without
changing the existing architecture.

For a new UI page:pages/new_page.py

For a new API: api/new_api.py

For a new test:tests/ui/test_new_feature.py

For new test data: testdata/ui_data/new_test.json

This separation makes the framework easier to scale as the application and
automation suite grow.


# Design Goals

The framework is designed around the following principles:

Maintainability – UI and API implementation is separated from tests.
Reusability – Common actions are implemented in Base Page and Base API.
Scalability – New pages, APIs and test scenarios can be added easily.
Readability – Test cases focus on business workflows.
Data-driven testing – Test data is maintained externally in JSON.
Debuggability – Logs, screenshots, traces and videos are available.
Independent execution – API tests can run without launching a browser.
CI/CD readiness – Tests can be executed from Jenkins or other CI/CD
platforms.

# Overall Architecture

                         Pytest
                           |
             +-------------+-------------+
             |                           |
          UI Tests                    API Tests
             |                           |
             v                           v
        Page Objects                API Services
             |                           |
             v                           v
        Base Page                    Base API
             |                           |
             v                           v
      Playwright Page          APIRequestContext
             |                           |
             v                           v
        Web Application                REST API


       Supporting Components
       ---------------------
              |
       +------+------+
       |             |
    Test Data     Logging
       |             |
      JSON       reports/logs
       |
    Pytest
 Parameterization
       |
   Reporting
       |
  Allure / HTML