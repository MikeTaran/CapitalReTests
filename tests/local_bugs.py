import allure
import pytest

from pages.main_page import MainPage
from pages.more_page import MorePage
from pages.product_page import ProductPage

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

languages = ['en', 'ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn']
base_url = 'https://capital.com/'


@allure.suite('Test Re-test Local bugs')
class TestLocalBugs:
    data = []

    @allure.feature('218_local: Placeholder "Search" of search field is not translated, when selected languages '
                    'any except EN, DE, IT, CN, PL')
    @pytest.mark.parametrize('lang', languages)
    @pytest.mark.parametrize('lic', ['United Kingdom'])
    @pytest.mark.xfail
    def test_218_loc(self, driver, lang, lic):
        data_lang = TestLocalBugs.data
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = MorePage(driver, base_url)
        placeholder = page.check_search_field()
        if lang not in ['en']:
            if placeholder == 'Search':
                data_lang.append(lang)
            if lang == 'cn':
                with allure.step(f'\nNo localization for next lang:  {data_lang}'):
                    print(f'\nNo localization for next lang:  {data_lang}')
            assert placeholder != 'Search', f'{lang}: {placeholder}'

    @allure.feature('220_loc: Phrase "Trade on market swings with CFDs and Spread Betting" '
                    'is displayed English on main page in the block "Explore our platform"')
    @pytest.mark.parametrize('lang', ['de', 'ar', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn'])
    @pytest.mark.parametrize('lic', ['United Kingdom'])
    @pytest.mark.xfail
    def test_220_loc(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        explore_text = page.check_explore_platform_text()
        with allure.step(f'{lang}: {explore_text}'):
            assert 'Trade on market' not in explore_text, f'{lang}: {explore_text}'

    @allure.feature('221_loc: Block title "Comment pouvons-nous vous aider?" (How can we help?) isnt fit to the block '
                    'in the menu item [Centre d adide et de support] (Support center), when FR language selected" ')
    @pytest.mark.parametrize('lang', languages)
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_221_loc(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = MorePage(driver, base_url)
        len_of_text = page.check_help_block()
        assert len_of_text < 25, f'Length of the local text is {len_of_text} symbols and more than fit in div'

    @allure.feature('223_loc: Text in the block "Award-winning platform" in menu item [Desktop trading] are '
                    'not translated , when  selected language is EL, ES, NL, RU')
    @pytest.mark.parametrize('lang', languages)
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_223_loc(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = ProductPage(driver, base_url)
        text = page.check_block_award()
        assert 'Best Online Trading' not in text, f'{lic}: {lang} - not translate'

    @allure.feature('226_loc: не воспроизводится. Нет пункта меню')
    def test_226_loc(self):
        pass  # не воспроизводится

    @allure.feature('227_loc: Text "Discover our mobile apps " are not translated from EN on BG, CS, DA, ET, EL, ES, '
                    'FR, HR, IT, LV, LT, HU, NL, SL, SK, FI, SV, ZH in the block "Industry-leading features for an '
                    'industry-leading platform" in the menu item [Why Capital.com?]')
    @pytest.mark.parametrize('lang',
                             ['ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn'])
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_227_loc(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = ProductPage(driver, base_url)
        text = page.check_industry_leading_block()
        assert 'Discover our mobile apps' not in text, f'{lic}: {lang} - not translate'

    @allure.feature('228_loc: Text "Learn more about stop-loss orders " are not translated from EN on BG, CS, DA, ET,'
                    ' EL, ES, FR, HR, IT, LV, LT, HU, NL, SL, SK, FI, SV, TH, ZH in the block "Protect what you earn" '
                    'in the menu item [Why Capital.com?]')
    @pytest.mark.parametrize('lang',
                             ['ar', 'de', 'el', 'es', 'fr', 'it', 'hu', 'nl', 'pl', 'ro', 'ru', 'zh', 'cn'])
    @pytest.mark.parametrize('lic', ['local'])
    @pytest.mark.xfail
    def test_228_loc(self, driver, lang, lic):
        page = MainPage(driver, base_url)
        page.open_site_lang_lic(lang, lic)
        #
        page = ProductPage(driver, base_url)
        text = page.check_protect_earn_block()
        assert 'Learn more about' not in text, f'{lic}: {lang} - not translate'
