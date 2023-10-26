from locators.main_page_locators import MainPageLocators
from locators.more_page_locators import MorePageLocators
from pages.base_page import BasePage


class MorePage(BasePage):
    locators_more = MorePageLocators()
    locators_main = MainPageLocators()

    def check_search_field(self):
        menu_more = self.element_is_visible(self.locators_main.MENU_MORE)
        self.action_move_to_element(menu_more)
        menu_help_support = self.element_is_visible(self.locators_main.MENU_MORE_HELP_SUPPORT)
        menu_help_support.click()
        input_field = self.element_is_visible(self.locators_more.SEARCH_FIELD)
        placeholder = input_field.get_attribute('placeholder')
        return placeholder

    def check_help_block(self):
        menu_more = self.element_is_visible(self.locators_main.MENU_MORE)
        self.action_move_to_element(menu_more)
        menu_help_support = self.element_is_visible(self.locators_main.MENU_MORE_HELP_SUPPORT)
        menu_help_support.click()
        support_banner = self.element_is_present(self.locators_more.SUPPORT_BANNER_TEXT)
        len_of_text = len(support_banner.text)
        new_color = '#ff0081'
        self.driver.execute_script("arguments[0].style.backgroundColor = '{}';".format(new_color), support_banner)
        return len_of_text
