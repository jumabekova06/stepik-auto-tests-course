from selenium import webdriver
from time import sleep
link = "http://suninjuly.github.io/registration1.html"
# link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome('/home/karlygach/stepik/chromedriver')
browser.get(link)

# Код, который заполняет обязательные поля

# Заполнение поля "Имя"
nameInput = browser.find_element_by_css_selector(".first_class [placeholder='Input your first name']")
nameInput.send_keys("Karlygach")

# Заполнение поля "Фамилия"
lastnameInput = browser.find_element_by_css_selector(".second_class [placeholder='Input your last name']")
lastnameInput.send_keys("jumabekova")

# Заполнение поля "Email"
emailInput = browser.find_element_by_css_selector(".third_class [placeholder='Input your email']")
emailInput.send_keys("aika2000mail.com")
emailInput = browser.find_element_by_css_selector("div.form-group.first_class [placeholder='Input your phone:']")
emailInput.send_keys("59 kv")
emailInput = browser.find_element_by_css_selector("div.form-group.second_class [placeholder='Input your address:']")
emailInput.send_keys("+996700283624")
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
sleep(5)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Congratulations! You have successfully registered!" == welcome_text
browser.close()