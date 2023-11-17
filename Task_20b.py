from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.keys import Keys

class labour_gov_in:

    def __init__(self, web_url):
        self.url = web_url
        firefox_options = Options()
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.dir", "D:\\guvi_related")
        firefox_options.set_preference("browser.download.useDownloadDir", True)
        firefox_options.set_preference("browser.helperApps.alwaysAsk.force", False)
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip;application/gz")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    def fetch_Documents(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)
            # Mouse hover on to the Documents Menu
            element_to_hover = self.driver.find_element(by=By.XPATH, value="//a[text()='Documents']")
            hover = ActionChains(self.driver).move_to_element(element_to_hover)
            hover.perform()
            sleep(4)
            # Click on the monthly progress report
            self.driver.find_element(by=By.XPATH, value="//a[text()='Monthly Progress Report']").click()
            sleep(4)
            # Click on the August 2023 Download option
            self.driver.find_element(by=By.XPATH, value="//a[text()='Download(315.77 KB)']").click()
            sleep(4)
            # To accept the pop-up window which asks for opening in a new tab
            alert = self.driver.switch_to.alert
            alert.accept()
            sleep(4)
            self.driver.switch_to.window(self.driver.window_handles[1])
            # Locate and Click on the download button in the newly opened tab
            self.driver.find_element(by=By.XPATH, value="//button[@id='download']").click()
            sleep(2)
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()


        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            print("Executed")

# Click on the Media menu and go to Photo Gallery

    def fetch_Media(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.find_element(by=By.LINK_TEXT, value="Media").click()
            sleep(4)
            self.driver.find_element(by=By.LINK_TEXT, value="Photo Gallery").click()
            sleep(4)
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()


url = "https://labour.gov.in/"

gov = labour_gov_in(url)
gov.fetch_Documents()
gov.fetch_Media()



