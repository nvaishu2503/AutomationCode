import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import openpyxl

@pytest.fixture(scope="class")
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    service_obj = Service("E:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.implicitly_wait(10)
    driver.get("http://localhost:3000/super/shops")
    driver.find_element(By.ID, "User Name").send_keys("admin")
    driver.find_element(By.ID, "Password").send_keys("admin@123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Add Shop']").click()
    return driver



@pytest.fixture(scope="class")
def adminsetup():

    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    service_obj = Service("E:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(options=options,service=service_obj)
    driver.implicitly_wait(10)
    driver.get("http://localhost:3000/admin")
    driver.maximize_window()
    driver.find_element(By.ID,"User Name").send_keys("newyorkerFin")
    driver.find_element(By.ID,"Password").send_keys("Product$123")
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    driver.find_element(By.XPATH,"//a[@href='/admin/categories']").click()
    driver.find_element(By.XPATH,"//button[normalize-space()='Add Category']").click()
    return driver


@pytest.fixture(scope="class")
def addproducts():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    service_obj = Service("E:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.implicitly_wait(10)
    driver.get("http://localhost:3000/admin")
    driver.maximize_window()
    driver.find_element(By.ID, "User Name").send_keys("newyorkerfin")
    driver.find_element(By.ID, "Password").send_keys("Product$123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.find_element(By.XPATH, "//a[@href='/admin/products']//div//span").click()
    driver.find_element(By.XPATH, "//body//div//div//div//div//div//div//div//button").click()
    driver.find_element(By.XPATH, "//body//div//div//div//div//div[1]//div[1]//div[1]//div[2]//div[2]//div[1]").click()
    return driver


@pytest.fixture(scope="class")
def ordering():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True)
    service_obj = Service("E:\chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service_obj)
    driver.implicitly_wait(10)
    driver.get("https://demo.vshops.fi/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//body/div/header/div/div[3]/div[1]/div[2]/div[1]").click()
    driver.find_element(By.ID, "Email").send_keys("praveena.vaishnavi1991@gmail.com")
    driver.find_element(By.ID, "Password").send_keys("Amritha$12")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    return driver