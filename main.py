from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[0]
    discard_button.click()


# webdriver helps us automate tasks in the browser

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# The driver is sending the required headers that a website would want
driver = webdriver.Chrome(options=chrome_options)

# Grab the website we want to scrape
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3930748816&distance=25&f_AL=true"
           "&f_TPR=r604800&geoId=102448103&keywords=Python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

email = driver.find_element(By.ID, value="username")
password = driver.find_element(By.ID, value="password")

email.send_keys(EMAIL)
password.send_keys(PASSWORD)

sign_in_user = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
sign_in_user.click()
time.sleep(3)

# Saves one job and follows the company
# save_button = driver.find_element(By.XPATH, value='//*[@id="main"]/div/div[2]/
# div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[1]/div[5]/div/button')
# save_button.click()
# time.sleep(5)

# follow_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-company__box button')
# follow_button.click()

# Applies to all jobs in the list that only requires 1-step to apply
job_list = driver.find_elements(By.CSS_SELECTOR, value=".scaffold-layout__list-container li")
for listing in job_list:
    time.sleep(2)
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.text == "Next":
            abort_application()
            print("Complex application, skipped.")
            time.sleep(2)
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            # submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        time.sleep(2)
        continue

time.sleep(5)
driver.quit()




