import time
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import ImagesPageLocators

class ImagesPage(BasePage):

    def should_be_category_name_in_the_search_field(self):
        image_first_category = self.browser.find_element(*ImagesPageLocators.IMAGE_FIRST_CATEGORY)
        name_category = image_first_category.get_attribute("data-grid-text")
        image_first_category.click()
        time.sleep(2)  # Просто, чтобы успеть визуально увидеть обновление страницы после клика.

        assert EC.text_to_be_present_in_element(ImagesPageLocators.SEARCH_FIELD, name_category), \
            "The category name is not displayed in the search field"

    def should_be_the_picture_is_open(self):
        image_first_category = self.browser.find_element(*ImagesPageLocators.IMAGE_FIRST_CATEGORY)
        image_first_category.click()
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()
        time.sleep(2)  # Просто, чтобы успеть визуально увидеть открытие картинки.

        assert self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE), "The picture did not open"

    def should_be_change_the_picture(self):
        image_first_category = self.browser.find_element(*ImagesPageLocators.IMAGE_FIRST_CATEGORY)
        image_first_category.click()
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()
        open_first_image = self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE)
        first_image_url = open_first_image.get_attribute("src")
        button_next = self.browser.find_element(*ImagesPageLocators.BUTTON_NEXT)
        button_next.click()
        open_next_image = self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE)
        next_image_url = open_next_image.get_attribute("src")
        time.sleep(2)  # Просто, чтобы успеть визуально увидеть, что картинка переключилась.

        assert first_image_url != next_image_url, "The image has not changed after clicking on forward button"

    def should_be_return_picture(self):
        image_first_category = self.browser.find_element(*ImagesPageLocators.IMAGE_FIRST_CATEGORY)
        image_first_category.click()
        first_image = self.browser.find_element(*ImagesPageLocators.FIRST_IMAGE)
        first_image.click()
        open_first_image = self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE)
        first_image_url = open_first_image.get_attribute("src")
        button_next = self.browser.find_element(*ImagesPageLocators.BUTTON_NEXT)
        button_next.click()
        open_next_image = self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE)
        next_image_url = open_next_image.get_attribute("src")
        button_back = self.browser.find_element(*ImagesPageLocators.BUTTON_BACK)
        time.sleep(1) # Просто, чтобы успеть визуально увидеть, что картинка переключилась на следующую.
        button_back.click()
        open_current_picture_image = self.browser.find_element(*ImagesPageLocators.OPEN_PICTURE)
        current_picture_image_url = open_current_picture_image.get_attribute("src")
        time.sleep(2)  # Просто, чтобы успеть визуально увидеть, что картинка переключилась на предыдущую.

        assert (current_picture_image_url == first_image_url) & (current_picture_image_url != next_image_url), \
            "Pressing the back button did not return the previous picture"