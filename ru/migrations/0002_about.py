# Generated by Django 2.2 on 2020-01-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
