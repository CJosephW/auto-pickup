import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import SMS
driver = webdriver.Firefox()

driver.get("https://www.hotschedules.com/hs/login.jsp")

usr = input('username')
pas = input('password')

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

driver.get('https://www.hotschedules.com/hs/menuParser.hs?screen=employeeHome&firstTime=true#/home?startDate=2019-09-07&showPickup=true')
time.sleep(5)
while len(driver.find_elements_by_css_selector('.spinner')) > 0:
    time.sleep(1)


shifts = driver.find_elements_by_css_selector('div.shift-pickup-item')
for i in range(len(shifts)):
    shifts = driver.find_elements_by_css_selector('div.shift-pickup-item')

    shifts[index].click()

    times = driver.find_elements_by_css_selector('div.table-item.shift-time')
    dates = driver.find_elements_by_css_selector('div.echo-component-EchoText-10vh5.echo-component-EchoText-3Pr7a.echo-component-EchoText-loCSL.echo-component-EchoText-3YRM3.echo-component-EchoText-2AVq7.echo-component-EchoText-2ZP5r.echo-component-EchoText-WQy-s')
    shift_locations_scrape = driver.find_elements_by_css_selector('div.table-item.location-name.pickup-table')
   

    shift_locations += [location.text for location in shift_locations_scrape]#todo fix for multiple shifts on one day


        
    for each_time in times:
        if each_time.text != 'SHIFT TIME':
            shift_times.append(each_time.text)#identical element with 'SHIFT TIME' text so I just get the right element by making sure it's anything but this

    for i in range(len(shift_locations_scrape)):    
        shift_dates += [date.text[28:] for date in dates]#giving a date for each time

    index += 1
    driver.refresh()#refreshes page since I couldn't get out of modal
        
    while len(driver.find_elements_by_css_selector('.spinner')) > 0:
        time.sleep(3)
    time.sleep(2)# Todo: find more effiecient way to wait for shift-info elements to be loaded in

formatted_list = []
for i in range(len(shift_locations)):
    formatted_list.append(shift_dates[i] +' '+ shift_locations[i] +' '+ shift_times[i])
    

for i in range(len(formatted_list)):
    message = formatted_list[i]
    SMS.send('\n'+message)

    
for datewe in shift_dates:
    print(datewe)


