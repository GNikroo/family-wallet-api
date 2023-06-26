from django.db import models
from accounts.models import Account


class Budget(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='budgets', related_query_name='budget_query')
    base_income = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return {self.id}


class Expense(models.Model):
    budget = models.OneToOneField(
        Budget, on_delete=models.CASCADE, related_name='expense', null=True, blank=True)
    expense_name = models.CharField(max_length=255)
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.expense_name}'


class Receipt(models.Model):
    budget = models.OneToOneField(
        Budget, on_delete=models.CASCADE, related_name='receipt', null=True, blank=True)
    receipt_name = models.CharField(max_length=255)
    receipt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.receipt_name}'
