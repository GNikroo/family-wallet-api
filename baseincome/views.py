from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView
from .serializers import BaseIncomeSerializer
from .models import BaseIncome
from accounts.models import Account
from budget.models import Budget
from rest_framework import permissions


class BaseIncomeList(ListCreateAPIView):
    serializer_class = BaseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BaseIncome.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BaseIncomeDetail(RetrieveUpdateAPIView):
    serializer_class = BaseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = BaseIncome.objects.all()

    def get_queryset(self):
        account = Account.objects.get(owner=self.request.user)
        return BaseIncome.objects.filter(budget=account.default_budget)
