from rest_framework import serializers
from .models import Budget, Expense, Receipt


class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Expense
        fields = [
            'id', 'owner', 'is_owner', 'expense_name', 'expense_amount',
        ]


class ReceiptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Receipt
        fields = [
            'id', 'owner', 'is_owner', 'receipt_name', 'receipt_amount',
        ]


class BudgetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    expense = ExpenseSerializer(required=False)
    receipt = ReceiptSerializer(required=False)

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def create(self, validated_data):
        expense_data = validated_data.pop('expense', None)
        receipt_data = validated_data.pop('receipt', None)
        # Get the current user from the request
        request = self.context['request']
        owner = request.user

        # Add the owner to the validated_data
        validated_data['owner'] = owner

        # Create the Budget instance
        budget = Budget.objects.create(**validated_data)

        if expense_data:
            # Add the owner to the expense_data
            expense_data['owner'] = owner
            Expense.objects.create(budget=budget, **expense_data)

        if receipt_data:
            # Add the owner to the receipt_data
            receipt_data['owner'] = owner
            Receipt.objects.create(budget=budget, **receipt_data)

        return budget

    class Meta:
        model = Budget
        fields = '__all__'
