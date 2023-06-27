from django.db import models
from django.contrib.auth.models import User
from baseincome.models import BaseIncome
from budget.models import Budget


class Receipt(models.Model):

    CATEGORY_OPTIONS = [
        ('ONLINE_SHOPPING', 'Online'),
        ('CLOTHING', 'Clothing'),
        ('TOYS', 'Toys'),
        ('SYSTEM', 'System Bolaget'),
        ('CONVENIENCE', 'Convenience'),
        ('VOLVO', 'Volvo'),
        ('TRAVEL', 'Travel'),
        ('TAKEOUT', 'Takeout'),
        ('RENT', 'Rent'),
        ('ENTERTAINMENT', 'Entertainment'),
        ("BILLS", "Bills"),
        ("Recurring", "Recurring"),
        ('OTHERS', 'Others')
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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        base_income = BaseIncome.objects.get(user=self.owner)
        base_income.amount += self.amount
        base_income.save()

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.id}"
