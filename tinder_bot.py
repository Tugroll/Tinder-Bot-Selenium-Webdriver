from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

class TinderBot:
    def __init__(self):
        self.driver = webdriver.Chrome()

        self.driver.get("http://www.tinder.com")


    def log_in(self):
        sleep(2)
        login_button = self.driver.find_element(By.XPATH, value='//*[text()="Log in"]')
        login_button.click()
        sleep(2)
        fb_login = self.driver.find_element(By.XPATH,
                                       value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login.click()

    def facebook_log_in_screen(self):
        sleep(2)
        base_window = self.driver.window_handles[0]
        fb_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(fb_login_window)

    def log_in_facebook(self,FB_EMAIL,FB_PASSWORD):
        email = self.driver.find_element(By.XPATH, value='//*[@id="email"]')
        password = self.driver.find_element(By.XPATH, value='//*[@id="pass"]')
        email.send_keys(FB_EMAIL)
        password.send_keys(FB_PASSWORD)
        password.send_keys(Keys.ENTER)

    def switching_base_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def allow_location_cookies_location(self):
        sleep(5)

        allow_location_button = self.driver.find_element(By.XPATH,
                                                    value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_location_button.click()

        notifications_button = self.driver.find_element(By.XPATH,
                                                   value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notifications_button.click()

        cookies = self.driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookies.click()

    def swipping_bot(self):
        for n in range(100):

            # Add a 1 second delay between likes.
            sleep(1)

            try:
                print("called")
                like_button = self.driver.find_element(By.XPATH, value=
                '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
                like_button.click()

            # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
            except ElementClickInterceptedException:
                try:
                    match_popup = self.driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
                    match_popup.click()

                # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
                except NoSuchElementException:
                    sleep(2)


    def run(self, FB_EMAIL, FB_PASSWORD):
        self.log_in()
        self.facebook_log_in_screen()
        self.log_in_facebook(FB_EMAIL, FB_PASSWORD)
        self.switching_base_window()
        self.allow_location_cookies_location()
        self.swipping_bot()

        self.driver.quit()
