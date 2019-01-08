import logging
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

logger = logging.getLogger('Kibana Selenium Tests')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920x1080')

browser = webdriver.Chrome('/etc/selenium/chromedriver', chrome_options=options)
