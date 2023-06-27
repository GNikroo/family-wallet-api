from .serializers import ExpenseSerializer
from .models import Expense
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework import response
from baseincome.models import BaseIncome


class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.order_by('-created_at')
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Expense.objects.order_by('-created_at')


class TotalExpenseStats(APIView):
    def get(self, request):
        base_income = BaseIncome.objects.get(user=request.user)
        return response.Response({'total_amount': base_income.amount})
