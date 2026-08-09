import logging
from pathlib import Path
from datetime import datetime


def get_logger(name):

    # Project root
    project_root = Path(__file__).resolve().parent.parent

    # Log directory
    log_dir = project_root / "reports" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)

    # Create unique log file for each execution
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    log_file = log_dir / f"automation_{timestamp}.log"

    logger = logging.getLogger(name)

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # --------------------------------
    # File Handler
    # --------------------------------

    file_handler = logging.FileHandler(
        log_file,
        mode="a",
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)

    # --------------------------------
    # Console Handler
    # --------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    # --------------------------------
    # Format
    # --------------------------------

    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger