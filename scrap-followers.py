from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = 'your_username'
PASSWORD = 'your_password'
TARGET_PROFILE = 'target_profile'

# Setup WebDriver
driver = webdriver.Chrome()  # or use webdriver.Firefox()

def login():
    driver.get('https://www.instagram.com/accounts/login/')
    time.sleep(3)

    user_input = driver.find_element(By.NAME, 'username')
    pass_input = driver.find_element(By.NAME, 'password')

    user_input.send_keys(USERNAME)
    pass_input.send_keys(PASSWORD)
    pass_input.send_keys(Keys.RETURN)

    time.sleep(5)

def scrape_followers():
    driver.get(f'https://www.instagram.com/{TARGET_PROFILE}/followers/')
    time.sleep(5)

    followers_popup = driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
    last_height = 0
    followers = set()

    while len(followers) < 100:  # Adjust the number of followers to scrape
        elements = followers_popup.find_elements(By.XPATH, ".//li//a[contains(@href, '/')]")
        for el in elements:
            href = el.get_attribute("href")
            if href and href.startswith("https://www.instagram.com/"):
                username = href.split("/")[-2]
                followers.add(username)

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;", followers_popup)
        time.sleep(2)

    return list(followers)

def main():
    try:
        login()
        usernames = scrape_followers()
        print(f"\nFound {len(usernames)} followers:")
        for u in usernames
