# Generated by Django 2.2 on 2020-01-26 11:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('view', models.PositiveIntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('present_address', models.CharField(blank=True, max_length=300, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=300)),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('college', models.CharField(blank=True, max_length=200, null=True)),
                ('university', models.CharField(blank=True, max_length=200, null=True)),
                ('relation', models.CharField(blank=True, max_length=200, null=True)),
                ('dept', models.CharField(blank=True, max_length=100, null=True)),
                ('session', models.CharField(blank=True, max_length=20, null=True)),
                ('blood', models.CharField(blank=True, max_length=9, null=True)),
                ('father', models.CharField(blank=True, max_length=100, null=True)),
                ('mother', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('fb', models.CharField(blank=True, max_length=100, null=True)),
                ('bio', models.TextField(blank=True, max_length=100, null=True)),
                ('img', models.ImageField(blank=True, default='default.png', upload_to='profile_pics')),
                ('alumni', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]