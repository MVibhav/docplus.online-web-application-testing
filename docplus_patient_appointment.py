from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
action=ActionChains
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get('https://docplus.online/')
driver.maximize_window()


driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/header/section/div/nav/div/div/div/div/a/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/header/section/div/nav/div/div/div/div/div/a[1]').click()
driver.implicitly_wait(10)
driver.find_element_by_css_selector('#welcome-sidebarLogin > div > div > img.pr-2').click()
driver.implicitly_wait(10)
email_input=driver.find_element_by_css_selector('#formFirstName')
email_input.send_keys('vibhav.2501@gmail.com')
password_input=driver.find_element_by_css_selector('#formPassword')
password_input.send_keys('Vibhav@123')
driver.find_element_by_class_name('btn-ca').click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'ant-notification-close-x'))).click()
#Clicking on Book a appointment button
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/a'))).click()
#Checking Now-Schedule button
time.sleep(20)
WebDriverWait(driver,40).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[4]/div[2]/div[1]/button')))).click()
time.sleep(20)
WebDriverWait(driver,40).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/div/main/div/div[3]/div/div[6]/div[1]/div/div/div[2]/div[3]/div/div[2]/button[1]')))).click()
time.sleep(20)
driver.back()
time.sleep(20)
#Checking right and left buttons on time
WebDriverWait(driver,40).until(((EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/div/main/div/div[3]/div/div[5]/div/div/div/div[3]/div/div/div/button[1]'))))).click()
WebDriverWait(driver,40).until(((EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[2]/div/main/div/div[3]/div/div[5]/div/div/div/div[3]/div/div/div/button[2]'))))).click()
#Checking search with different options entered No1
search=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[1]/div/div/span[1]/span/input')
search.send_keys('Eye Doctor')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[2]/div/div/input').click()
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div/div[1]/div[2]/table/tbody/tr[5]/td[5]')))).click()
time.sleep(10)
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[3]/div/div[2]')))).click()
time.sleep(20)
#Clicking schedule button for all the persons in the search No1
for i in range(1,11):
    print('No'+str(i)+' person in eye doctor')
    if(i!=2):
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[6]/div['+str(i)+']/div/div/div[2]/div[3]/div/div[2]/button[2]')))).click()
    else:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[6]/div['+str(i)+']/div/div/div[2]/div[4]/div/div[2]/button[2]')))).click()
    time.sleep(40)
    #Clicking on like and dislike buttons No1
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/span')))).click()
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/span')))).click()
    #Clicking on show more and show less buttons No1
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[3]/div/p/div/p')))).click()
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[3]/div/p/div/p')))).click()
    except:
        print('There is no show more option')
    #Adding Symptoms No1
    symptom=WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[3]/div/input'))))
    symptom.send_keys('Color Blindness')
    #Changing to In-person option
    try:
        WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/label[2]/span[1]')))).click()
    except:
        print('Only Tele-Consult option is available for this person')
    #Clicking on show more and show less buttons No1
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div')))).click()
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div')))).click()
        #Clicking on time
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div/div[1]')))).click()
    except:
        #Clicking on time
        try:
            WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[2]/div/div[1]/span')))).click()
        except:
            print('No slots available')
            driver.back()
            time.sleep(30)
            continue

    #Clicking on Book Now button
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.CLASS_NAME,'book-btn')))).click()
    time.sleep(30)
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[3]/form/div[3]/button')))).click()
    except:
        time.sleep(30)
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[3]/form/div[3]/button')))).click()
    time.sleep(40)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(20)
#Checking show more button No1
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[6]/div[11]/h5').click()
#Checking search with different options entered No2
search=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[1]/div/div/span[1]/span/input')
search.send_keys('Dentist')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[2]/div/div/input').click()
time.sleep(5)
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div/div[1]/div[2]/table/tbody/tr[5]/td[5]')))).click()
time.sleep(10)
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/section/div/div/div/div[3]/div/div[2]')))).click()
time.sleep(20)
#Clicking schedule button for all the persons in the search No2
for i in range(1,11):
    print('No.'+str(i)+' person in dentists')
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[6]/div['+str(i)+']/div/div/div[2]/div[3]/div/div[2]/button[2]')))).click()
    time.sleep(40)
    #Clicking on like and dislike buttons No2
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/span')))).click()
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/span')))).click()
    #Clicking on show more and show less buttons No2
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[3]/div/p/div/p')))).click()
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[1]/div[3]/div/p/div/p')))).click()
    except:
        print('There is no show more option')
    #Adding Symptoms No2
    symptom=WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[3]/div/input'))))
    symptom.send_keys('Tooth Ache')
    #Changing to In-person option
    try:
        WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/label[2]/span[1]')))).click()
    except:
        print('Only Tele-Consult option is available for this person')
    #Clicking on show more and show less buttons No2
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div')))).click()
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div')))).click()
        #Clicking on time
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[3]/div/div[1]')))).click()
    except:
        #Clicking on time
        try:
            WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/main/div/div/div/div/div[2]/div/div[2]/div/div[8]/div/div/div[2]/div/div[1]/span')))).click()
        except:
            print('No slots available')
            driver.back()
            time.sleep(30)
            continue

    #Clicking on Book Now button
    WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.CLASS_NAME,'book-btn')))).click()
    time.sleep(30)
    try:
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[3]/form/div[3]/button')))).click()
    except:
        time.sleep(30)
        WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div[4]/div/div/div/div/div[3]/form/div[3]/button')))).click()
    time.sleep(40)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(10)
    driver.back()
    time.sleep(40)
#Checking show more button No2
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/div/div[3]/div/div[6]/div[11]/h5').click()