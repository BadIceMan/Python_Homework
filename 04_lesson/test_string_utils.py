import pytest
from string_utils import StringUtils

utils = StringUtils()

# ================= 1. Метод capitalize =================


@pytest.mark.parametrize("input_string, expected", [
    ("skypro", "Skypro"),            # Позитивный: обычное слово
    ("123", "123"),                  # Позитивный: числа
    ("с пробелом", "С пробелом"),    # Позитивный: фраза с пробелом
    ("", ""),                        # Негативный: пустая строка
    (" ", " ")                       # Негативный: строка из пробела
])
def test_capitalize_positive_and_negative(input_string, expected):
    assert utils.capitalize(input_string) == expected


def test_capitalize_none():
    # Передача None вызывает падение утилиты (AttributeError)
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# ================= 2. Метод trim =================


@pytest.mark.parametrize("input_string, expected", [
    ("   skypro", "skypro"),         # Позитивный: пробелы слева
    ("skypro   ", "skypro   "),      # Позитивный: пробелы не должны удаляться
    ("   ", ""),                     # Граничный: только пробелы
    ("", "")                         # Негативный: пустая строка
])
def test_trim_positive_and_negative(input_string, expected):
    assert utils.trim(input_string) == expected


def test_trim_none():
    # Передача None вызывает падение утилиты (AttributeError)
    with pytest.raises(AttributeError):
        utils.trim(None)


# ================= 3. Метод contains =================


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("SkyPro", "S", True),           # Позитивный: символ в начале
    ("SkyPro", "Pro", True),         # Позитивный: поиск подстроки
    ("SkyPro", "U", False),          # Позитивный: символа нет
    ("", "A", False)                 # Негативный: пустая строка
])
def test_contains_positive_and_negative(input_string, symbol, expected):
    assert utils.contains(input_string, symbol) == expected


def test_contains_none_string():
    # КРИТИЧЕСКИЙ БАГ: передача None в строку ломает метод (Тест упадёт!)
    assert utils.contains(None, "S") is False


def test_contains_none_symbol():
    # КРИТИЧЕСКИЙ БАГ: передача None в символ ломает метод (Тест упадёт!)
    assert utils.contains("SkyPro", None) is False


# ================= 4. Метод delete_symbol =================


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),        # Позитивный: удаление буквы из середины
    ("SkyPro", "Pro", "Sky"),        # Позитивный: удаление подстроки
    ("SkyPro", "x", "SkyPro"),       # Позитивный: удаление символа
    ("", "a", "")                    # Негативный: пустая строка
])
def test_delete_symbol_positive_and_negative(input_string, symbol, expected):
    assert utils.delete_symbol(input_string, symbol) == expected


def test_delete_symbol_none_string():
    # Баг: падение при None
    assert utils.delete_symbol(None, "k") == ""


def test_delete_symbol_none_symbol():
    # Баг: падение при None
    assert utils.delete_symbol("SkyPro", None) == "SkyPro"
