from locators.main_page_locators import MainPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    locators_product = ProductPageLocators()
    locators_main = MainPageLocators()

    def check_block_award(self):
        menu_product = self.element_is_visible(self.locators_main.MENU_PRODUCT)
        self.action_move_to_element(menu_product)
        self.element_is_visible(self.locators_main.MENU_PRODUCT_DESKTOP_TRADING).click()
        award_winning = self.element_is_visible(self.locators_product.AWARD_WINNING_PLATFORM)
        award_winning_text = award_winning.text
        return award_winning_text

    def check_industry_leading_block(self):
        menu_product = self.element_is_visible(self.locators_main.MENU_PRODUCT)
        self.action_move_to_element(menu_product)
        self.element_is_visible(self.locators_main.MENU_WHY_CAPITAL).click()
        industry_block = self.element_is_visible(self.locators_product.INDUSTRY_LEADING_BOX)
        text = industry_block.text
        return text

    def check_protect_earn_block(self):
        menu_product = self.element_is_visible(self.locators_main.MENU_PRODUCT)
        self.action_move_to_element(menu_product)
        self.element_is_visible(self.locators_main.MENU_WHY_CAPITAL).click()
        protect_block = self.element_is_visible(self.locators_product.PROTECT_EARN_BOX)
        text = protect_block.text
        return text
