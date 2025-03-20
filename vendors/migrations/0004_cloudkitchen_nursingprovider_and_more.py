# Generated by Django 5.1.7 on 2025-03-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0003_department_employeetype_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloudKitchen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cuisine_type', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),

    ]
