import time
from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    def should_be_search_field(self):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))

        assert self.is_element_present(*MainPageLocators.SEARCH_FIELD_IN_IFRAME), "The search field is missing on the page"

    def should_be_suggest(self, request):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_IN_IFRAME)
        search_field.send_keys(request)
        time.sleep(2) # Просто, чтобы успеть визуально увидеть таблицу подсказок.

        assert self.is_element_present(*MainPageLocators.SUGGEST_TABLE_IN_IFRAME), "The table with suggest did not appear"

    def should_be_search_results(self, request):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_IN_IFRAME)
        search_field.send_keys(request)
        search_field.send_keys(Keys.ENTER)
        windows_list = self.browser.window_handles
        self.browser.switch_to.window(windows_list[1])

        assert self.is_element_present(*MainPageLocators.SEARCH_TABLE), "The search table is missing on the page"

    def link_to_request(self, request):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_IN_IFRAME)
        search_field.send_keys(request)
        search_field.send_keys(Keys.ENTER)
        windows_list = self.browser.window_handles
        self.browser.switch_to.window(windows_list[1])
        first_snippet = self.browser.find_element(*MainPageLocators.FIRST_SNIPPET)
        href_locators = first_snippet.find_elements(*MainPageLocators.HREF_TENSOR)

        # Можно и так: assert href_locators[0].get_attribute("href") == "https://tensor.ru/"
        assert len(href_locators) != 0, "The first link does not lead to the site tensor.ru"

    def should_be_image_link(self):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_IN_IFRAME)
        search_field.click()
        time.sleep(2) # Просто, чтобы успеть визуально увидеть выпадающий бокс.

        assert self.is_element_present(*MainPageLocators.IMAGE_LINK), "The link to the pictures will be removed in suggest"

    def should_be_click_on_the_image_link(self):
        self.browser.switch_to.frame(self.browser.find_element(*MainPageLocators.IFRAME_LINK))
        search_field = self.browser.find_element(*MainPageLocators.SEARCH_FIELD_IN_IFRAME)
        search_field.click()
        image_link = self.browser.find_element(*MainPageLocators.IMAGE_LINK)
        image_link.click()
        windows_list = self.browser.window_handles
        self.browser.switch_to.window(windows_list[1])

        assert "https://yandex.ru/images/" in self.browser.current_url, "The open page did not match with https://yandex.ru/images/"