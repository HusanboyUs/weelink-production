from django.test import TestCase,Client
from django.urls import reverse
import json
from .models import Profile

class TestViews(TestCase):
    def test_project_list_GET(self):
        client=Client()
        response=client.get(reverse('lists'))
        self.assertEqual(response.status_code, 200)
        
