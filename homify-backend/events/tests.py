from django.test import TestCase

class EventCreateTestCase(TestCase):
    def setUp(self):
        self.request = {
            "user":1,
            "user_group":1,
            "title":"laundry Bazyli",
            "start":"2023-12-01 18:00:00",
            "end":"2023-12-01 19:30:00",
        }
        
        self.responses = {
            "success" : (201, "Event created successfully")
        }
        
    def test_create_event_success(self):
        #call api with self.request
        #validate status code against self.responses['success']
        #validate event creation
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
                # list of event instances
            ])
        }
        
    def test_list_events_success(self):
        #call api with query params
        #validate status code agains self.responses['success']
        #validate event list against self.responses['success']
        assert True
        