# Generated by Django 4.2.2 on 2023-06-28 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ONLINE_SHOPPING', 'Online'), ('CLOTHING', 'Clothing'), ('TOYS', 'Toys'), ('SYSTEM', 'System Bolaget'), ('CONVENIENCE', 'Convenience'), ('VOLVO', 'Volvo'), ('TRAVEL', 'Travel'), ('TAKEOUT', 'Takeout'), ('RENT', 'Rent'), ('ENTERTAINMENT', 'Entertainment'), ('BILLS', 'Bills'), ('CHARITY', 'Charity'), ('Recurring', 'Recurring'), ('OTHER', 'Other')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='budget.budget')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_at'],
            },
        ),
    ]
