# Generated by Django 4.1.2 on 2023-02-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffs', '0002_auto_20201124_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
