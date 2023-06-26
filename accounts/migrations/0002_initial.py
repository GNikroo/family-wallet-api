# Generated by Django 4.2.2 on 2023-06-26 19:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('budget', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('groceries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='budget_account', to='budget.budget'),
        ),
        migrations.AddField(
            model_name='account',
            name='grocery_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grocery_list_account', to='groceries.groceryitem'),
        ),
        migrations.AddField(
            model_name='account',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
