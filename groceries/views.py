from rest_framework import generics
from .models import GroceryItem
from .serializers import GroceryItemSerializer


class GroceryItemList(generics.ListCreateAPIView):
    queryset = GroceryItem.objects.order_by('created_at')
    serializer_class = GroceryItemSerializer


class GroceryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroceryItem.objects.order_by('created_at')
    serializer_class = GroceryItemSerializer
