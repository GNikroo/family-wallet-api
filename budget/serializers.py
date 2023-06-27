from rest_framework import serializers
from .models import Budget
from expenses.models import Expense
from receipts.models import Receipt
from django.db.models import Sum


class BudgetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    total_expense_amount = serializers.SerializerMethodField()
    total_receipt_amount = serializers.SerializerMethodField()
    total_budget_amount = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_total_expense_amount(self, obj):
        expenses = Expense.objects.filter(
            budget=obj, owner=self.context['request'].user)
        return expenses.aggregate(Sum("amount"))["amount__sum"] or 0

    def get_total_receipt_amount(self, obj):
        receipts = Receipt.objects.filter(
            budget=obj, owner=self.context['request'].user)
        return receipts.aggregate(Sum("amount"))["amount__sum"] or 0

    def get_total_budget_amount(self, obj):
        total_receipt_amount = self.get_total_receipt_amount(obj)
        total_expense_amount = self.get_total_expense_amount(obj)
        return total_receipt_amount - total_expense_amount

    class Meta:
        model = Budget
        fields = [
            'id', 'owner', 'name', 'created_at',
            'updated_at', 'is_owner', 'total_expense_amount',
            'total_receipt_amount', 'total_budget_amount',
        ]
