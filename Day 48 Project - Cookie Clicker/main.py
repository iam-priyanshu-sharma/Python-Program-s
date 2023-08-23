from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "E:\BCA\Program's\chromedriver-win64\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path, log_path="NUL"))
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

main_timer = time.time() + 300

store_items = driver.find_elements(By.CSS_SELECTOR, "div #store b")
item_list = [item.text.split("-")[0].rstrip(" ") for item in store_items[0:7]]
item_list.reverse()
while time.time() < main_timer:
    buy_timer = time.time() + 13
    while time.time() < buy_timer:
        cookie.click()
    for item in item_list:
        buy_item = driver.find_element(By.ID, f"buy{item}")
        try:
            buy_item.click()
        except:
            pass
        else:
            time.sleep(0.01)
            buy_timer += 2

cookies_per_second = driver.find_element(By.ID, "cps")
print(cookies_per_second.text)
