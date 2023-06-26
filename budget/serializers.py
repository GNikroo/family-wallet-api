from rest_framework import serializers
from .models import Budget, Expense, Receipt


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    expense = ExpenseSerializer(required=False)
    receipt = ReceiptSerializer(required=False)

    class Meta:
        model = Budget
        fields = '__all__'
