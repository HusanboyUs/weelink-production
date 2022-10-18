from lzma import _PathOrFile
from django.test import TestCase,Client
from django.urls import reverse
from .models import Profile

class TestViews(TestCase):
    

    def test_project_list_GET(self):
        client=Client()
        response=client.get(reverse('lists'))
        self=total_profiles=Profile.objects.all()
        
        self.assertEqual(response.status_code, 200)
        
