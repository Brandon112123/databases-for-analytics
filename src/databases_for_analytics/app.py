"""app.py - Project script (example).

Author: Denise Case
Date: 2026-08

"""


# === DECLARE IMPORTS (BRING IN FREE CODE) ===

import logging
from typing import Final

from datafun_toolkit.logger import get_logger, log_header

# === CONFIGURE LOGGER ONCE PER MODULE (PYTHON FILE) ===

LOG: logging.Logger = get_logger("P01", level="INFO")

# === DECLARE GLOBAL CONSTANTS ===

# All of these global variables are CONSTANT and do NOT change when the program runs.
# By convention, constant variable names are all UPPERCASE_WITH_UNDERSCORES.
# Declare a variable and initialize it with a value for each of these common types:
#    str, int, float, bool, list of strings.
# Code like a pro: Use optional Python `type hints` to make types explicit
# Just add a colon and the type before the equals sign.
# If a variable is a constant, use Final from typing module.

COURSE_NAME: Final[str] = "Databases for Analytics"
COURSE_NUMBER: Final[int] = 661
COURSE_HOURS_PER_WEEK: Final[float] = 15.0
ASSUMES_PRIOR_EXPERIENCE: Final[bool] = (
    False  # NOTE: In Python, True and False are Capitalized (and not quoted).
)

HELPFUL_TRAITS: Final[list[str]] = [
    "patience",
    "curiosity",
    "humor",
    "tenacity",
]

# === DECLARE A FUNCTION TO FORMAT THE INFORMATION ===


def get_summary() -> str:
    """Get a formatted summary of the information held in the global variables.

    Arguments: None (nothing is passed in the parentheses after `get_summary`).

    Returns: - a formatted multi-line string (starts with f and wrapped in triple quotes).
    """
    summary: str = f"""
    Course Information:
        Course name: {COURSE_NAME}
        Course number: {COURSE_NUMBER}
        Course hrs/wk: {COURSE_HOURS_PER_WEEK:.2f}
        Assumes prior experience: {ASSUMES_PRIOR_EXPERIENCE}
        Helpful traits: {HELPFUL_TRAITS}

    """

    LOG.info("Generated formatted multi-line SUMMARY string.")
    LOG.info("Returning the str to the calling function.")
    return summary


# === DEFINE THE MAIN FUNCTION THAT CALLS OTHER FUNCTIONS ===


def main() -> None:
    """Entry point when running this file as a Python script.

    Arguments: None (nothing is passed in the parentheses after the `main`).

    Returns: None (nothing is returned when this function runs).

    This function creates what we call `side effects` -
    it just logs output to the console and a file.

    Use the LOG variable to call info() methods to log messages.
    Call the log_header() function once to log some key details that can help with debugging.
    Call the get_summary() function to get the formatted summary string,
    Log the summary string we get back from get_summary().
    """
    log_header(LOG, "DBA")

    LOG.info("===================================")
    LOG.info("START main()")
    LOG.info("===================================")

    summary: str = get_summary()
    LOG.info(summary)

    LOG.info("===================================")
    LOG.info("END main() - Executed successfully!")
    LOG.info("===================================")


# === CONDITIONAL EXECUTION GUARD ===

# WHY: This is standard Python "boilerplate" - we copy and paste it
# into every Python script. It is a "conditional execution" guard,
# meaning: if this file is being run as a script, then execute the code
# in the main() function.

if __name__ == "__main__":
    main()
