# pytest -v --tb=line test_images_on_Yandex.py - для запуска

from pages.main_page import MainPage
from pages.images_page import ImagesPage

link = "https://yandex.ru"
images_link = "https://yandex.ru/images/"

# Тесты были адаптированы под обновленный интерфейс Яндекс

def test_image_link_is_present_in_min_suggest(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_image_link()

def test_switched_to_pictures(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_click_on_the_image_link()

def test_category_name_is_displayed_in_the_search_field(browser):
    page = ImagesPage(browser, images_link)
    page.open()
    page.should_be_category_name_in_the_search_field()

def test_picture_opened_by_clicking(browser):
    page = ImagesPage(browser, images_link)
    page.open()
    page.should_be_the_picture_is_open()

def test_picture_changed_by_pressing_the_forward_button(browser):
    page = ImagesPage(browser, images_link)
    page.open()
    page.should_be_change_the_picture()

def test_return_to_the_previous_picture_by_pressing_the_back_button(browser):
    page = ImagesPage(browser, images_link)
    page.open()
    page.should_be_return_picture()