from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import time
from faker import Faker

fake = Faker()

def generate_random_code():
    first_part = 320109
    second_part = random.randint(100, 999)
    random_code = f"{first_part}/{second_part}"
    return random_code


def generate_random_id_number():
    random_number = random.randint(100000000, 999999999)
    return random_number


def fill_and_submit_form():
    try:
        driver = webdriver.Chrome()
        driver.get("https://www.rerum.cz/")

        # Cookie pop up
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'))).click()
        wait = WebDriverWait(driver, 10)

        
        form_button_locator = driver.find_element(by=By.ID, value='get-credit-frontpage')
        form_button_locator.click()


        wait = WebDriverWait(driver, 10)
        driver.find_element(by=By.NAME, value='contract_accept').click()


        # 1 registration page 
        try:
            name_input = wait.until(EC.presence_of_element_located((By.NAME, 'realname')))
            surname_input = wait.until(EC.presence_of_element_located((By.NAME, 'surname')))
            email_input = wait.until(EC.presence_of_element_located((By.ID, 'email')))
            mob_phone_input = wait.until(EC.presence_of_element_located((By.ID, 'mob_phone')))
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))

            name_input.send_keys(fake.name())
            surname_input.send_keys(fake.last_name())
            email_input.send_keys(fake.email())
            mob_phone_input.send_keys(fake.numerify('#########'))
            submit_button.click()
        except Exception as e:
            print(f"An error occurred in 1 registration page https://www.rerum.cz/register/1: {str(e)}")    
    
        
        # 2 registration page 
        try:
            # Státní občanství
            select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'nationality')))
            select_element.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#nationality option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            # Země narození
            select_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'country_of_birth')))
            select_element.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#country_of_birth option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            # Rodné číslo
            person_code = wait.until(EC.presence_of_element_located((By.ID, 'person_code')))
            person_code.send_keys(generate_random_code())

            # Místo narození
            wait.until(EC.presence_of_element_located((By.NAME, 'place_of_birth'))).send_keys('Praga')

            # Číslo občanského průkazu
            id_number = wait.until(EC.presence_of_element_located((By.NAME, 'id_number')))
            id_number.send_keys(generate_random_id_number())

            # Rodinný stav
            family_status_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "family_status")))
            family_status_select.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#family_status option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            education_degree_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "education_degree")))
            education_degree_select.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#education_degree option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            # Počet vyživovaných dětí
            driver.find_element(by=By.NAME, value='number_of_children').send_keys('1')

            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))
            submit_button.click()        
        except Exception as e:
            print(f"An error occurred in 2 registration page https://www.rerum.cz/register/2: {str(e)}")    


        # 3 registration page
        try:
            # Ulice
            wait.until(EC.presence_of_element_located((By.NAME, 'address'))).send_keys('Na Strži')

            # Číslo
            wait.until(EC.presence_of_element_located((By.NAME, 'house'))).send_keys('344/7')

            # Obec
            wait.until(EC.presence_of_element_located((By.NAME, 'city'))).send_keys('Prague 4')

            # PSČ
            wait.until(EC.presence_of_element_located((By.NAME, 'zipcode'))).send_keys('14000')

            # Způsob bydlení
            place_of_living_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "place_of_living")))
            place_of_living_select.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#place_of_living option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            # Bydlím zde od (měsíc)
            month_of_living_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "month_of_living")))
            month_of_living_select.click()
            options = driver.find_elements(By.CSS_SELECTOR, "#month_of_living option[value]:not([value=''])")
            random_option = random.choice(options)
            random_option.click()

            # Rok
            wait.until(EC.presence_of_element_located((By.NAME, 'year_of_living'))).send_keys(fake.random_int(min=1930, max=2023))

            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))
            submit_button.click()
        except Exception as e:
            print(f"An error occurred in 3 registration page https://www.rerum.cz/register/3: {str(e)}")       


        # 3 registration page (second part)
        try:
            income_type_select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "income_type")))
            income_type_select.click()
            student_option = driver.find_element(By.XPATH, '//*[@id="income_type"]/option[6]')
            student_option.click()
            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))
            submit_button.click() 
        except Exception as e:
            print(f"An error occurred in 3 registration page (second part) https://www.rerum.cz/register/3: {str(e)}")    

        # 4 registration page
        try:
            # Měsíční příjem
            wait.until(EC.presence_of_element_located((By.NAME, 'income'))).send_keys(random.randint(0, 100000))

            # Měsíční výdaje
            wait.until(EC.presence_of_element_located((By.NAME, 'expenses'))).send_keys(random.randint(0, 100000))

            # Počet členů domácnosti
            wait.until(EC.presence_of_element_located((By.NAME, 'household_members'))).send_keys(random.randint(0, 100))

            # Počet členů domácnosti s příjmem
            wait.until(EC.presence_of_element_located((By.NAME, 'household_members_with_income'))).send_keys(random.randint(0, 100))
            time.sleep(5)
    
            # Číslo účtu
            wait.until(EC.presence_of_element_located((By.NAME, 'account_number'))).send_keys('19-60004/0800')

            submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Pokračovat"]')))
            submit_button.click()  
            time.sleep(50000)
       
        except Exception as e:
            print(f"An error occurred in 4 registration page https://www.rerum.cz/register/4: {str(e)}")        

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.quit()

# Example usage
fill_and_submit_form()           
