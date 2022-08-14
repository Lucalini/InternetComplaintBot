from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
chrome_driver_path = "C:/Users/evasa/Documents/chromedriver.exe"

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= chrome_driver_path)
        self.up = 10
        self.down = 200

    def get_intern_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]').click()
        time.sleep(50)
        try:
            self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a').click()
        except:
            pass
        actdownload = (self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span'))
        actupload = (self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span'))
        self.values = []
        self.values.append(float(actdownload.text))
        self.values.append(float(actupload.text))
        return(self.values)
    def tweet_at_provider(self, actual_down, actual_up, email, password):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        input_email = self.driver.find_element(By.NAME, 'text')
        input_email.send_keys(f"{email}")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()
        time.sleep(2)

        #if they check for security
        # security = self.driver.find_element(By.NAME, 'text')
        # security.send_keys("REDACTED")
        # self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()
        # time.sleep(4)
        input_pass = self.driver.find_element(By.NAME,'password')
        input_pass.send_keys(f"{password}")
        time.sleep(4)
        input_pass.send_keys(Keys.ENTER)
        time.sleep(10)
        tweet  = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey internet provider, Why is my download: {actual_down} and upload: {actual_up} when I pay for {self.down} and {self.up}")
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]').click()

    def close(self):
        self.driver.close()
