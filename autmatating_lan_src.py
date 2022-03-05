from webbrowser import BaseBrowser
from selenium import webdriver
from time import sleep
browser = webdriver.Chrome()

browser.get('https://172.22.2.6/connect/PortalMain')

advance_click = browser.find_element_by_xpath('//*[@id="details-button"]')
advance_click.click()

procced_click = browser.find_element_by_xpath('//*[@id="proceed-link"]')
procced_click.click()
sleep(1)

enter_username = browser.find_element_by_xpath('//*[@id="LoginUserPassword_auth_username"]')
enter_username.send_keys('21ume041')
sleep(1)
enter_password = browser.find_element_by_xpath('//*[@id="LoginUserPassword_auth_password"]')
enter_password.send_keys('UwbE5180+')

click_log_in = browser.find_element_by_xpath('//*[@id="UserCheck_Login_Button_span"]')
click_log_in.click()
