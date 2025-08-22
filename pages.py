from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code
from selenium.webdriver.common.by import By






class UrbanRoutesPage:
    FROM_Locator = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    # Call taxi and plan selection locators
    CALL_TAXI_BUTTON = (By.XPATH, "//button[text()='Call a taxi']")
    SUPPORTIVE_PLAN = (By.XPATH, "//img[@alt='Supportive']")
    ACTIVE_PLAN = (By.CSS_SELECTOR, ".tcard.active .tcard-title")

    # Phone number locators
    PHONE_NUMBER_FIELD = (By.ID, "phone")
    PHONE_NUMBER_BUTTON = (By.XPATH, "//div[@class='np-text']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    SMS_FIELD = (By.ID, "code")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Confirm']")
    # Payment method locators
    PAYMENT_METHOD = (By.XPATH, "//div[@class='pp-text']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    CARD_NUMBER_FIELD = (By.ID, "number")
    CARD_CODE_FIELD = (By.XPATH, "//div[@class='card-code-input']//input")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    # Driver message locator
    MESSAGE_FOR_DRIVER = (By.ID, "comment")
    # Blanket and handkerchiefs locators
    BLANKET_CHECKBOX = (By.XPATH, "//div[@class='r-sw']//div[@class='switch']")
    BLANKET_VERIFY = (By.XPATH, "//div[@class='r-sw']//input[@class='switch-input']")
    # Ice cream locators
    ICE_CREAM_PLUS = (By.XPATH, "//div[@class='counter-plus' and text()='+']")
    ICE_CREAM_COUNTER = (By.CLASS_NAME, 'counter-value')
    # Order taxi locators
    ORDER_TAXI_BUTTON = (By.XPATH, "//button[text()='Order']")
    CAR_SEARCH_MODAL = (By.XPATH, "//div[text()='Car search']")
    ENTER_NUMBER_ORDER_BUTTON = (By.XPATH, "//button[@class='smart-button']/span[text()='Enter the number and order']")
    ORDER_REQUIREMENTS_BUTTON = (By.XPATH, "//div[@class='reqs-head' and text()='Order requirements']")

    def __init__(self, driver):
        self.driver = driver

    def set_from_address(self, from_address):
        self.driver.find_element(*self.FROM_Locator).send_keys(from_address)

    def set_to_address(self, to_address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_Locator).get_property('value')

    def get_to_address(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def click_supportive_plan(self):
        if self.get_active_plan()!='Supportive':
            self.driver.find_element(*self.SUPPORTIVE_PLAN).click()
        else:
            print('Supportive was already selected')

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_TAXI_BUTTON).click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).click()

    def set_phone_number_field(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(phone_number)
        self.driver.find_element(*self.PHONE_NUMBER_FIELD).send_keys(Keys.RETURN)

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def click_add_card_button(self):
        self.driver.find_element(*self.ADD_CARD_BUTTON).click()

    def set_card_number_field(self, card_number_field):
        self.driver.find_element(*self.CARD_NUMBER_FIELD).send_keys(card_number_field)

    def set_card_code_field(self, card_code_field):
        self.driver.find_element(*self.CARD_CODE_FIELD).send_keys(card_code_field)

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON).click()

    def set_message_for_driver(self, message):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message)

    def click_blanket_checkbox(self):
        self.driver.find_element(*self.BLANKET_CHECKBOX).click()

    def click_enter_number_order_button(self):
        self.driver.find_element(*self.ENTER_NUMBER_ORDER_BUTTON).click()

    def get_enter_number_order_button(self):
        return self.driver.find_element(*self.ENTER_NUMBER_ORDER_BUTTON).text

    def click_ice_cream_plus(self):
        self.driver.find_element(*self.ICE_CREAM_PLUS).click()
        self.driver.find_element(*self.ICE_CREAM_PLUS).click()

    def get_ice_cream_counter(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNTER).text)

    def click_order_requirements_button(self):
        self.driver.find_element(*self.ORDER_REQUIREMENTS_BUTTON).click()

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def set_sms_field(self,code):
        self.driver.find_element(*self.SMS_FIELD).send_keys(code)
        self.driver.find_element(*self.SMS_FIELD).send_keys(Keys.RETURN)

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def get_phone_number_field(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BUTTON).text

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER).get_property('value')

    def get_card_number_field(self):
        return self.driver.find_element(*self.CARD_NUMBER_FIELD).get_property('value')

    def get_card_code_field(self):
        return self.driver.find_element(*self.CARD_CODE_FIELD).get_property('value')

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN).text

    def get_car_search_visibility(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).is_displayed()

    def get_blanket_status(self):
        return self.driver.find_element(*self.BLANKET_VERIFY).get_property('checked')


