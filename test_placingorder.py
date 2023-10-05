import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixturse("ordering")

def test_orderplaced(ordering):


    ordering.find_element(By.CSS_SELECTOR, "input[placeholder='Search for shop, events and products']").send_keys("Deli Deli")
    ordering.find_element(By.CSS_SELECTOR,"div[class*='user-header_name__NM4ee']").click()
    #driver.execute_script("return arguments[0].scrollIntoView(true);", viewall)
    #driver.execute_script("arguments[0].click();", viewall)

    order = ordering.find_element(By.CSS_SELECTOR,"button[class*='button_button__HzWwD  card_editButton__+PC5T']")
    ordering.execute_script("return arguments[0].scrollIntoView(true);", order)
    ordering.execute_script("arguments[0].click();",order)

    ordering.find_element(By.CSS_SELECTOR,"button[class*='button_button__HzWwD  form_saveButton__j-8-p']").click()

    adcart = ordering.find_element(By.CSS_SELECTOR, "div[class*='app-menu_cartSize__zBhIY']")
    ordering.execute_script("return arguments[0].scrollIntoView(true);", adcart)
    ordering.execute_script("arguments[0].click();", adcart)

    checkout = ordering.find_element(By.XPATH, "//body/div/div/div/div/div/div/button[1]")
    ordering.execute_script("return arguments[0].scrollIntoView(true);", checkout)
    ordering.execute_script("arguments[0].click();", checkout)

    payment = ordering.find_element(By.XPATH,"//div[4]//div[1]//div[3]//div[1]//div[1]")
    ordering.execute_script("return arguments[0].scrollIntoView(true);", payment)
    ordering.execute_script("arguments[0].click();", payment)

    ordering.find_element(By.ID,"rcc-confirm-button").click()

    orderplaced=ordering.find_element(By.CSS_SELECTOR,"button[class*='checkout-payment-section_button']")
    ordering.execute_script("return arguments[0].scrollIntoView(true);", orderplaced)
    ordering.execute_script("arguments[0].click();", orderplaced)



#Provence AOP locator=(By.CSS_SELECTOR,"button[class*='button_button__HzWwD  card_editButton__+PC5T']
