from django.db import models
from django.contrib.auth.models import User
from budget.models import Budget


class Receipt(models.Model):

    CATEGORY_OPTIONS = [
        ('INCOME', 'Income'),
        ('REFUND', 'Refund'),
        ('GIFT', 'Gift'),
        ('REBATE', 'Rebate'),
        ('OTHER', 'Other')
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.id}"
