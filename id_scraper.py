#Import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions, Chrome
import time
import csv

#Open CSV output file
file = open('linkedin_usersId.csv', 'w')
writer = csv.writer(file)
writer.writerow(['User ID'])

#Ask user for username and password
your_username = input('Enter username :')
your_password = input('Enter password :')

#Set keyword
TARGET = 'data scientist'

#Open Linkedin page on Chrome
driver = webdriver.Chrome('C:/Users/Nawfel/Documents/chromedriver.exe')
driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3Fkeywords%3Ddata%2520scientist%26origin%3DCLUSTER_EXPANSION%26sid%3DG%7EY&fromSignIn=true&trk=cold_join_sign_in")

#Find username and password textfield and fill them to login
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_key']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='session_password']")))

page_number = 1

username.clear()
password.clear()

username.send_keys(your_username)
password.send_keys(your_password)

log_in = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(3)

links_list = []

#Loop through all pages and get users id
for i in range(99):
    driver.execute_script("window.scrollTo(0,4000)")
    links = driver.find_elements_by_tag_name('a')
    print('Scraping Page : ', page_number)
    for link in links:
        if 'miniProfile' in link.get_attribute('href'):
            userid = link.get_attribute('href').split('/in/')[1].split('?mini')[0]
            if userid not in links_list:
                links_list.append(userid)
    page_number += 1
    change_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[aria-label='Page {page_number}']"))).click()
    time.sleep(7)

#Write to CSV
for i in range(len(links_list)):
    writer.writerow([links_list[i]])

print("File successfully created !")

file.close()