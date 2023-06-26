from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    base_income = models.DecimalField(
        max_digits=10, default=0, decimal_places=2)

    def __str__(self):
        return {self.id}


class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.OneToOneField(
        Budget, on_delete=models.CASCADE, related_name='expense')
    expense_name = models.CharField(max_length=255, null=True, blank=True)
    expense_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.expense_name}'


class Receipt(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    budget = models.OneToOneField(
        Budget, on_delete=models.CASCADE, related_name='receipt')
    receipt_name = models.CharField(max_length=255, null=True, blank=True)
    receipt_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.receipt_name}'
