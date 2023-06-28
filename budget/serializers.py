from rest_framework import serializers
from .models import Budget
from expenses.models import Expense
from receipts.models import Receipt
from groceries.models import GroceryItem
from django.db.models import Sum


class BudgetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    total_expenses = serializers.SerializerMethodField()
    total_receipts = serializers.SerializerMethodField()
    total_grocery_expenses = serializers.SerializerMethodField()
    total_budget_amount = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_total_expenses(self, obj):
        expenses = Expense.objects.filter(
            budget=obj, owner=self.context['request'].user)
        return expenses.aggregate(Sum("amount"))["amount__sum"] or 0

    def get_total_receipts(self, obj):
        receipts = Receipt.objects.filter(
            budget=obj, owner=self.context['request'].user)
        return receipts.aggregate(Sum("amount"))["amount__sum"] or 0

    def get_total_grocery_expenses(self, obj):
        groceries = GroceryItem.objects.filter(
            budget=obj, owner=self.context['request'].user)
        return groceries.aggregate(Sum("amount"))["amount__sum"] or 0

    def get_total_budget_amount(self, obj):
        total_receipts = self.get_total_receipts(obj)
        total_expenses = self.get_total_expenses(obj)
        total_grocery_expenses = self.get_total_grocery_expenses(
            obj)
        return total_receipts - total_expenses - total_grocery_expenses

    class Meta:
        model = Budget
        fields = [
            'id', 'owner', 'name', 'created_at',
            'updated_at', 'is_owner', 'total_expenses',
            'total_receipts', 'total_budget_amount',
            'total_grocery_expenses',
        ]
