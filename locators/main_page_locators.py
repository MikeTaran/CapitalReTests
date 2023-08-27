from selenium.webdriver.common.by import By


class MainPageLocators:
    LANG_MENU = (By.CSS_SELECTOR, 'div[class="licLangSw js-licLangSw"]')
    LANG_LIST = (By.CSS_SELECTOR, 'div[class="licLangSw__langs"]>a>span')
    COUNTRY_MENU = (By.CSS_SELECTOR, 'input[class="fieldDropdown__control fieldDropdown__control--hidden"]')
    INPUT_LIC = (By.CSS_SELECTOR, 'input[class*="js-countriesSearchInput"]')
    LIC_LIST = (By.CSS_SELECTOR, 'ul[class*="js-countriesList"]>li>a')
    # navbar ProductAndService
    MENU_PRODUCT = (By.CSS_SELECTOR, 'a[data-type="nav_id2"]')
    MENU_TRADING_PRODUCTS = (By.CSS_SELECTOR, 'a[data-type="nav_id33"]')
    MENU_PRODUCT_CFD_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id587"]')
    MENU_PRODUCT_DEMO_ACCOUNT = (By.CSS_SELECTOR, 'a[data-type="nav_id578"]')
    MENU_PRODUCT_PLATFORM_AND_SERVICE = (By.CSS_SELECTOR, 'a[data-type="nav_id53"]')
    MENU_PRODUCT_OUR_MOBILE_APPS = (By.CSS_SELECTOR, 'a[data-type="nav_id465"]')
    MENU_PRODUCT_CAPITAL_API = (By.CSS_SELECTOR, 'a[data-type="nav_id426"]')
    MENU_PRODUCT_TRADING_VIEW = (By.CSS_SELECTOR, 'a[data-type="nav_id197"]')
    MENU_PRODUCT_METATRADER4 = (By.CSS_SELECTOR, 'a[data-type="nav_id235"]')
    MENU_PRODUCT_PROFESSIONAL_TRADERS = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_DISCOVER_PRO_TRADING = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_CORPORATE_ACCOUNTS = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_TRADE_WITH_CAPITAL = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_CHARGES_FEES = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_CAPITAL_VS_COMPETITOR = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_WHY_CAPITAL = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_DESKTOP_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id77"]')
    # NAVBAR EDUCATION
    MENU_PRODUCT_ = (By.CSS_SELECTOR, 'a[]')
    MENU_PRODUCT_ = (By.CSS_SELECTOR, 'a[]')
    # navbar More
    MENU_MORE = (By.CSS_SELECTOR, 'a[data-type="nav_id16"]')
    MENU_HELP_SUPPORT = (By.CSS_SELECTOR, 'a[data-type="nav_id18"]')

    MENU_PROF_ACCOUNT = (By.CSS_SELECTOR, 'a[data-type="nav_id89"]')
    MENU_WHY_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id115"]')


    # 220_loc
    EXPLORE_PLATFORM_TEXT = (By.CSS_SELECTOR, "ul[class='listChecked brickSm hideXs']>li:nth-last-child(1)>strong")

    #TRADE_INSTRUMENT_LIST = (By.XPATH, "//a[normalize-space()='US Wall Street 30']")
    TRADE_INSTRUMENT_LIST = (By.CSS_SELECTOR, '.js-wMarkets__displayTitle')
