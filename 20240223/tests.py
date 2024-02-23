import unittest

from app import Cat, Dog

class TestStuff(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Kitty", 4, 4, "tiger")

    def test_init(self):
        self.assertIsInstance(self.cat, Cat, "Wrong or no class")
        self.assertEqual(self.cat.name, "Kitty", "wrong Name")

    def test_comunicate(self):
        self.assertEqual(self.cat.communicate(), "Moew  - I can see the bottom of my foodbowl")

    def test_eat(self):
        self.assertEqual(self.cat.eats("dogfood"), "bark", "always good to know other languages")
        self.assertEqual(self.cat.eats("fishfood"), "swim", "will drown")
        self.assertEqual(self.cat.eats("sausage"), "happy smile", "yummy")

    #here you probably will mock the function hiddenfunc(), as we need it's result for the execution of eats()
    #but we want to be sure to have a result, we can work with
        self.assertEqual(self.cat.eats("hidden"), "do something fancy and something else", "nope, not hidden")

    def test_jump(self):
        self.assertIs(self.cat.can_jump(), "oppsy")
        self.assertEqual(self.cat.can_jump(), True, "oppsy")

    def test_dog_bark(self):
        #normally initialize a cass-object and test its function
        dog = Dog("name", 1, 4)
        self.assertEqual(dog.barking(), "wauwau")

        #as 'barking' is a staticmethod, we don't need to initialize it and just can call it right away
        self.assertEqual(Dog.barking(), "wauwau")
        self.ass

if __name__ == "__main__":
    unittest.main()