import time

import allure
import pytest

from pages.main_page import MainPage
from pages.markets_page import MarketsPage

# licenses = [
# "local" # native country
# "es",  # Spain - "CYSEC" - https://capital.com/?country=es
# "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
# "fr",  # France - "CYSEC" - https://capital.com/?country=fr
# "au",  # Australia - "ASIC" - https://capital.com/?country=au
# "hk",  # Hong Kong - "SCB" - https://capital.com/?country=hk
# "tw",  # Taiwan - "SCB"
# "pl",  # Poland - "CYSEC" - https://capital.com/?country=pl
# "de",  # Germany - "CYSEC" - https://capital.com/?country=de
# "tr",  # Turkey - "SCB" - https://capital.com/?country=tr
# ]
# lang = ['en', 'ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn']
base_url = 'https://capital.com/'


@allure.suite('Test Re-test Web bugs')
class TestWebBugs:
    @allure.feature('232_web: The mouse pointer is dispayed when hovering over the name of a trading instrument when '
                    'hovering over the name of a trading instrument in the trading calculator')
    @pytest.mark.parametrize('lang', ['en'])
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_232_web(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = MarketsPage(driver, base_url)
        pointer = page.check_trading_calculator_input()
        assert pointer != 'pointer', 'Cursor is as a pointer'

    @allure.feature('232_web:')
    @pytest.mark.parametrize('lang', ['en'])
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_web(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        page.check_main_menu()
