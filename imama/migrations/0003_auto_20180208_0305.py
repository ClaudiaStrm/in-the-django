# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-08 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imama', '0002_auto_20180208_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_menarca',
            field=models.DateField(blank=True, null=True, verbose_name='Data da menarca (1ª menstruação)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_menopausa',
            field=models.DateField(blank=True, null=True, verbose_name='Desde quando'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_reposicao_hormonal',
            field=models.DateField(blank=True, null=True, verbose_name='Há quanto tempo'),
        ),
    ]
