# Generated by Django 3.2.6 on 2021-09-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacation', '0004_auto_20210925_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('DENIED', 'Denied')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='type_vacation',
            field=models.CharField(choices=[('ANNUAL_LEAVE', 'Annual Leave'), ('SICK_LEAVE', 'Sick Leave'), ('OTHER', 'Other'), ('PAID_VACATION', 'Paid Vacation')], default='OTHER', max_length=20),
        ),
    ]
