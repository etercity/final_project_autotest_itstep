from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "Гарантия")
    PHONE = (By.XPATH, "//div[text()='+38 098 911 95 22']")
    CURRENCY = (By.XPATH, '//select[@id="currency"]')

    UAH = (By.XPATH, '//option[@class="custom_list clc"]')
    USD = (By.XPATH, '//option[@value="USD"]')
    EUR = (By.XPATH, '//option[@value="EUR"]')
    LOGO = (By.XPATH, '//img[@src="images/logo.png"]')
    SEARCH_INPUT = (By.XPATH, '//input[@id="typeahead"]')
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    WISH_BUTTON = (By.XPATH, '//a[@href="wish/show"]')
    CART_BUTTON = (By.XPATH, '//a[@href="cart/show"]')

    HITY = (By.XPATH, "//span[text()='Хиты']")
    SKIDKI = (By.XPATH, "//span[text()='Скидки']")
    NOVINKI = (By.XPATH, "//span[text()='Новинки']")
    HEAD_CAT_SAMSUNG = (By.XPATH, "//div[@class='search-by-level-1' and text()='Samsung']")

    SUBSCRIBE = (By.XPATH, "//button[text() = 'Подписаться!']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@name = 'submail']")
    LOGO_FOOTER = (By.XPATH, "//img[@src = 'images/logo-footer.png']")


class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class = 'screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href = 'category/zaryadki']")
    SUB_CAT_POWER_BANK = (By.XPATH, "//ul[@class = 'cat_menu']/li[5]/ul/li[6]")

