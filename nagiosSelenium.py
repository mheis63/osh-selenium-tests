import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

browser = webdriver.Chrome('/home/meg/Downloads/chromedriver')
browser.get('http://nagiosadmin:password@nagios.osh-infra.svc.cluster.local')

sideFrame = browser.switch_to.frame('side')

services = browser.find_element_by_link_text('Services')
services.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('/home/meg/Nagios_Services.png')

hostGroups = browser.find_element_by_link_text('Host Groups')
hostGroups.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('Nagios_HostGroups.png')

hosts = browser.find_element_by_link_text('Hosts')
hosts.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('Nagios_Hosts.png')
