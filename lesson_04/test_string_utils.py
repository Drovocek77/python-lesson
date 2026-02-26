import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


class TestCapitalize:

    def test_capitalize_positive_lowercase(self, string_utils):
        """Позитивный тест 1: слово с маленькой буквы"""
        assert string_utils.capitalize("skypro")

    def test_capitalize_positive_one_letter(self, string_utils):
        """Позитивный тест 2: строка из одной буквы"""
        assert string_utils.capitalize("a")

    def test_capitalize_positive_russian(self, string_utils):
        """Позитивный тест 3: слово с большой буквы"""
        assert string_utils.capitalize("Привет")

    def test_capitalize_negative_empty(self, string_utils):
        """Негативный тест 1: пустая строка"""
        assert string_utils.capitalize("")

    def test_capitalize_negative_numbers(self, string_utils):
        """Негативный тест 2: строка начинается с цифры"""
        assert string_utils.capitalize("123abc")

    def test_capitalize_negative_special_chars(self, string_utils):
        """Негативный тест 3: строка начинается со спецсимвола"""
        assert string_utils.capitalize("@#$%")


class TestTrim:

    def test_trim_positive_normal(self, string_utils):
        """Позитивный тест 1: пробелы в начале"""
        assert string_utils.trim("   skypro")

    def test_trim_positive_many_spaces(self, string_utils):
        """Позитивный тест 2: много пробелов в начале"""
        assert string_utils.trim("               skypro")

    def test_trim_positive_spaces_and_text(self, string_utils):
        """Позитивный тест 3: пробелы в начале текст и пробелы в конце"""
        assert string_utils.trim("  hello world  ")

    def test_trim_negative_no_spaces(self, string_utils):
        """Негативный тест 1: слово без пробелов"""
        assert string_utils.trim("skypro")

    def test_trim_negative_empty(self, string_utils):
        """Негативный тест 2: пустая строка"""
        assert string_utils.trim("")

    def test_trim_negative_only_spaces(self, string_utils):
        """Негативный тест 3: только пробелы"""
        assert string_utils.trim("     ")


class TestContains:

    def test_contains_positive_single_char(self, string_utils):
        """Позитивный тест 1: поиск одного символа"""
        assert string_utils.contains("SkyPro", "S")

    def test_contains_positive_substring(self, string_utils):
        """Позитивный тест 2: поиск полслова"""
        assert string_utils.contains("SkyPro", "Sky")

    def test_contains_positive_special_char(self, string_utils):
        """Позитивный тест 3: поиск спецсимвола"""
        assert string_utils.contains("Hello@World", "@")

    def test_contains_negative_no_symbol(self, string_utils):
        """Негативный тест 1: символ отсутствует"""
        assert string_utils.contains("SkyPro", "U")

    def test_contains_negative_empty_string(self, string_utils):
        """Негативный тест 2: пустая строка"""
        assert string_utils.contains("", "S")

    def test_contains_negative_case_sensitive(self, string_utils):
        """Негативный тест 3: несовпадение регистра"""
        assert string_utils.contains("SkyPro", "s")


class TestDeleteSymbol:

    def test_delete_positive_single_char(self, string_utils):
        """Позитивный тест 1: удаление одного символа"""
        assert string_utils.delete_symbol("SkyPro", "k")

    def test_delete_positive_substring(self, string_utils):
        """Позитивный тест 2: удаление подстроки"""
        assert string_utils.delete_symbol("SkyPro", "Pro")

    def test_delete_positive_multiple_occurrences(self, string_utils):
        """Позитивный тест 3: удаление всех вхождений"""
        assert string_utils.delete_symbol("Hello World", "l")

    def test_delete_negative_no_symbol(self, string_utils):
        """Негативный тест 1: удаление несуществующего символа"""
        assert string_utils.delete_symbol("SkyPro", "X")

    def test_delete_negative_empty_string(self, string_utils):
        """Негативный тест 2: пустая строка"""
        assert string_utils.delete_symbol("", "a")

    def test_delete_negative_empty_symbol(self, string_utils):
        """Негативный тест 3: пустой символ для удаления"""
        assert string_utils.delete_symbol("SkyPro", "")
