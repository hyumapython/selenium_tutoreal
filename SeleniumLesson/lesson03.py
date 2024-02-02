# インポート
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# TODO:リンクにアクセス
driver.get('https://www.python.org/')

# TODO:要素の取得
element = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')

# TODO:情報の入力
sleep(3)
element.send_keys("python")
sleep(3)
gobutton = driver.find_element(By.XPATH, '//*[@id="submit"]')
gobutton.click()
sleep(5)
