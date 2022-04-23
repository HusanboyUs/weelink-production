from django.shortcuts import render
from requests import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer
from base.models import Profile

class apiView(APIView):
    def get(self, request):
        profile=Profile.objects.all()
        serializer=ProfileSerializer(profile, many=True)
        return Response(serializer.data)