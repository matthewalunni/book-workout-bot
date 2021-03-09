from logging import setLogRecordFactory
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import username, password
import datetime
import time

class SeleniumHelper():
    """This class is used to automatically book gym workouts"""
    def __init__(self) -> None:
        # configure webdriver
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = driver = webdriver.Chrome(ChromeDriverManager().install())
        pass
    
    def openWebPage(self, url):
        """This method opens a page at a desired url

        Args:
            url (string): page to navigate to
        """
        self.driver.get(url)
        time.sleep(5)
        pass

    def _fillField(self, input, xpath):
        """This method fills a field at a specified xpath

        Args:
            input (string): text to be inserted into desired field
            xpath (string): xpath of desired field
        """
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(input)
            time.sleep(1)
        except: 
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.driver.find_element_by_xpath(xpath).send_keys(input)
            time.sleep(1)
        pass

    def findElementByText(self, text):
        """This method finds a page element by its text

        Args:
            text (string): text to be searched for

        Returns:
            selenium element: selenium element
        """
        return self.driver.find_element(By.XPATH, f"//*[text()='{text}']")
    
    def findElementByXPATH(self, xpath):
        """This method finds a page element by its xpath

        Args:
            xpath (string): elements page xpath

        Returns:
            selenium element: selenium element
        """
        return self.driver.find_element(By.XPATH, xpath)

    pass
    

if __name__ == "__main__":
    b =  SeleniumHelper()
    b.openWebPage("https://www.goodlifefitness.com/book-workout.html")

    today = datetime.datetime.now()
    print(f"Todays Date: {today}")

    nextAvailableBookDate = today + datetime.timedelta(days=3)
    print(f"Next Available Book Date: {nextAvailableBookDate}")
    nextAvailableBookDate = nextAvailableBookDate.strftime("%a, %b %d")

    dayXPath = """//*[@id="js-class-schedule-weekdays-container"]/li[4]"""
    b.findElementByXPATH(dayXPath).send_keys(Keys.ENTER)

    CoEdXPath = """//*[@id="typeGym Floor"]"""
    b.findElementByXPATH(CoEdXPath).send_keys(Keys.ENTER)

    bookWorkoutXPath = """//*[@id="day-number-4"]/li[10]/div[2]/div/div[2]/div[1]/button"""
    b.findElementByXPATH(bookWorkoutXPath).send_keys(Keys.ENTER)

    time.sleep(5)
    usernameXPath = """//*[@id="page-cbd68da9f6"]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[1]/label/input"""
    passwordXPath = """//*[@id="page-cbd68da9f6"]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[2]/label/input"""
    b._fillField(username, usernameXPath)
    b._fillField(password, passwordXPath)

    loginXPath = """//*[@id="page-cbd68da9f6"]/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[2]/div/div[2]/form/div[4]/button"""
    b.findElementByXPATH(loginXPath).send_keys(Keys.ENTER)

    time.sleep(5)
    dayXPath = """//*[@id="js-class-schedule-weekdays-container"]/li[4]"""
    b.findElementByXPATH(dayXPath).send_keys(Keys.ENTER)

    CoEdXPath = """//*[@id="typeGym Floor"]"""
    b.findElementByXPATH(CoEdXPath).send_keys(Keys.ENTER)

    #ALERT change me to select desired time
    bookWorkoutXPath = """//*[@id="day-number-4"]/li[10]/div[2]/div/div[2]/div[1]/button""" 
    b.findElementByXPATH(bookWorkoutXPath).send_keys(Keys.ENTER)

    time.sleep(5)
    IAgreePath = """//*[@id="js-workout-booking-agreement-input"]"""
    b.findElementByXPATH(IAgreePath).send_keys(Keys.ENTER)

    confirmXPath = """//*[@id="class-modal-container"]/div[4]/div/button[1]"""
    b.findElementByXPATH(confirmXPath).send_keys(Keys.ENTER)