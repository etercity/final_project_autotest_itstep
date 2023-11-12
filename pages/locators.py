from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    LOGOUT = (By.XPATH, "//div[@class='top_bar_user']//a[@href = 'user/logout']")
    DETAILS = (By.XPATH, "//a[text() = 'Детали сотрудничества']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
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
    SUBCATEGORY_SAMSUNG_HEADER = (By.XPATH, "//div[@class = 'items-wrap']/ul/li[6]//li[55]")

    SUBSCRIBE = (By.XPATH, "//button[text() = 'Подписаться!']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@name = 'submail']")
    LOGO_FOOTER = (By.XPATH, "//img[@src = 'images/logo-footer.png']")
    ALERT_SUCCESS = (By.XPATH, "//div[@id = 'alert-success']")
    ALERT_ERROR = (By.XPATH, "//div[@id = 'alert-error']")


class MainPageLocators:
    SCREEN_SLIDER = (By.XPATH, "//div[@class = 'screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href = 'category/zaryadki']")
    SUB_CAT_POWER_BANK = (By.XPATH, "//ul[@class = 'cat_menu']/li[5]/ul/li[6]")

    INFO_BLOCK_VOZVRAT_SREDSTV = (By.XPATH, "//div[@class = 'characteristics']//div[@class = 'row']/div[1]/div")
    INFO_BLOCK_DOSTAVKA = (By.XPATH, "//div[@class = 'characteristics']//div[@class = 'row']/div[2]/div")
    INFO_BLOCK_OTSROCHKA = (By.XPATH, "//div[@class = 'characteristics']//div[@class = 'row']/div[3]/div")
    INFO_BLOCK_SUPPORT = (By.XPATH, "//div[@class = 'characteristics']//div[@class = 'row']/div[4]/div")
    BUTTON_SHOW_NEW_PRODUCTS = (By.XPATH, "//div[@class = 'new_arrivals_title clearfix']//a[@href = 'main/showNew']")
    BUTTON_PREV_NEW_PRODUCTS = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'arrivals_nav arrivals_prev']")
    BUTTON_NEXT_NEW_PRODUCTS = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'arrivals_nav arrivals_next']")
    SECTION_NEW_PRODUCTS = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']")
    NEW_PRODUCT_8 = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[3]/div[2]")
    BUTTON_SHOW_HITS = (By.XPATH, "//div[@class = 'best_sellers']//a[@href = 'main/showHit']")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'best_prev best_nav']/i")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'best_next best_nav']/i")
    SECTION_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'bestsellers_panel panel active']")
    BUTTON_PREV_TREND = (By.XPATH, "//div[@class = 'trends']//div[@class = 'trends_prev trends_nav slick-arrow']/i")
    BUTTON_NEXT_TREND = (By.XPATH, "//div[@class = 'trends']//div[@class = 'trends_next trends_nav slick-arrow']/i")


class SignupLoginPageLocators:
    GO_TO_SIGNUP = (By.XPATH, "//a[@href = 'user/signup']")
    H1_SIGNUP = (By.XPATH, "//h1[text() = 'Регистрация']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    BUTTON_SIGNUP = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    H1_VHOD = (By.XPATH, "//h1[text() = 'Вход']")
    BUTTON_LOGIN = (By.XPATH, "//button[text() = 'Войти']")


class OrderPageLocators:
    FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]")
    BUTTON_ADD_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//button[text() = 'В корзину!']")
    PRICE_FIRST_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[1]/div[1]//div[@class = 'product_price']")
    BTN_CONTINUE_SHOP_POPUP = (By.XPATH, "//button[text() = 'Продолжить покупки']")
    SECOND_PRODUCT_INPUT_NUMBER_QTY = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//input[@type = 'number']")
    PRICE_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//div[@class = 'product_price']")
    BUTTON_ADD_SECOND_PRODUCT = (By.XPATH, "//div[@class = 'shop_content']//div[@id = 'product']/div[1]//button")
    TOTAL_PRICE = (By.XPATH, "//tr[@class = 'cart-cena']/td[2]")
    QTY = (By.XPATH, "//tr[@class = 'cart-itogo']/td[2]")
    CHECKOUT_BTN_POPUP = (By.XPATH, "//a[@href = 'cart/view']")
    CART_REG_FORM = (By.XPATH, "//div[@class = 'cart-reg']")
    INPUT_EMAIL = (By.XPATH, "//input[@name = 'email']")
    INPUT_PASSWORD = (By.XPATH, "//input[@name = 'password']")
    INPUT_NOTE = (By.XPATH, "//textarea[@name= 'note']")
    CHECKOUT_BUTTON = (By.XPATH, "//button[@class = 'btn green']")


class CabinetPageLocators:
    pass


class CategoryPageLocators:
    pass


class SearchPageLocators:
    pass

