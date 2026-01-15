"""
Test calc
"""
from django.test import SimpleTestCase
from app.calc import add

class CalcTest(SimpleTestCase):
    def test_add(self):
        sum= add(5,6)
        
        self.assertEqual(sum, 11)


