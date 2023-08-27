from selenium.webdriver.common.by import By


class MainPageLocators:
    LANG_MENU = (By.CSS_SELECTOR, 'div[class="licLangSw js-licLangSw"]')
    LANG_LIST = (By.CSS_SELECTOR, 'div[class="licLangSw__langs"]>a>span')
    COUNTRY_MENU = (By.CSS_SELECTOR, 'input[class="fieldDropdown__control fieldDropdown__control--hidden"]')
    INPUT_LIC = (By.CSS_SELECTOR, 'input[class*="js-countriesSearchInput"]')
    LIC_LIST = (By.CSS_SELECTOR, 'ul[class*="js-countriesList"]>li>a')
    # navbar More
    MENU_MORE = (By.CSS_SELECTOR, 'a[data-type="nav_id16"]')
    MENU_HELP_SUPPORT = (By.CSS_SELECTOR, 'a[data-type="nav_id18"]')
    MENU_PRODUCT = (By.CSS_SELECTOR, 'a[data-type="nav_id2"]')
    MENU_PRODUCT_DESKTOP = (By.CSS_SELECTOR, 'a[data-type="nav_id77"]')
    MENU_PROF_ACCOUNT = (By.CSS_SELECTOR, 'a[data-type="nav_id89"]')
    MENU_WHY_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id115"]')


    # 220_loc
    EXPLORE_PLATFORM_TEXT = (By.CSS_SELECTOR, "ul[class='listChecked brickSm hideXs']>li:nth-last-child(1)>strong")

    #TRADE_INSTRUMENT_LIST = (By.XPATH, "//a[normalize-space()='US Wall Street 30']")
    TRADE_INSTRUMENT_LIST = (By.CSS_SELECTOR, '.js-wMarkets__displayTitle')
