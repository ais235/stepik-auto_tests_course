import os
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
import time
import math

from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return math.log(abs(12 * math.sin(x)))


def test_yandex_search():
    # путь к хром драйверу
    browser = WebDriver(executable_path="F:\selenium\chromedriver.exe")

    link = "http://suninjuly.github.io/explicit_wait2.html"

    try:
        browser.implicitly_wait(12)
        browser.get(link)

        price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
        print(price)
        button = browser.find_element_by_id('book')
        button.click()




        # window = browser.window_handles
        # browser.switch_to.window(window[1])

        # confirm = browser.switch_to.alert
        # confirm.accept()

        num1 = int(browser.find_element_by_id("input_value").text)
        x = calc(num1)

        input1 = browser.find_element_by_id("answer")
        input1.send_keys(str(x))

        button = browser.find_element_by_xpath("//button[@type='submit']")
        button.click()

        # input1 = browser.find_element_by_xpath("//label[contains(.,'First name*')]/following-sibling::input")
        # input1.send_keys("Ivan")
        # input2 = browser.find_element_by_xpath("//label[contains(.,'Last name*')]/following-sibling::input")
        # input2.send_keys("Petrov")
        # input3 = browser.find_element_by_xpath("//label[contains(.,'Email *')]/following-sibling::input")
        # input3.send_keys("qwe@ya.ru")
        #
        # element = browser.find_element_by_css_selector("#file")
        # current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
        # file_path = os.path.join(current_dir, 'requirements.txt')  # добавляем к этому пути имя файла
        # element.send_keys(file_path)

        # button = browser.find_element_by_tag_name("button")
        # browser.execute_script("window.scrollBy(0, 100);")
        #

        # box = browser.find_element_by_id("treasure")
        # attr_value = box.get_attribute("valuex")
        # print(attr_value)
        # x = int(attr_value)
        # y = calc(x)
        # print(y)

        # num1 = int(browser.find_element_by_id("num1").text)
        # num2 = int(browser.find_element_by_id("num2").text)
        # print(num1)
        # print(num2)
        # equally = num1 + num2
        # print(equally)
        #
        # select = Select(browser.find_element_by_tag_name("select"))
        # select.select_by_value(str(equally))  # ищем элемент с значение equally

        # x_element = browser.find_element_by_css_selector("[id='input_value']")
        # x = x_element.text
        # y = calc(x)

        # input1 = browser.find_element_by_css_selector("[id='answer']")
        # input1.send_keys(str(y))
        #
        # input2 = browser.find_element_by_css_selector("input[id='robotCheckbox']")
        # input2.click()
        #
        # input3 = browser.find_element_by_css_selector("input[id='robotsRule']")
        # input3.click()

        # # xpath ищет текстовое значение label а потом через following-sibling:: следующий за ним элемент input
        # input1 = browser.find_element_by_xpath("//label[contains(.,'First name*')]/following-sibling::input")
        # input1.send_keys("Ivan")
        # input2 = browser.find_element_by_xpath("//label[contains(.,'Last name*')]/following-sibling::input")
        # input2.send_keys("Petrov")
        # input3 = browser.find_element_by_xpath("//label[contains(.,'Email*')]/following-sibling::input")
        # input3.send_keys("qwe@ya.ru")
        # input4 = browser.find_element_by_xpath("//label[contains(.,'Phone:')]/following-sibling::input")
        # input4.send_keys("+7 303 123 45 78")
        # input5 = browser.find_element_by_xpath("//label[contains(.,'Address:')]/following-sibling::input")
        # input5.send_keys("Москва")
        #

        #
        # # Проверяем, что смогли зарегистрироваться
        # # ждем загрузки страницы
        # time.sleep(1)
        #
        # # находим элемент, содержащий текст
        # welcome_text_elt = browser.find_element_by_tag_name("h1")
        # # записываем в переменную welcome_text текст из элемента welcome_text_elt
        # welcome_text = welcome_text_elt.text
        #
        # # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
