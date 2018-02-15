# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-08 04:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('imama', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='amigo_rosa',
            field=models.CharField(help_text='*', max_length=200, verbose_name='Navegador'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='celular',
            field=models.CharField(blank=True, help_text=' Exemplo: 99 9999999999', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cidade',
            field=models.CharField(help_text='*', max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(help_text=' Apenas números', max_length=20, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_entrevista',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data da entrevista e mamografia PoA Rural'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_mamografia',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data da mamografia mais recente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_menarca',
            field=models.DateField(blank=True, verbose_name='Data da menarca (1ª menstruação)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_menopausa',
            field=models.DateField(blank=True, verbose_name='Desde quando'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(help_text='* Formato: dd/mm/aaaa', verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_outros_exames',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Outros exames das mamas (data)'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='data_reposicao_hormonal',
            field=models.DateField(blank=True, verbose_name='Há quanto tempo'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='email',
            field=models.CharField(help_text='*', max_length=200),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(help_text='*', max_length=400, verbose_name='Endereço'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='etnia',
            field=models.CharField(help_text='*', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nome',
            field=models.CharField(help_text='*', max_length=200, verbose_name='Nome da paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observacoes',
            field=models.TextField(blank=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rg',
            field=models.CharField(help_text='*', max_length=20, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(help_text='*', max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(help_text='* Exemplo: 99 9999999999', max_length=20),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='ultima_consulta_ginecologista',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Data da última consulta com ginecologista'),
        ),
    ]