from rest_framework import generics, permissions
from .models import Budget, Expense, Receipt
from .serializers import BudgetSerializer, ExpenseSerializer, ReceiptSerializer


class BudgetList(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BudgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.order_by('created_at')
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.order_by('created_at')
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReceiptList(generics.ListCreateAPIView):
    queryset = Receipt.objects.order_by('created_at')
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReceiptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Receipt.objects.order_by('created_at')
    serializer_class = ReceiptSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
