# Generated by Django 4.0.4 on 2022-08-19 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studio', '0003_remove_studio_photo_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryStudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_indiv', models.BooleanField(default=False)),
                ('category_indivStudio', models.BooleanField(default=False)),
                ('category_indivOutdoor', models.BooleanField(default=False)),
                ('category_family', models.BooleanField(default=False)),
                ('category_child', models.BooleanField(default=False)),
                ('category_couple', models.BooleanField(default=False)),
                ('category_friend', models.BooleanField(default=False)),
                ('category_event', models.BooleanField(default=False)),
                ('category_pet', models.BooleanField(default=False)),
                ('category_commercial', models.BooleanField(default=False)),
                ('category_food', models.BooleanField(default=False)),
                ('category_video', models.BooleanField(default=False)),
                ('studio_category', models.ForeignKey(db_column='studio_category', on_delete=django.db.models.deletion.CASCADE, related_name='studio_category', to='studio.studio')),
            ],
        ),
    ]