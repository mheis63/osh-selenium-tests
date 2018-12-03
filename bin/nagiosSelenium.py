import pdb

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

# Create logger, console handler and formatter
logger = logging.getLogger('Nagios Selenium Tests')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Set the formatter and add the handler
ch.setFormatter(formatter)
logger.addHandler(ch)

# Get Grafana admin user name
if "NAGIOS_USER" in os.environ:
  grafana_user = os.environ['NAGIOS_USER']
  logger.info('Found Nagios username')
else:
  logger.critical('Nagios username environment variable not set')
  sys.exit(1)

if "NAGIOS_PASSWORD" in os.environ:
  nagios_password = os.environ['NAGIOS_PASSWORD']
  logger.info('Found Nagios password')
else:
  logger.critical('Nagios password environment variable not set')
  sys.exit(1)

if "NAGIOS_URI" in os.environ:
  grafana_uri = os.environ['NAGIOS_URI']
  logger.info('Found Nagios URI')
else:
  logger.critical('Nagios URI environment variable not set')
  sys.exit(1)

browser = webdriver.Chrome('/tmp/chromedriver')
browser.get('http://'+NAGIOS_USER+':'+NAGIOS_PASSWORD+'@'+NAGIOS_URI)

sideFrame = browser.switch_to.frame('side')

services = browser.find_element_by_link_text('Services')
services.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('Nagios_Services.png')

hostGroups = browser.find_element_by_link_text('Host Groups')
hostGroups.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('Nagios_HostGroups.png')

hosts = browser.find_element_by_link_text('Hosts')
hosts.click()

el = WebDriverWait(browser, 15)
browser.save_screenshot('Nagios_Hosts.png')
