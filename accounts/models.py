from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from budget.models import Budget


class Account(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_user_fsxard')
    default_budget = models.ForeignKey(
        Budget, on_delete=models.SET_NULL, null=True, blank=True, related_name='account')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s account"


def create_account(sender, instance, created, **kwargs):
    if created:
        account = Account.objects.create(owner=instance)
        # Create or retrieve the default budget for the user
        default_budget, _ = Budget.objects.get_or_create(
            name='Default Budget', owner=instance)
        account.default_budget = default_budget
        account.save()


post_save.connect(create_account, sender=User)
