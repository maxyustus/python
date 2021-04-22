from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_EMAIL = "YOUR_LOGIN_EMAIL"
ACCOUNT_PASSWORD = "YOUR_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"
URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=111154941&keywords=python%20developer&location=Moscow%2C%20Moscow%20City%2C%20Russia"

chrome_driver_path = "/Users/mac/Documents/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(URL)

time.sleep(2)
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element_by_class_name("footer button")

        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
