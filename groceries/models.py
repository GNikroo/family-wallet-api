from django.db import models
from accounts.models import Account


class GroceryItem(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='grocery_items')
    item_name = models.CharField(max_length=255)
    item_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    item_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.item_name}'
