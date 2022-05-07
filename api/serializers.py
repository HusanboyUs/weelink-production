from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from base.models import Profile,ProfileLink


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields='__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProfileLink
        fields='__all__'

