# Generated by Django 4.1.4 on 2023-05-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]