"""Selenium helpers for UI tests."""

from selenium.webdriver.chrome.options import Options as ChromeOptions


def make_options(headless: bool = True) -> ChromeOptions:
    """Return a configured ChromeOptions instance."""
    options = ChromeOptions()
    if headless:
        options.add_argument("--headless")
    return options


def build_login_url(base_url: str) -> str:
    """Return the login page URL given a base URL."""
    return f"{base_url.rstrip('/')}/login"
