import unittest
from app import greeting

class TestGreeting(unittest.TestCase):
    def test_greeting(self):
        self.assertEqual(greeting("Michael", "programmer"), "Hello Michael, you are a coding master")
        self.assertEqual(greeting("Michael", "engineer"), "Hello Michael, you are a builder of things")
        self.assertEqual(greeting("Michael", "scientist"), "Hello Michael, you are a mad scientist")