# automatedtesting/selenium/login.py
import sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


USER = "standard_user"
PASS = "secret_sauce"
BASE = "https://www.saucedemo.com"

def log(msg):
    # easy to spot in pipeline logs and Log Analytics
    print(f"SEL: {msg}", flush=True)

def main():
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")        # comment this to see the browser locally
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(60)
    wait = WebDriverWait(driver, 10)           # <-- explicit waits

    try:
        driver.get(BASE)

        # Login
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(USER)
        wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys(PASS)
        wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        log(f"Logged in user: {USER}")

        # Add two items (inventory page)
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
        log("Added items: Sauce Labs Backpack, Sauce Labs Bike Light")

        # Wait for the "remove" button to appear, then click it
        wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light"))).click()
        log("Removed item: Sauce Labs Bike Light")

        # Optional: open cart and assert there is 1 item
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        log(f"Cart items after removal: {len(items)}")
        assert len(items) == 1, "Expected exactly 1 item in cart"

        log("Selenium test PASSED")

    except Exception as e:
        driver.save_screenshot("screenshots/selenium_failure.png")
        log(f"Selenium test FAILED: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    sys.exit(main())
