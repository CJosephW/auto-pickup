import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

driver.get("https://www.hotschedules.com/hs/login.jsp")

usr =  ''
pas = ''

username = driver.find_element_by_id('loginusername')
username.clear()
username.send_keys(usr)

password = driver.find_element_by_id('loginpassword')
password.clear()
password.send_keys(pas)

wait = WebDriverWait(driver, 10)

shift_times = []
shift_dates = []
shift_locations = []
index = 0
driver.find_element_by_id('loginBtn').click()

driver.get('https://www.hotschedules.com/hs/menuParser.hs?screen=employeeHome&firstTime=true#/home?startDate=2019-09-06&showPickup=true')


time.sleep(5)

while len(driver.find_elements_by_css_selector('.spinner')) > 0:
    time.sleep(1)


shifts = driver.find_elements_by_css_selector('div.shift-pickup-item')
for i in range(len(shifts)):
    shifts = driver.find_elements_by_css_selector('div.shift-pickup-item')

    shifts[index].click()
    
    date = driver.find_element_by_css_selector('div.echo-component-EchoText-10vh5.echo-component-EchoText-3Pr7a.echo-component-EchoText-loCSL.echo-component-EchoText-3YRM3.echo-component-EchoText-2AVq7.echo-component-EchoText-2ZP5r.echo-component-EchoText-WQy-s')
    shift_location = driver.find_element_by_css_selector('div.table-item.location-name.pickup-table')
        
    shift_locations.append(shift_location.text)
        
    shift_dates.append(date.text[28:])
        
    times = driver.find_elements_by_css_selector('div.table-item.shift-time')
        
        

    for timef in times:
        if timef.text != 'SHIFT TIME':
            shift_times.append(timef.text)

    index += 1
    driver.refresh()#refreshes page since I couldn't get out of modal
        
    while len(driver.find_elements_by_css_selector('.spinner')) > 0:
        time.sleep(5)
    time.sleep(10)# Todo: find more effiecient way to wait for shift-info elements to be loaded in
