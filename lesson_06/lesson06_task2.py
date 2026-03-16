from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located(
    (By.ID, "newButtonName"))).send_keys("SkyPro")
button = wait.until(EC.element_to_be_clickable((By.ID, "updatingButton")))
button.click()

print(button.text)

driver.quit()
