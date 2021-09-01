from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://fuuast.edu.pk/student-portal/login")

mobile_number_element = driver.find_element_by_xpath('//*[@id="tel"]')
mobile_number_element.send_keys("TYPE_YOUR_MOBILE_NUMBER_HERE")

password_element = driver.find_element_by_xpath('//*[@id="form-password"]')
password_element.send_keys("TYPE_YOUR_PASSWORD_HERE")

signin_button_element = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[2]/div/div/div[2]/form/button')
signin_button_element.click()
