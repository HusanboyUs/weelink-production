from django.shortcuts import get_object_or_404
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

class UserView(APIView):
    def get(self,request,slug):
        profile=get_object_or_404(Profile, slug=slug)
        serializer=ProfileSerializer(profile)
        return Response(serializer.data)
            