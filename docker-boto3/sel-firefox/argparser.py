import selenium
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import boto3
import sys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#firefox_options = webdriver.FirefoxOptions()
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
binary = FirefoxBinary(r'/usr/bin/firefox')
#driver = webdriver.Firefox(options=options)
caps = DesiredCapabilities.FIREFOX.copy()
caps['marionette'] = True
driver = webdriver.Firefox(firefox_binary=binary,capabilities=caps,executable_path=r"/usr/bin/geckodriver",options=firefox_options)

#url = "https://"+sys.argv[1]
Url = os.getenv('url')
print (Url)
url_Path="https://"+Url
driver.get(url_Path)
sleep(1)
screenshot = driver.save_screenshot("firefox-screenshot.png")
driver.quit()

#driver = webdriver.Chrome()
#driver.get('https://www.python.org')
sleep(1)

#driver.get_screenshot_as_file("screenshot.png")
client = boto3.client(
    's3',
    aws_access_key_id="XXXXXXX",
    aws_secret_access_key="XXXXXXXX",
    region_name='us-west-2'
)

response = client.upload_file("firefox-screenshot.png", "jannatlambda", "jannat-firefox-screenshot.png")

url= client.generate_presigned_url(
	ClientMethod='get_object',
	Params={'Bucket': "jannatlambda", 'Key': "jannat-firefox-screenshot.png"},
	ExpiresIn=1800,

)
print(url)
