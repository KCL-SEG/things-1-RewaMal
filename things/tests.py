from django.core.exceptions import ValidationError
from django.test import TestCase
from things.models import Thing

# Create your tests here.
class ThingsModelTestCase(TestCase):

    def setUp(self):
        self.thing = Thing.objects.create_thing(
            name= 'rug',
            description= 'circle yallow rug',
            quantity='9',             
        )

    def test_name_must_be_uniqe(self):
        second_thing = self._create_second_thing() 
        self.name = second_thing.name
        self._assert_thing_is_invaild()

    def _assert_thing_is_vaild(self):
        try:
            self.Thing.full_clean()
        except(ValidationError):
            self.fail("Thing should be vaild")

    def _assert_thing_is_invaild(self):
        with self.assertRaises(ValidationError):
            self.Thing.full_clean()

    def _create_second_thing(self):
        thing = Thing.objects.create_thing(
            name= 'jamal',
            description= 'jamal statue',
            quantity='3',  
        )
        return thing