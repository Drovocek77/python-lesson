from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")

wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.ID, "ajaxButton"))).click()

success_element = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "p.bg-success")))
text = success_element.text
print(text)

driver.quit()
