import time
from selenium import webdriver
driver = webdriver.Firefox()

driver.get("https://www.hotschedules.com/hs/login.jsp")

usr =  'cameron.wise'
pas = 'april82002'

username = driver.find_element_by_id('loginusername')
username.clear()
username.send_keys(usr)

password = driver.find_element_by_id('loginpassword')
password.clear()
password.send_keys(pas)


shift_times = []
shift_dates = []
shift_locations = []

driver.find_element_by_id('loginBtn').click()

driver.get('https://www.hotschedules.com/hs/menuParser.hs?screen=employeeHome&firstTime=true#/home?startDate=2019-09-06&showPickup=true')

time.sleep(5)

while len(driver.find_elements_by_css_selector('.spinner')) > 0:
    time.sleep(1)

for items in driver.find_elements_by_css_selector('div.shift-pickup-item'):
    items.click()
    
    date = driver.find_element_by_css_selector('div.echo-component-EchoText-10vh5.echo-component-EchoText-3Pr7a.echo-component-EchoText-loCSL.echo-component-EchoText-3YRM3.echo-component-EchoText-2AVq7.echo-component-EchoText-2ZP5r.echo-component-EchoText-WQy-s')
    shift_location = driver.find_element_by_css_selector('div.table-item.location-name.pickup-table')
    
    shift_locations.append(shift_location.text)
    
    shift_dates.append(date.text[28:])
    
    times = driver.find_elements_by_css_selector('div.table-item.shift-time')
    
    
    for time in times:
        if time.text != 'SHIFT TIME':
            shift_times.append(time.text)
    driver.find_element_by_id("//use[@href='#iso-close']").click()
    
    

for shift in shift_times:
    print(shift)