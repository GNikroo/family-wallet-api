from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework import response
from .models import GroceryItem
from .serializers import GrocerySerializer
from django.db.models import Sum


class GroceryItemList(generics.ListCreateAPIView):
    serializer_class = GrocerySerializer
    queryset = GroceryItem.objects.order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroceryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrocerySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = GroceryItem.objects.order_by('-created_at')


class TotalGroceryExpenseStats(APIView):
    def get(self, request):
        groceries = GroceryItem.objects.filter(owner=request.user)
        total_amount = groceries.aggregate(Sum("amount"))
        return response.Response(total_amount)
