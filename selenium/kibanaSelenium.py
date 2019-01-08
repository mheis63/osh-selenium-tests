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

# Get Grafana admin user name
if "KIBANA_USER" in os.environ:
  kibana_user = os.environ['KIBANA_USER']
  logger.info('Found Kibana username')
else:
  logger.critical('Kibana username environment variable not set')
  sys.exit(1)

if "KIBANA_PASSWORD" in os.environ:
  kibana_password = os.environ['KIBANA_PASSWORD']
  logger.info('Found Kibana password')
else:
  logger.critical('Kibana password environment variable not set')
  sys.exit(1)

if "KIBANA_URI" in os.environ:
  kibana_uri = os.environ['KIBANA_URI']
  logger.info('Found Kibana URI')
else:
  logger.critical('Kibana URI environment variable not set')
  sys.exit(1)

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1920x1080')

browser = webdriver.Chrome('/etc/selenium/chromedriver', chrome_options=options)

browser.get("http://"+kibana_user+":"+kibana_password+"@"+kibana_uri)
