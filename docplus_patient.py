from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains
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
button=driver.find_element_by_css_selector('#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button')
ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(20)

##Add Reports No1
add_report=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[1]')
ActionChains(driver).move_to_element(add_report).click(add_report).perform()
driver.implicitly_wait(20)
##When Report Name and Report Type are not entered No1
addreportbutton=driver.find_element_by_class_name('ant-btn')
ActionChains(driver).move_to_element(addreportbutton).click(addreportbutton).perform()
driver.implicitly_wait(30)
##Report Naame and Report Type are entered No1
report_name=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/input')
report_name.send_keys('Radiology Report')
report_type=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input')
report_type.send_keys('CT Scan')
##Report file is uploaded No1
report_upload=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/input')
report_upload.send_keys('D:\CT-Scan-Report.pdf')
#Final Report is added No1
driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/center/button').click()
driver.implicitly_wait(20)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/a'))).click()
driver.implicitly_wait(20)
time.sleep(4)

button=driver.find_element_by_css_selector('#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button')
ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(20)
##Add Reports No2
add_report=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[1]')
ActionChains(driver).move_to_element(add_report).click(add_report).perform()
driver.implicitly_wait(20)
##Report Naame and Report Type are entered No2
report_name=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/input')
report_name.clear()
report_name.send_keys('Pathology Report')
report_type=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input')
report_type.clear()
report_type.send_keys('Tissue Scan')
##Report file is uploaded No2
report_upload=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/input')
report_upload.clear()
report_upload.send_keys('D:\Tissue-Scan-Report.pdf')
time.sleep(4)
#Final Report is added No2
driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/center/button').click()
driver.implicitly_wait(20)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/a'))).click()
driver.implicitly_wait(20)
time.sleep(4)

button=driver.find_element_by_css_selector('#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button')
ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(40)
##Add Reports No3
add_report1=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[1]')
ActionChains(driver).move_to_element(add_report1).click(add_report1).perform()
driver.implicitly_wait(20)
##Report Naame and Report Type are entered No3
report_name=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/input')
report_name.clear()
report_name.send_keys('Laboratory Report')
report_type=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/input')
report_type.clear()
report_type.send_keys('MRI Scan')
##Report file is uploaded No3
report_upload=driver.find_element_by_xpath('/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div/div/input')
report_upload.clear()
report_upload.send_keys('D:\MRI-Scan-Report.pdf')
time.sleep(5)
#Final Report is added No3
WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[7]/div/div[2]/div/div[2]/div[1]/div/form/center/button'))).click()
driver.implicitly_wait(20)
WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/a'))).click()
driver.implicitly_wait(30)

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Medication No1
add_report=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[2]')
ActionChains(driver).move_to_element(add_report).click(add_report).perform()
driver.implicitly_wait(20)
##Add PillName No1
pill_name=driver.find_element_by_css_selector('#nest-messages_name')
pill_name.send_keys('Paracetamol')
driver.implicitly_wait(30)
##Add course duration from and to No1
cal_from=driver.find_element_by_css_selector('#from')
cal_from.send_keys('2021/06/23')
driver.implicitly_wait(30)
cal_to=driver.find_element_by_css_selector('#to')
cal_to.send_keys('2021-06-30')
driver.implicitly_wait(30)
##Add Time No1
time1=driver.find_element_by_id('0')
time1.send_keys('17:15:30')
##Submit Medicine No1
sub=driver.find_element_by_css_selector('#nest-messages > center > div > div > div > div > button')
ActionChains(driver).move_to_element(sub).click(sub).perform()
driver.implicitly_wait(20)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()
time.sleep(5)
##Add Medication No2
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
add_report=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[2]')
ActionChains(driver).move_to_element(add_report).click(add_report).perform()
driver.implicitly_wait(20)
##Add PillName No2
pill_name=driver.find_element_by_css_selector('#nest-messages_name')
pill_name.send_keys('Rantidine')
driver.implicitly_wait(30)
##Add course duration from and to No2
cal_from=driver.find_element_by_css_selector('#from')
cal_from.send_keys('2018/06/22')
driver.implicitly_wait(30)
cal_to=driver.find_element_by_css_selector('#to')
cal_to.send_keys('2022-07-28')
driver.implicitly_wait(30)
##Add Time No2
time1=driver.find_element_by_id('0')
time1.send_keys('20:45:38')
##Submit Medicine No2
add_medicine=driver.find_element_by_css_selector('#nest-messages > center > div > div > div > div > button')
add_medicine.click()

##Add course duration from and to No3
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()
time.sleep(5)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
add_report=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[2]')
ActionChains(driver).move_to_element(add_report).click(add_report).perform()
driver.implicitly_wait(20)
time.sleep(3)
##Checking today and now buttons in course duration from and to time
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.CSS_SELECTOR,'#from')))).click()
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[9]/div/div/div/div/div[2]/a')))).click()
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.CSS_SELECTOR,'#to')))).click()
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[10]/div/div/div/div/div[2]/a')))).click()
time.sleep(4)
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.ID,'0')))).click()
time.sleep(4)
WebDriverWait(driver,20).until((EC.element_to_be_clickable((By.XPATH,'/html/body/div[11]/div/div/div/div/div[2]/ul/li[1]/a')))).click()
pill_name=driver.find_element_by_css_selector('#nest-messages_name')
pill_name.send_keys('Paracetamol')
add_medicine=driver.find_element_by_css_selector('#nest-messages > center > div > div > div > div > button')
add_medicine.click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()
time.sleep(5)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Allergies No1
add_allergy=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[3]')
ActionChains(driver).move_to_element(add_allergy).click(add_allergy).perform()
driver.implicitly_wait(20)
##When Allergy Type/Name,Reaction and Severity are not entered
addallergybutton=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addallergybutton).click(addallergybutton).perform()
driver.implicitly_wait(30)
##Adding Allergy Type/Name,Reaction and Severity No1
allergy_name=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div[1]/div/input')
allergy_name.send_keys('Skin Allergy')
reaction=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div[1]/div/input')
reaction.send_keys('Skin Rashes')
severity=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div[1]/div/input')
severity.send_keys('High')
addallergybutton=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addallergybutton).click(addallergybutton).perform()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Allergies No2
add_allergy=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[3]')
ActionChains(driver).move_to_element(add_allergy).click(add_allergy).perform()
driver.implicitly_wait(20)
##Adding Allergy Type/Name,Reaction and Severity No2
allergy_name=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div[1]/div/input')
allergy_name.send_keys('Dust Allergy')
reaction=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div[1]/div/input')
reaction.send_keys('Sneezing')
severity=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div[1]/div/input')
severity.send_keys('Medium')
addallergybutton=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addallergybutton).click(addallergybutton).perform()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()

time.sleep(3)
WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Allergies No3
add_allergy=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[3]')
ActionChains(driver).move_to_element(add_allergy).click(add_allergy).perform()
driver.implicitly_wait(20)
##Adding Allergy Type/Name,Reaction and Severity No3
allergy_name=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div[1]/div/input')
allergy_name.send_keys('Insect Allergy')
reaction=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div[1]/div/input')
reaction.send_keys('Drowsy Feeling')
severity=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div[1]/div/input')
severity.send_keys('Low')
addallergybutton=driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addallergybutton).click(addallergybutton).perform()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()


WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Surgeries No1
add_surgery=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[4]')
ActionChains(driver).move_to_element(add_surgery).click(add_surgery).perform()
driver.implicitly_wait(20)
surgery_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div/input')
surgery_name.send_keys('Skin Surgery')
surgeon_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div/div/input')
surgeon_name.send_keys('K Jeswanth')
or_ot=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div/div/input')
or_ot.send_keys('OT')
date=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[4]/div[2]/div/div[2]/div[1]/div/div/div/input')
date.send_keys('2021-06-23')
addsurgerybutton=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addsurgerybutton).click(addsurgerybutton).perform()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()


WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Surgeries No2
add_surgery=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[4]')
ActionChains(driver).move_to_element(add_surgery).click(add_surgery).perform()
driver.implicitly_wait(20)
surgery_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div/input')
surgery_name.send_keys('Heart Surgery')
surgeon_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div/div/input')
surgeon_name.send_keys('T Rohan')
or_ot=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div/div/input')
or_ot.send_keys('OR')
date=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[4]/div[2]/div/div[2]/div[1]/div/div/div/input')
date.send_keys('2022-07-14')
addsurgerybutton=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addsurgerybutton).click(addsurgerybutton).perform()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()
driver.implicitly_wait(30)


WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#Right-Screen > div.row.flex-container.justify-content-end.mr-2 > button'))).click()
driver.implicitly_wait(20)
##Add Surgeries No3
add_surgery=driver.find_element_by_xpath('/html/body/div[6]/div[3]/ul/li[4]')
ActionChains(driver).move_to_element(add_surgery).click(add_surgery).perform()
driver.implicitly_wait(20)
surgery_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[1]/div[2]/div/div[2]/div/div/input')
surgery_name.send_keys('Brain Surgery')
surgeon_name=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[2]/div[2]/div/div[2]/div/div/input')
surgeon_name.send_keys('S Aasish')
or_ot=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[3]/div[2]/div/div[2]/div/div/input')
or_ot.send_keys('OR')
date=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/div[4]/div[2]/div/div[2]/div[1]/div/div/div/input')
date.send_keys('2021-11-29')
addsurgerybutton=driver.find_element_by_xpath('/html/body/div[10]/div/div[2]/div/div[2]/div[1]/div/form/center/div/div/div/div/button')
ActionChains(driver).move_to_element(addsurgerybutton).click(addsurgerybutton).perform()
driver.implicitly_wait(30)
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()
driver.implicitly_wait(30)
time.sleep(3)
#deleting reports
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[4]/div[2]/div/div/div[4]/div/a'))).click()
i=1
while(i!=0):
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody/tr['+str(i)+']/td[5]/div/button'))).click()
        WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/table/tbody/tr['+str(i)+']/td[5]/div/div/a[2]'))).click()
        time.sleep(10)
    except:
        break
##Going to Family Members Page
driver.find_element_by_xpath('//html/body/div[1]/div[2]/div/div[1]/div/div/div/ul/span[4]/div').click()
##Adding family members
time.sleep(4)
WebDriverWait(driver,25).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div/div/button/span[1]'))).click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/center/div[2]/div/div/div/button'))).click()
first_name=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[1]/div/div[2]/div/div/input')
first_name.send_keys('M Sri')
last_name=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[2]/div/div[2]/div/div/input')
last_name.send_keys('Vibhav')
Email_address=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[3]/div/div[2]/div/div/input')
Email_address.send_keys('vibhav25012001@gmail.com')
Phone_number=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[4]/div/div[2]/div/div/div/input')
Phone_number.send_keys('9989051566')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[5]/div/div[2]/div[1]/div/div/div/span[1]/input').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[2]/div[1]/div/div/div[1]').click()
Relationship=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[6]/div/div[2]/div[1]/div/input')
Relationship.send_keys('Myself')
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[7]/div/div[2]/div/div/div/div/span[2]').click()
Birth_date=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/div/div[7]/div/div[2]/div[1]/div/div/div/input')
Birth_date.send_keys('2001/01/25')
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div/div/div/form/center/div[2]/div/div/div/button'))).click()
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[3]/div/div/div/a'))).click()

driver.close()