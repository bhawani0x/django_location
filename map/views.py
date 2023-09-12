from rest_framework import viewsets
from .models import BaseAddress
from .serializers import BaseAddressSerializer


class BaseAddressList(viewsets.ModelViewSet):
    queryset = BaseAddress.objects.all()
    serializer_class = BaseAddressSerializer


class BaseAddressDetail(viewsets.ModelViewSet):
    queryset = BaseAddress.objects.all()
    serializer_class = BaseAddressSerializer
