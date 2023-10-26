from locators.main_page_locators import MainPageLocators
from locators.markets_page_locators import MarketsPageLocators
from pages.base_page import BasePage


class MarketsPage(BasePage):
    locators_markets = MarketsPageLocators()
    locators_main = MainPageLocators()

    def check_trading_calculator_input(self):
        self.element_is_present(self.locators_main.TRADE_INSTRUMENT_LIST).click()
        trading_calculator_input = self.element_is_visible(self.locators_markets.TRADING_CALCULATOR_INPUT)
        pointer = trading_calculator_input.value_of_css_property('cursor')
        return pointer
