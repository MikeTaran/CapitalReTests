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
    MENU_PRODUCT_PROFESSIONAL_TRADERS = (By.CSS_SELECTOR, '')
    MENU_PRODUCT_DISCOVER_PRO_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id581"]')
    MENU_PRODUCT_CORPORATE_ACCOUNTS = (By.CSS_SELECTOR, 'a[data-type="nav_id485"]')
    MENU_PRODUCT_TRADE_WITH_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id534"]')
    MENU_PRODUCT_CHARGES_FEES = (By.CSS_SELECTOR, 'a[data-type="nav_id93"]')
    MENU_PRODUCT_CAPITAL_VS_COMPETITOR = (By.CSS_SELECTOR, 'a[data-type="nav_id240"]')
    MENU_PRODUCT_WHY_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id592"]')
    MENU_PRODUCT_DESKTOP_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id77"]')
    # NAVBAR EDUCATION
    MENU_EDUCATION = (By.CSS_SELECTOR, 'a[data-type="nav_id96"]')
    # EDUCATION / LEARNING HUB
    MENU_EDUCATION_LEARNING_HUB = (By.CSS_SELECTOR, 'a[data-type="nav_id95"]')
    MENU_EDUCATION_BASICS_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id174"]')
    MENU_EDUCATION_TRADING_COURSES = (By.CSS_SELECTOR, 'a[data-type="nav_id11"]')
    MENU_EDUCATION_CFD_TRADING_GUIDE = (By.CSS_SELECTOR, 'a[data-type="nav_id58"]')
    MENU_EDUCATION_GLOSSARY_TRADING_ITEMS = (By.CSS_SELECTOR, 'a[data-type="nav_id12"]')
    MENU_EDUCATION_INVESTMATE_APP = (By.CSS_SELECTOR, 'a[data-type="nav_id78"]')
    # EDUCATION / MARKET GUIDES
    MENU_EDUCATION_SHARE_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id105"]')
    MENU_EDUCATION_COMMODITIES_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id106"]')
    MENU_EDUCATION_FOREX_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id108"]')
    MENU_EDUCATION_CRYPTOCURRENCY_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id109"]')
    MENU_EDUCATION_INDICES_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id110"]')
    MENU_EDUCATION_ETF_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id243"]')
    # EDUCATION / TRADING STRATEGIES GUIDE
    MENU_EDUCATION_TRADING_STRATEGIES_GUIDE = (By.CSS_SELECTOR, '')
    MENU_EDUCATION_DAY_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id526"]')
    MENU_EDUCATION_TEND_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id527"]')
    MENU_EDUCATION_POSITION_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id528"]')
    MENU_EDUCATION_SWING_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id529"]')
    MENU_EDUCATION_WHAT_IS_MARGIN = (By.CSS_SELECTOR, 'a[data-type="nav_id331"]')
    MENU_EDUCATION_TRADING_PSYCHOLOGY_GUIDE = (By.CSS_SELECTOR, 'a[data-type="nav_id219"]')
    # MARKETS
    MENU_MARKETS = (By.CSS_SELECTOR, 'a[data-type="nav_id3"]')
    # MARKETS / ALL MARKETS
    MENU_MARKETS_ALL_MARKETS = (By.CSS_SELECTOR, 'a[data-type="nav_id31"]')
    MENU_MARKETS_FOREX = (By.CSS_SELECTOR, 'a[data-type="nav_id57"]')
    MENU_MARKETS_INDICES = (By.CSS_SELECTOR, 'a[data-type="nav_id8"]')
    MENU_MARKETS_COMMODITIES = (By.CSS_SELECTOR, 'a[data-type="nav_id4"]')
    MENU_MARKETS_SHARES = (By.CSS_SELECTOR, 'a[data-type="nav_id9"]')
    MENU_MARKETS_CRYPTOCURRENCIES = (By.CSS_SELECTOR, 'a[data-type="nav_id65"]')
    MENU_MARKETS_ESG = (By.CSS_SELECTOR, 'a[data-type="nav_id461"]')
    # MARKETS / MARKET TOOLS
    MENU_MARKETS_MARKET_TOOLS = (By.CSS_SELECTOR, 'a[data-type="nav_id561"]')
    MENU_MARKETS_CFD_CALCULATOR = (By.CSS_SELECTOR, 'a[data-type="nav_id562"]')
    MENU_MARKETS_ESG_TRADING = (By.CSS_SELECTOR, 'a[data-type="nav_id563"]')
    MENU_MARKETS_ECONOMIC_CALENDAR = (By.CSS_SELECTOR, 'a[data-type="nav_id564"]')
    # NEWS AND ANALYSIS
    MENU_NEWS_ANALYSIS = (By.CSS_SELECTOR, 'a[data-type="nav_id10"]')
    # ALL NEWS
    MENU_NEWS_ALL_NEWS = (By.CSS_SELECTOR, 'a[data-type="nav_id33"]')
    MENU_NEWS_ANALYSIS_STOCKS = (By.CSS_SELECTOR, 'a[data-type="nav_id43"]')
    MENU_NEWS_ANALYSIS_COMMODITIES = (By.CSS_SELECTOR, 'a[data-type="nav_id44"]')
    MENU_NEWS_ANALYSIS_INDICES = (By.CSS_SELECTOR, 'a[data-type="nav_id480"]')
    MENU_NEWS_ANALYSIS_CRYPTOCURRENCIES = (By.CSS_SELECTOR, 'a[data-type="nav_id35"]')
    MENU_NEWS_ANALYSIS_FOREX = (By.CSS_SELECTOR, 'a[data-type="nav_id343"]')
    MENU_NEWS_ANALYSIS_ECONOMICS = (By.CSS_SELECTOR, 'a[data-type="nav_id45"]')
    MENU_NEWS_ANALYSIS_VIDEO = (By.CSS_SELECTOR, 'a[data-type="nav_id479"]')
    MENU_NEWS_ANALYSIS_DATA_JOURNALISM = (By.CSS_SELECTOR, 'a[data-type="nav_id379"]')
    MENU_NEWS_ANALYSIS_TRADINGVIEW = (By.CSS_SELECTOR, 'a[data-type="nav_id449"]')
    # MARKET UPDATES
    MENU_NEWS_ANALYSIS_MARKET_UPDATES = (By.CSS_SELECTOR, 'a[data-type="nav_id335"]')
    MENU_NEWS_ANALYSIS_ECONOMIC_CALENDAR = (By.CSS_SELECTOR, 'a[data-type="nav_id97"]')
    # navbar More
    MENU_MORE = (By.CSS_SELECTOR, 'a[data-type="nav_id16"]')
    # ABOUT CAPITAL
    MENU_MORE_ABOUT_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id56"]')
    MENU_MORE_OUR_STORY = (By.CSS_SELECTOR, 'a[data-type="nav_id459"]')
    MENU_MORE_WHITEPAPER = (By.CSS_SELECTOR, 'a[data-type="nav_id156"]')
    MENU_MORE_LEADERSHIP_TEAM = (By.CSS_SELECTOR, 'a[data-type="nav_id590"]')
    MENU_MORE_OUR_GLOBAL_OFFICE = (By.CSS_SELECTOR, 'a[data-type="nav_id173"]')
    MENU_MORE_COMPLAINCE_LEGALS = (By.CSS_SELECTOR, 'a[data-type="nav_id17"]')
    MENU_MORE_CAREERS_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id593"]')
    MENU_MORE_MEDIA_CENTRE = (By.CSS_SELECTOR, 'a[data-type="nav_id361"]')
    MENU_MORE_ANTI_MONEY_LAUNDERING = (By.CSS_SELECTOR, 'a[data-type="nav_id589"]')
    # HELP & SUPPORT
    MENU_MORE_HELP_SUPPORT = (By.CSS_SELECTOR, 'a[data-type="nav_id18"]')
    MENU_MORE_SUPPORT = (By.CSS_SELECTOR, 'a[data-type="nav_id535"]')
    MENU_MORE_CAPITAL_SYSTEM_STATUS = (By.CSS_SELECTOR, 'a[data-type="nav_id311"]')
    MENU_MORE_COMPLAINS = (By.CSS_SELECTOR, 'a[data-type="nav_id523"]')
    # PARTNER WITH US
    MENU_MORE_PARTNER_WITH_US = (By.CSS_SELECTOR, '')
    MENU_MORE_PARTNERSHIP_PROGRAMME = (By.CSS_SELECTOR, 'a[data-type="nav_id323"]')

    MENU_PROF_ACCOUNT = (By.CSS_SELECTOR, 'a[data-type="nav_id89"]')
    MENU_WHY_CAPITAL = (By.CSS_SELECTOR, 'a[data-type="nav_id115"]')


    # 220_loc
    EXPLORE_PLATFORM_TEXT = (By.CSS_SELECTOR, "ul[class='listChecked brickSm hideXs']>li:nth-last-child(1)>strong")

    #TRADE_INSTRUMENT_LIST = (By.XPATH, "//a[normalize-space()='US Wall Street 30']")
    TRADE_INSTRUMENT_LIST = (By.CSS_SELECTOR, '.js-wMarkets__displayTitle')
