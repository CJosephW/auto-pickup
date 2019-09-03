from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.hotschedules.com/hs/login.jsp")
 
usr =  input('please enter username')
pas = input('please enter password')

username = driver.find_element_by_id('loginusername')
username.clear()
username.send_keys(usr)
 
password = driver.find_element_by_id('loginpassword')
password.clear()
password.send_keys(pas)
 
driver.find_element_by_id('loginBtn').click()
 
driver.get('https://www.hotschedules.com/hs/menuParser.hs?screen=employeeHome&firstTime=true#/home?startDate=2019-08-27&showPickup=true')
 
for items in driver.find_elements_by_css_selector('div.shift-pickup-item'):
    items.click()
    print(driver.find_elements_by_css_selector('strong.shift-info').text)
 
