from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    # Запускаем браузер Chrome
    driver = webdriver.Chrome()

    # Настройка неявного ожидания элементов
    driver.implicitly_wait(10)

    # 1. Откройте страницу формы
    driver.get("https://httpbin.org/forms/post")

    # 2. Найдите поле ввода по атрибуту name
    input_field = driver.find_element(By.NAME, "custname")

    # 3. Введите в него имя
    input_field.send_keys("John")

    # 4. Найдите кнопку Submit с помощью точного XPATH по тексту и нажмите
    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit']")
    submit_button.click()

    # 5. Проверьте, что после нажатия URL изменился
    # после отправки формы httpbin перенаправляет на страницу обработки данных
    assert driver.current_url != "https://httpbin.org/forms/post"

    # Закрываем браузер
    driver.quit()
