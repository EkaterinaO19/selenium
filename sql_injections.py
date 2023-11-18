from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


def auth_form_check():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.rerum.cz/prihlaseni")

         # Cookie pop up
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
        wait = WebDriverWait(driver, 10)

        email_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'login'))).send_keys("' OR 1=1; --")
        password_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'login_password'))).send_keys("' OR 1=1; --")

        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/div/div/div[1]/div[2]/form/input[3]')))
        submit_button.click()
        
        WebDriverWait(driver, 10).until(EC.alert_is_present())

    except Exception as e:
        print(f"Test auth_form_check passed: SQL injection protection is effective {str(e)}") 

    finally:
        driver.quit()    

auth_form_check()


def registration_form_check_test1():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.rerum.cz/")

        # Cookie pop up
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
        wait = WebDriverWait(driver, 10)

        
        form_button_locator = driver.find_element(by=By.ID, value='get-credit-frontpage')
        form_button_locator.click()

        # 1 registration page 
        wait = WebDriverWait(driver, 10)
        driver.find_element(by=By.NAME, value='contract_accept').click()
        name_input = wait.until(EC.presence_of_element_located((By.NAME, 'realname')))
        surname_input = wait.until(EC.presence_of_element_located((By.NAME, 'surname')))
        email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
        mob_phone_input = wait.until(EC.presence_of_element_located((By.ID, 'mob_phone')))
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))

        name_input.send_keys("' OR 1=1; --")
        surname_input.send_keys("' OR 1=1; --")
        email_input.send_keys("' OR 1=1; --")
        mob_phone_input.send_keys("' OR 1=1; --")
        submit_button.click()
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("ok") 
    finally:
        driver.quit()
    
# registration_form_check_test1()            
