from django.db import models
from django.contrib.auth.models import User
from budget.models import Budget


class BaseIncome(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return f"Income {self.id}"
