from selenium.webdriver.common.by import By


class ProductPageLocators:
    AWARD_WINNING_PLATFORM = (By.CSS_SELECTOR, 'div[class="prime__list prime__list--platform"]>div')
    INDUSTRY_LEADING_BOX = (By.CSS_SELECTOR, 'div.accordionCheckbox__content.sectionAccordion__box--bgDark')
    PROTECT_EARN_BOX = (By.CSS_SELECTOR, "div[class='accordionCheckbox__content sectionAccordion__box "
                                             "sectionAccordion__box--bgDark'] a[class='arrowLink']")
