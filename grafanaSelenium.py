
import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome('/home/meg/Downloads/chromedriver')

browser.get('http://grafana.osh-infra.svc.cluster.local')
username = browser.find_element_by_name('username')
username.send_keys("admin")

password = browser.find_element_by_name('password')
password.send_keys("password")

login = browser.find_element_by_css_selector('body > grafana-app > div.main-view > div > div:nth-child(1) > div > div > div.login-inner-box > form > div.login-button-group > button')
login.click()

el = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Home'))
)

homeBtn = browser.find_element_by_link_text('Home')
homeBtn.click()


el = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Nodes'))
)

nodeBtn = browser.find_element_by_link_text('Nodes')
nodeBtn.click()

el = WebDriverWait(browser, 15).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div[2]/div/div[1]/div/div/div[1]/dashboard-grid/div/div[1]/div/plugin-component/panel-plugin-graph/grafana-panel/div/div[2]/ng-transclude/div/div[1]/canvas[2]'))
)

browser.save_screenshot('Grafana_Nodes.png')
