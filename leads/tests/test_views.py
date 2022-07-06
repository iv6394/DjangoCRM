import re
from django.http import response
from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
    """"
    TEST FOR LANDING PAGE
    """
    def test_get(self):
        
        """"
        check if:
        1) the response is ok and equal to 200
        2) we correctly use the tamplate for landing page
        """
        response = self.client.get(reverse("landing-page"))
        self.assertEqual(response.status_code,200) 
        self.assertTemplateUsed(response, "landing_page.html")
