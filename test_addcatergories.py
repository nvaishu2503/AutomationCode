import openpyxl
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("adminsetup")

def test_addcatergories(adminsetup):
    path1 = r'C:\Users\User\Desktop\vaishu test cases\vshopcatergories.xlsx'
    wb1 = openpyxl.load_workbook(path1)
    s = wb1.active
    c = s.cell(row=2,column=4)
    print(c.value)
    adminsetup.find_element(By.XPATH, "//body/div/div/div/div/div/div/div/div/div/div[2]/div[1]").click()
    adminsetup.find_element(By.ID, "EnglishName").send_keys(c.value)
    adminsetup.find_element(By.XPATH, "//button[@type='submit']").click()
