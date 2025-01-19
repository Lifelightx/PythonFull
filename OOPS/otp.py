from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your chromedriver
chrome_driver_path = "path/to/chromedriver"  # Replace this with the correct path

# Set up the Service for the WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://web.whatsapp.com")

input("Scan the QR code and press Enter...")

# Search for the contact
search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@title="Search input textbox"]')
search_box.click()
search_box.send_keys("Contact Name")  # Replace with the name of the contact
search_box.send_keys(Keys.RETURN)

# Type and send the message
time.sleep(2)  # Wait for the chat to load
message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@title="Type a message"]')
message_box.click()
message_box.send_keys("Hello, this is an automated message!")
message_box.send_keys(Keys.RETURN)

time.sleep(5)  # Wait to ensure the message is sent
driver.quit()
