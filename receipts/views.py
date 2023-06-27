from .serializers import ReceiptSerializer
from .models import Receipt
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework import response
from django.db.models import Sum


class ReceiptList(generics.ListCreateAPIView):
    serializer_class = ReceiptSerializer
    queryset = Receipt.objects.order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Receipt.objects.order_by('-created_at')


class TotalReceiptStats(APIView):
    def get(self, request):
        receipt = Receipt.objects.filter(owner=request.user)
        total_amount = Receipt.aggregate(Sum("amount"))
        return response.Response(total_amount)
