from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import Account
from budget.models import Budget


class CustomRegisterSerializer(RegisterSerializer):
    def custom_registration(self, user):
        # Create or retrieve the default budget for the user
        default_budget, _ = Budget.objects.get_or_create(
            name='Default Budget', owner=user)

        # Assign the default budget to the user's account
        user.account.default_budget = default_budget
        user.account.save()

    def save(self, request):
        user = super().save(request)
        self.custom_registration(user)
        return user


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Account
        fields = [
            'id', 'owner', 'image', 'is_owner',
        ]
