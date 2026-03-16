from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

wait = WebDriverWait(driver, 30)

wait.until(
    lambda driver: len(driver.find_elements(By.TAG_NAME, "img")) >= 4
)

images = driver.find_elements(By.TAG_NAME, "img")

print(images[3].get_attribute("src"))

driver.quit()
