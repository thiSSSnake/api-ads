from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import AdsSerializer
from .models import Ads


class AdsListCreateView(generics.ListCreateAPIView):
    '''The view is used to get a list of all ads 
    from the database using a GET request, 
    or to add new data using a POST request.
    Only an authorized user can add data.'''

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class AdRetrieveView(generics.RetrieveAPIView):
    '''Getting ad data using the transmitted ad id'''
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    lookup_field = "pk"
