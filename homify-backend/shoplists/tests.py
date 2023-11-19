from django.test import TestCase

class ShoplistCreateTestCase(TestCase):
    def setUp(self):
        self.request = {
            "user":1,
            "user_group":1,
            "products":{
                "name":"milk",
                "quantity":1
            },
            "assigned_user":2
        }
        
        self.responses = {
            "success" : (201, "Shoplist created successfully")
        }
        
    def test_create_shoplist_success(self):
        #call api with self.request
        #validate status code against self.responses['success']
        #validate shoplist creation
        assert True
        
class EventListTestCase(TestCase):
    def setUp(self):
        self.reqeust = {
            "user_group":1,
            "start":"2023-12-01 17:00:00",
            "end":"2023-12-01 22:30:00",
        }
        
        self.responses = {
            "success" : (200, [
                # list of shoplist instances
            ])
        }
        
    def test_list_events_success(self):
        #call api with query params
        #validate status code agains self.responses['success']
        #validate shoplist list against self.responses['success']
        assert True
        