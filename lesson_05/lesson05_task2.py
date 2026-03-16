from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)

    button_xpath = ("//button[contains(concat(' ',"
                    " normalize-space(@class), ' '), ' btn-primary ')]")
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, button_xpath))
    )
    button.click()

    time.sleep(2)

finally:
    driver.quit()
