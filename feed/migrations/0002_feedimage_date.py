# Generated by Django 2.0.9 on 2019-07-17 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedimage',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
