from rest_framework import serializers
from .models import Receipt


class ReceiptSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Receipt
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'category',
            'amount', 'description', 'is_owner', 'date',
            'budget',
        ]
