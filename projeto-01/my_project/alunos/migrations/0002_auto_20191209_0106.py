# Generated by Django 3.0 on 2019-12-09 04:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='ano_nasc',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1970)]),
        ),
    ]
