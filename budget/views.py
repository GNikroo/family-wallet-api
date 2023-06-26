from rest_framework import generics
from .models import Budget, Expense, Receipt
from .serializers import BudgetSerializer, ExpenseSerializer, ReceiptSerializer


class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.order_by('created_at')
    serializer_class = ExpenseSerializer


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.order_by('created_at')
    serializer_class = ExpenseSerializer


class ReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.order_by('created_at')
    serializer_class = ReceiptSerializer


class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.order_by('created_at')
    serializer_class = ReceiptSerializer
