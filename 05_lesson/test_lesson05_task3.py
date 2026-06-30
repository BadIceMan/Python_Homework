from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    # Запускаем браузер Chrome
    driver = webdriver.Chrome()

    # Ожидание элементов до 10 секунд
    driver.implicitly_wait(10)

    # 1. Откройте страницу со ссылками
    driver.get("https://httpbin.org/links/10")

    # 2. Найдите все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверьте, что количество ссылок равно 9
    assert len(links) == 9

    # 4. Проверьте, что все ссылки отображаются на странице
    for link in links:
        assert link.is_displayed() is True

    # 5. Проверьте, что текст первой ссылки содержит "1"
    assert "1" in links[0].text

    # Закрываем браузер
    driver.quit()
