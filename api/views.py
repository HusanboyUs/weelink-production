from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer,LinkSerializer
from base.models import Profile,ProfileLink
from django.contrib.auth.decorators import login_required,permission_required



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
            
class linkView(apiView):
    def get(self, request):
        link=ProfileLink.objects.all()
        serializer=LinkSerializer(link, many=True)
        return Response(serializer.data)        