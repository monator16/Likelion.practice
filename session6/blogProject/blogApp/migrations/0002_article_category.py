# Generated by Django 4.0.3 on 2022-04-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='', max_length=100),
        ),
    ]