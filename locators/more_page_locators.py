from selenium.webdriver.common.by import By


class MorePageLocators:
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input[id="query"]')
    SUPPORT_BANNER_TEXT = (By.CSS_SELECTOR, 'div[class="supp-center__container"]>span')

