import os

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.implicitly_wait(15)
browser.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
delay = 10
try:
    myElem = WebDriverWait(browser, delay).until(ec.presence_of_element_located((By.ID, 'onesignal-slidedown-dialog')))
    cancel = browser.find_element_by_id("onesignal-slidedown-cancel-button")
    cancel.click()
except ElementClickInterceptedException:
    element = browser.find_element_by_class_name("elementor-container elementor-column-gap-default")
    browser.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, element)

# name
user_name = browser.find_element_by_xpath("//input[@name='username']").send_keys("Anna")

# pass
password = browser.find_element_by_xpath("//input[@name='password']").send_keys("Password1")

# comments
comments = browser.find_element_by_xpath("//textarea[@name='comments']")
comments.clear()
comments.send_keys("No comment")

# checkbox
checkbox = browser.find_element_by_xpath("//input[@value='cbselenium']")
browser.execute_script("arguments[0].scrollIntoView(true);", checkbox)
checkbox.click()

# radiobutton
radio_button = browser.find_element_by_xpath("//input[@name='radioselenium']")
browser.execute_script("arguments[0].scrollIntoView(true);", radio_button)
radio_button.click()

# multiple
multiple_values = browser.find_element_by_xpath("//option[@value='msselenium']").click()

# dropdown
drpdown = browser.find_element_by_xpath("//select[@name='dropdown']")
drpdown.click()
itemsInDropdown = browser.find_element_by_xpath("//option[@value='ddautomation']")
itemsInDropdown.click()

# datepicker

datepicker = browser.find_element_by_xpath("//input[@type='date']")
datepicker.send_keys(27022021)

# upload

upload_button = browser.find_element_by_xpath("//input[@type='file']")
upload_button.send_keys(os.getcwd() + "/text_file.txt")

# download

download_item = browser.find_element_by_xpath("(//a[@rel='nofollow noopener noreferrer'])[1]")
download_item.click()


# table
table_item = browser.find_element_by_xpath("//input[@name='female']")
browser.execute_script("arguments[0].scrollIntoView(true);", table_item)
table_item.click()

# click Button
button = browser.find_element_by_xpath("//input[@value='Button']").click()
