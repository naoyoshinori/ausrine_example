from logging import WARNING, INFO, DEBUG
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set the logging level.
logging_level = DEBUG

# Configure the Chrome settings.
user_data_dir = r"C:\works\_tools\selenium\chrome\User Data"
profile_dir = r"Default"
download_dir = r"C:\works\_tools\selenium\chrome\Downloads"

# Define the sequences of Ausrine.
sequences = [
    {"get": {"url": "https://www.google.com/?hl=en"}},
    {"click": {"by": By.XPATH, "value": "//textarea[@title='Search']"}},
    {"send_keys": {"by": By.XPATH, "value": "//textarea[@title='Search']", "text": "iphone"}},
    {"send_keys": {"by": By.XPATH, "value": "//textarea[@title='Search']", "text": " 14", "append": True}},
    {"send_keys": {"by": By.XPATH, "value": "//textarea[@title='Search']", "text": Keys.ENTER}},
]
