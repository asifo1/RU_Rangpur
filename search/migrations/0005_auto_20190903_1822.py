# Generated by Django 2.2 on 2019-09-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_report_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='status',
            field=models.CharField(blank=True, default='Unsolved', max_length=60, null=True),
        ),
    ]