# Generated by Django 3.2.2 on 2021-05-11 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='case',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
