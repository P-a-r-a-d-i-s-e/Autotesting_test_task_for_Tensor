# pytest -v --tb=line test_search_for_Tensor_company_in_yandex.py - для запуска

from pages.main_page import MainPage

link = "https://yandex.ru"
REQUEST = "Тензор"

# Тесты были адаптированы под обновленный интерфейс Яндекс

def test_search_field_is_present(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_field()

def test_suggest_appeared(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_suggest(REQUEST)

def test_search_results_appeared(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_results(REQUEST)

def test_first_link_leads_to_the_tensor(browser):
    page = MainPage(browser, link)
    page.open()
    page.link_to_request(REQUEST)