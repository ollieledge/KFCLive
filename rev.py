
from tabula import read_pdf
import tabula
import csv
from datetime import datetime
import tkinter as tk
import pyautogui
from twilio.rest import Client
import twilio
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


while True:
    service = Service('/home/ollie/Documents/chromedriver.exe')

    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option("prefs", {
    "download.default_directory": "/home/ollie/dashboard/data",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
})
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://kfcuk.macromatix.net/MMS_System_Reports.aspx?MenuCustomItemID=173")


    search_box = driver.find_element(By.ID, "Login_UserName")
    search_box.send_keys("okl5380")

    search_box = driver.find_element(By.ID, "Login_Password")
    search_box.send_keys("Roots123!")

    search_box = driver.find_element(By.ID, "Login_Button1")
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element(By.ID, "ctl00_ph_ListBoxReports")
    search_box.send_keys(Keys.ARROW_DOWN*4, Keys.SPACE)

    search_box = driver.find_element(By.ID, "ctl00_ph_ButtonGenerate_input")
    search_box.send_keys(Keys.TAB, Keys.ARROW_DOWN*2, Keys.SPACE)
    search_box = driver.find_element(By.ID, "ctl00_ph_ButtonGenerate_input")
    search_box.send_keys(Keys.RETURN)

    file_path = '/home/ollie/dashboard/data/HourlySalesByTradingDay-OKL5380 (1).csv'
    while not os.path.exists(file_path):
        time.sleep(1)

    driver.quit()

    file_path = '/home/ollie/dashboard/data/HourlySalesByTradingDay-OKL5380.csv'

    os.remove(file_path)

    time.sleep(1)
    os.rename('/home/ollie/dashboard/data/HourlySalesByTradingDay-OKL5380 (1).csv', '/home/ollie/dashboard/data/HourlySalesByTradingDay-OKL5380.csv')

    time.sleep(5)



