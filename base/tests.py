from django.test import TestCase,Client
from django.urls import reverse
from .models import Profile

class TestViews(TestCase):
    def setUp(self):
        self.client=Client()
        self.detail_url=reverse('profileView')
        self.profiles=Profile.objects.all()


    def test_profiles(self):
        
        self.assertNotEqual(self.profiles.count(), 0)    

