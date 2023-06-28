from rest_framework import serializers
from .models import GroceryItem


class GrocerySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = GroceryItem
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'description',
            'item', 'amount', 'is_owner', 'budget',
        ]
