import time
from selenium import webdriver
from selenium.webdriver.common.by import By

USER = "standard_user"
PASS = "secret_sauce"
BASE = "https://www.saucedemo.com"


def log(msg: str) -> None:
    # easy to spot in pipeline logs and Log Analytics
    print(f"SEL: {msg}", flush=True)


def main() -> None:
    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=opts)
    driver.set_page_load_timeout(60)
    try:
        driver.get(BASE)

        driver.find_element(By.ID, "user-name").send_keys(USER)
        driver.find_element(By.ID, "password").send_keys(PASS)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        log(f"Logged in user: {USER}")

        # add two items
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        log("Added items: Sauce Labs Backpack, Sauce Labs Bike Light")

        # remove one item
        driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
        log("Removed item: Sauce Labs Bike Light")

        # assert the cart shows 1 item
        cart_qty = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert cart_qty == "1"

        log("Selenium test PASSED")
    except Exception as e:
        log(f"Selenium test FAILED: {e}")
        raise
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

