import time

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

all_languages = {'en': 'English', 'ar': 'العَرَبِيَّة', 'de': 'Deutsch', 'el': 'ελληνικά', 'es': 'Español',
                 'fr': 'Français',
                 'it': 'Italiano', 'hu': 'Magyar', 'nl': 'Nederlands',
                 'pl': 'Polski', 'ro': 'Română', 'ru': 'Русский', 'zh': '简体中文', 'cn': '繁體中文',
                 }


# lang = ['en', 'ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn']


class MainPage(BasePage):
    locators = MainPageLocators()

    def select_site_language(self, lang_new):
        lang_new = all_languages[lang_new]
        lang_menu = self.element_is_visible(self.locators.LANG_MENU)
        self.action_move_to_element(lang_menu)
        lang_list = self.elements_are_present(self.locators.LANG_LIST)
        for lng in lang_list:
            lang_index = lng.text
            if lang_new == lang_index:
                lng.click()
                break

    def select_site_license(self, lic):
        if lic != 'local':
            lang_menu = self.element_is_visible(self.locators.LANG_MENU)
            self.action_move_to_element(lang_menu)
            self.element_is_present(self.locators.COUNTRY_MENU).click()
            lic_list = self.elements_are_present(self.locators.LIC_LIST)
            for lic_i in lic_list:
                if lic_i.text == lic:
                    lic_i.click()
                    break

    def open_site_lang_lic(self, lang, lic):
        self.open()
        self.select_site_language(lang)
        self.select_site_license(lic)

    def check_explore_platform_text(self):
        explore_text = self.element_is_visible(self.locators.EXPLORE_PLATFORM_TEXT).text
        return explore_text

    def check_main_menu(self):
        self.main_menu_navigation(self.locators.MENU_EDUCATION, self.locators.MENU_EDUCATION_CFD_TRADING_GUIDE)

