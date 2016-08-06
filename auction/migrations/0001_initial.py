# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-06 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='pictures')),
                ('username', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bids',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.items'),
        ),
    ]