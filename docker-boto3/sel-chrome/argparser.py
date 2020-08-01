from selenium import webdriver
from time import sleep
import boto3
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

Url = os.getenv('url')
print (Url)
url_Path="https://"+Url
driver.get(url_Path)
sleep(1)

screenshot = driver.save_screenshot("chrome-screenshot.png")
driver.quit()

#driver = webdriver.Chrome()
#driver.get('https://www.python.org')
sleep(1)

#driver.get_screenshot_as_file("screenshot.png")
client = boto3.client(
    's3',
    aws_access_key_id="AKIA2M6LCEP6MPIRHG7D",
    aws_secret_access_key="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",
    region_name='us-west-2'
)

response = client.upload_file("chrome-screenshot.png", "jannatlambda", "jannat-chrome-screenshot.png")

url= client.generate_presigned_url(
	ClientMethod='get_object',
	Params={'Bucket': "jannatlambda", 'Key': "jannat-chrome-screenshot.png"},
	ExpiresIn=1800,

)
print(url)

