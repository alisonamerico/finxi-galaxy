from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from droid.api.models import Anunciante, DemandaDePecas
from droid.api.serializers import AnuncianteSerializer, DemandaDePecaSerializer


class AnuncianteViewSet(viewsets.ModelViewSet):

    """
    TouristSpotViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = Anunciante.objects.all()
    serializer_class = AnuncianteSerializer
    permission_classes = (IsAuthenticated,)
    search_fields = ['name']


class DemandaDePecasViewSet(viewsets.ModelViewSet):

    """
    FavoriteViewSet:
        - Performs queries of objects in the database;
        - Implements search fields and sort filters;
        - Authentication and permission for API access.
    """

    queryset = DemandaDePecas.objects.all()
    serializer_class = DemandaDePecaSerializer
    permission_classes = (IsAuthenticated,)
