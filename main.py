import data
import helpers
class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_urban_routes(self):
        # Add in S8
        print("Function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("Function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("Function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("Function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("Function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        number_of_ice_creams = 2
        for i in range(number_of_ice_creams):
            # Add in S8
            print(f"Ordering ice cream #{i + 1}")
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass
