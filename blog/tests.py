from django.http import response
from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.

class HomePageTest(TestCase):

    def test_status_code(self):
        # self.client is similar to request package in Django  (can pass urls through GET, POST requests)
        response = self.client.get(reverse("blog-home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/home.html")

# typically should create a 'tests' folder in app and have __init__.py file that runs all tests
# would rename this file something like test_views.py

# and others like test_forms.py


# django will run tests in this directory structure just fine