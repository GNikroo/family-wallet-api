from .serializers import ReceiptSerializer
from .models import Receipt
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework import response
from baseincome.models import BaseIncome


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
        base_income = BaseIncome.objects.get(user=request.user)
        return response.Response({'total_amount': base_income.amount})
