from selenium import webdriver

from selenium.webdriver.common.by import By

browser = webdriver.Chrome('/home/karlygach/stepik/chromedriver')
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element(By.ID, "submit_button")
