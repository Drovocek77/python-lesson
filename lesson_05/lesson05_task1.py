from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    url = "http://uitestingplayground.com/classattr"
    driver.get(url)

    time.sleep(2)

    blue_button_xpath = ("//button[contains(concat(' ',"
                         " normalize-space(@class), ' '), ' btn-primary ')]")

    wait = WebDriverWait(driver, 10)
    blue_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, blue_button_xpath))
    )

    blue_button.click()

    time.sleep(2)

    alert = driver.switch_to.alert
    alert.accept()


finally:
    driver.quit()
