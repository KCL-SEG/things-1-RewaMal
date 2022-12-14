from django.core.exceptions import ValidationError
from django.test import TestCase
from things.models import Thing

# Create your tests here.
class ThingsModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing(
            name= 'rug',
            description= 'circle yallow rug',
            quantity='9',             
        )

    def test_name_must_be_unique(self):
        second_thing = self._create_second_thing() 
        self.thing.name = second_thing.name
        self._assert_thing_is_invalid()
    
    def test_description_need_not_to_be_unique(self):
        second_thing =self._create_second_thing()
        self.description = second_thing.description
        self._assert_thing_is_valid()

    def test_quantity_must_not_be_unique(self):
        second_thing = self._create_second_thing() 
        self.quantity = second_thing.quantity
        self._assert_thing_is_valid()

    def _assert_thing_is_valid(self):
        try:
            self.thing.full_clean()
        except(ValidationError):
            self.fail("Thing should be valid")

    def _assert_thing_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.thing.full_clean()

    def _create_second_thing(self):
        thing = Thing(
            name= 'jamal',
            description= 'jamal statue',
            quantity='3',  
        )
        return thing