# Generated by Django 3.0 on 2019-12-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('site', models.URLField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
