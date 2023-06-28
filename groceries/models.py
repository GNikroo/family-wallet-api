from django.db import models
from django.contrib.auth.models import User
from budget.models import Budget


class GroceryItem(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.item
