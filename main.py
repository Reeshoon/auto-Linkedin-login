from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import username, password,driver,eventLink

### load selenium driver
driver = webdriver.Chrome(driver)
driver.get(eventLink)
sleep(1)

### click the login button
login_click = driver.find_element_by_xpath\
            ("//a[@class='main__sign-in-link']")
sleep(1)
login_click.click()
driver.switch_to.window(driver.window_handles[-1])

### get username and password input boxes path
usernameLink = driver.find_element_by_xpath('//*[@id="username"]')
passwordLink = driver.find_element_by_xpath('//*[@id="password"]')

### input the email id and password
usernameLink.send_keys(username)
passwordLink.send_keys(password)

### click the login button
login_btn = driver.find_element_by_xpath\
            ("//button[@class='btn__primary--large from__button--floating']")
sleep(1)
login_btn.click()

driver.switch_to.window(driver.window_handles[-1])

attendees = driver.find_element_by_xpath("//list[@class='//div[@class='entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light']")
print(attendees)
