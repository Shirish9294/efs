# Generated by Django 3.1.5 on 2021-01-31 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_fund'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='fund_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]