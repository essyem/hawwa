# Generated by Django 5.1.7 on 2025-03-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminops', '0002_attachment_budget_category_employee_financialreport_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
