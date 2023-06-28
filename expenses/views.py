from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework import response
from .models import Expense
from .serializers import ExpenseSerializer
from django.db.models import Sum


class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.order_by('-created_at')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Expense.objects.order_by('-created_at')


class TotalExpenseStats(APIView):
    def get(self, request):
        expenses = Expense.objects.filter(owner=request.user)
        total_amount = expenses.aggregate(Sum("amount"))
        return response.Response(total_amount)
