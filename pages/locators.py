from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTERED_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTERED_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTERED_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON =(By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    NAME_OF_BOOK = (By.CSS_SELECTOR,"#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    NAME_OF_BOUGHT_BOOK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    TEXT_OF_SUCCESS_BUING = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    CURRENT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    FINAL_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    TEXT_OF_FINAL_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,"#messages > div:nth-child(1) > div")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")