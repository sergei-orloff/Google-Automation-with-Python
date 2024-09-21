"""
A test case example where the Python code simulates a cake factory and performs
different functions. These include choosing different sizes and flavors of a cake,
including small, medium, and large, and chocolate or vanilla.
In addition, the simple class allows developers to add sprinkles or cherries to the cake,
return a list of ingredients, and return the price of the cake based on size and toppings.

The test suite includes tests for the cake’s flavor, size, toppings, ingredients,
and price. Because unittest is class-based, encapsulate these statements into test methods.
The program calls the TextTestRunner() method, which returns a runner (TextTestResult).
"""
from typing import List
import unittest


class CakeFactory:
    def __init__(self, cake_type: str, size: str):
        self.cake_type = cake_type
        self.size = size
        self.toppings = []

        # Price based on cake type and size
        self.price = 10 if self.cake_type == "chocolate" else 8
        self.price += 2 if self.size == "medium" else 4 if self.size == "large" else 0

    def add_topping(self, topping: str):
        self.toppings.append(topping)
        # Adding 1 to the price for each topping
        self.price += 1

    def check_ingredients(self) -> List[str]:
        ingredients = ['flour', 'sugar', 'eggs']
        ingredients.append('cocoa') if self.cake_type == "chocolate" else ingredients.append('vanilla extract')
        ingredients += self.toppings
        return ingredients

    def check_price(self) -> float:
        return self.price


# Example of creating a cake and adding toppings
cake = CakeFactory("chocolate", "medium")
cake.add_topping("sprinkles")
cake.add_topping("cherries")
cake_ingredients = cake.check_ingredients()
cake_price = cake.check_price()

print(f"Ingredients: {cake_ingredients}, Price: ${cake_price}")
print("===" * 20)


# ==============================================================


class TestCakeFactory(unittest.TestCase):
    def test_create_cake(self):
        cake = CakeFactory("vanilla", "small")
        self.assertEqual(cake.cake_type, "vanilla")
        self.assertEqual(cake.size, "small")
        self.assertEqual(cake.price, 8)  # Vanilla cake, small size

    def test_add_topping(self):
        cake = CakeFactory("chocolate", "large")
        cake.add_topping("sprinkles")
        self.assertIn("sprinkles", cake.toppings)

    def test_check_ingredients(self):
        cake = CakeFactory("chocolate", "medium")
        cake.add_topping("cherries")
        ingredients = cake.check_ingredients()
        self.assertIn("cocoa", ingredients)
        self.assertIn("cherries", ingredients)
        self.assertNotIn("vanilla extract", ingredients)

    def test_check_price(self):
        cake = CakeFactory("vanilla", "large")
        cake.add_topping("sprinkles")
        cake.add_topping("cherries")
        price = cake.check_price()
        self.assertEqual(price, 14)  # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))
