# Generated by Django 3.2.9 on 2021-12-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_alter_theme_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_body',
            field=models.TextField(blank=True, default=''),
        ),
    ]