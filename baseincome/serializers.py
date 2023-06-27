from rest_framework import serializers
from .models import BaseIncome


class BaseIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseIncome
        fields = ['id', 'amount', 'budget']
