from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome('/home/karlygach/stepik/chromedriver')
browser.get(link)

try: 
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//*[label="First name*"]//input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//*[label="Last name*"]//input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//*[label="Email*"]//input')
    input3.send_keys("Smolensk@.sa.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()