# Generated by Django 4.0.4 on 2022-08-19 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studio',
            name='photo_category',
            field=models.JSONField(default={'child': False, 'commercial': False, 'couple': False, 'event': False, 'family': False, 'food': False, 'friend': False, 'indiv': False, 'indivOutdoor': False, 'indivStudio': False, 'pet': False, 'video': False}),
        ),
    ]
