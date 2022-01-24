from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys




driver_path = r"C:\Users\Maxime\PycharmProjects\pythonProject1\chromedriver.exe"
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

pseudo = str(input("pseudo du joueur : "))
if len(pseudo)>0:
    s = Service(driver_path)
    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    browser = webdriver.Chrome(service=s, options=option)
    browser.get("https://rocketleague.tracker.network/")
    browser.maximize_window()
    sleep(2)
    cookies = browser.find_element_by_id("onetrust-accept-btn-handler").click()
    pub = browser.find_element_by_id("closeIconHit").click()
    upload_field = browser.find_element_by_xpath("//input[@type='search']")
    upload_field.send_keys(pseudo)
    upload_field.send_keys(Keys.ENTER)


