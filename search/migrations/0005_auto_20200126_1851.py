# Generated by Django 2.2 on 2020-01-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200126_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committee',
            name='president',
            field=models.CharField(blank=True, default=None, max_length=40, null=True),
        ),
    ]
