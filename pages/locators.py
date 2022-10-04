from selenium.webdriver.common.by import By

class MainPageLocators():
    IFRAME_LINK = (By.CSS_SELECTOR, "[class='dzen-search-arrow-common__frame']")
    SEARCH_FIELD_IN_IFRAME = (By.CSS_SELECTOR, "[class='arrow__input mini-suggest__input']")
    SUGGEST_TABLE_IN_IFRAME = (By.CSS_SELECTOR, "[class='mini-suggest__popup-content']")
    SEARCH_TABLE = (By.CSS_SELECTOR, "[class='main__content']")
    FIRST_SNIPPET = (By.XPATH, "//li[@data-first-snippet]")
    HREF_TENSOR = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    IMAGE_LINK = (By.XPATH, "//span[contains(@class, 'images')]")

class ImagesPageLocators():
    IMAGE_FIRST_CATEGORY = (By.XPATH, "//div[contains(@class, 'PopularRequestList-Item_pos_0')]")
    SEARCH_FIELD = (By.CSS_SELECTOR, "[class='input__control mini-suggest__input']")
    FIRST_IMAGE = (By.XPATH, "//div[contains(@class, 'item_pos_0')]")
    OPEN_PICTURE = (By.CSS_SELECTOR, ".MMImage-Origin")
    BUTTON_NEXT = (By.XPATH, "//div[contains(@class, 'ButtonNext')]")
    BUTTON_BACK = (By.XPATH, "//div[contains(@class, 'ButtonPrev')]")