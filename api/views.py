
from rest_framework import generics
from base.models import Profile
from .serializers import ProfileSerializer



class ProfileListView(generics.ListAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

profiles_list=ProfileListView.as_view()


class PorifleDetailView(generics.RetrieveAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

profile_detail=PorifleDetailView.as_view()

