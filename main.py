import data
import helpers
import pages
from selenium import webdriver
import time
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_urban_routes(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_supportive_plan()

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_phone_number_button()
        routes_page.set_phone_number_field(data.PHONE_NUMBER)
        code = helpers.retrieve_phone_code(self.driver)
        routes_page.set_sms_field(code)
        assert routes_page.get_phone_number_field() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_payment_method()
        routes_page.click_add_card_button()
        routes_page.set_card_number_field(data.CARD_NUMBER)
        routes_page.set_card_code_field(data.CARD_CODE)
        time.sleep(2)
        routes_page.click_link_button()

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.set_message_for_driver(data.MESSAGE_FOR_DRIVER)


    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_supportive_plan()
        routes_page.click_blanket_checkbox()


    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_supportive_plan()
        routes_page.click_ice_cream_plus()
        routes_page.click_ice_cream_plus()

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = pages.UrbanRoutesPage(self.driver)
        routes_page.set_from_address(data.ADDRESS_FROM)
        routes_page.set_to_address(data.ADDRESS_TO)
        routes_page.click_call_taxi_button()
        time.sleep(2)
        routes_page.click_supportive_plan()
        routes_page.click_enter_number_order_button()


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()