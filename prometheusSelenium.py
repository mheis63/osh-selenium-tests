import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

browser = webdriver.Chrome('/home/meg/Downloads/chromedriver')

browser.get('http://admin:changeme@prometheus.osh-infra.svc.cluster.local')

el = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.NAME, 'submit'))
)

browser.save_screenshot('Prometheus_Dash.png')
