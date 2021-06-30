from django.test import TestCase

class FirstTest(TestCase):
    def sumTwo(self):
        initialnum = 5
        self.assertEquals(initialnum,5)
        