from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    # 1. Открываем главную страницу
    driver.get("https://httpbin.org/")

    # Проверяем, что нет ошибки 503
    assert "503" not in driver.title, "Ошибка 503: Сервер недоступен"

    # 2. Находим и кликаем на ссылку "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()

    # 3. Проверяем, что URL изменился на нужный
    assert driver.current_url == "https://httpbin.org"

    # 4. Возвращаемся назад на главную страницу
    driver.back()

    # 5. Проверяем, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.org/"

    driver.quit()
