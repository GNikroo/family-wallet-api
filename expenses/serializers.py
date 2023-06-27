from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Expense
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category',
            'amount', 'description', 'is_owner', 'date',
            'budget',
        ]
