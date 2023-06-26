from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_user_fsxard')
    budget = models.ForeignKey(
        'budget.Budget', default=None, on_delete=models.CASCADE, related_name='budget_account')
    grocery_list = models.ForeignKey(
        'groceries.GroceryItem', on_delete=models.CASCADE, related_name='grocery_list_account')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s account"


def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(owner=instance)


post_save.connect(create_account, sender=User)
