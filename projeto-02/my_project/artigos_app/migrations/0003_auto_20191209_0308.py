# Generated by Django 3.0 on 2019-12-09 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos_app', '0002_artigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artigo',
            old_name='atualizadp_em',
            new_name='atualizado_em',
        ),
    ]
