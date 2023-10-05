from selenium import webdriver
#from webdriver_auto_update import
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
#check_driver('E:\chromedriver\chromedriver.exe')
service_obj = Service("E:\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(options=options,service=service_obj)
"""
options = webdriver.FirefoxOptions()
service_obj = Service("E:\geckodriver-v0.32.1-win64\geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service_obj)
"""
driver.implicitly_wait(10)
driver.get("http://localhost:3000/")
#driver.get("https://demo.vshops.fi/")
driver.maximize_window()
driver.find_element(By.XPATH,"//body/div/header/div/div[3]/div[1]/div[2]/div[1]").click()
driver.find_element(By.ID,"Email").send_keys("praveena.vaishnavi1991@gmail.com")
driver.find_element(By.ID,"Password").send_keys("Amritha$12")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
button = driver.find_element(By.XPATH,"//a[normalize-space()='Register']")
driver.execute_script("arguments[0].click();", button)
t1 = driver.current_window_handle
parent = driver.window_handles[0]
t2 = driver.window_handles[1]
driver.switch_to.window(t2)
admin = driver.find_element(By.XPATH,"//body/div/div/div/div/form/div[2]/div[1]/div[1]")
driver.execute_script("arguments[0].click();", admin)
driver.find_element(By.ID,"Name").send_keys("Sabun")
driver.find_element(By.ID,"Email").send_keys("praveena.vaishnavi1991@gmail.com")
driver.find_element(By.ID,"User Name").send_keys("Sabun")
driver.find_element(By.ID,"Password").send_keys("Varshini$12")
driver.find_element(By.ID,"Shop Name").send_keys("Sabun")
dropdown=Select(driver.find_element(By.ID,"Category"))
dropdown.select_by_index(2)
driver.find_element(By.ID,"Address Line 1").send_keys("Hakaniem kauppahalli")
driver.find_element(By.ID,"Address Line 2").send_keys("Kerros 3")
driver.find_element(By.ID,"City").send_keys("HELSINKI")
driver.find_element(By.ID,"State").send_keys("Finland")
driver.find_element(By.ID,"Pincode").send_keys("0260")
driver.find_element(By.ID,"Description").send_keys("Pure Luxury,Naturally")
driver.find_element(By.XPATH,"//button[normalize-space()='Register']").click()
