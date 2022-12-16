from dataclasses import field
from os import link
from pyexpat import model
from rest_framework import serializers
from base.models import Profile,ProfileLink



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'


class LinkSerializer(serializers.ModelSerializer):
    links=ProfileSerializer(read_only=True, many=True)
    class Meta:
        model=ProfileLink
        fields='__all__'

