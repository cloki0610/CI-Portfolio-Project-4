# Generated by Django 3.2.9 on 2021-12-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promote_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promoterequest',
            name='reason',
            field=models.TextField(default=''),
        ),
    ]
