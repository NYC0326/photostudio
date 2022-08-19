# Generated by Django 4.0.4 on 2022-08-19 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('studio', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time_hour', models.IntegerField()),
                ('start_time_minute', models.IntegerField()),
                ('end_time_hour', models.IntegerField()),
                ('end_time_minute', models.IntegerField()),
                ('person_cnt', models.IntegerField()),
                ('admitted', models.BooleanField(default=False)),
                ('reserver_id', models.ForeignKey(db_column='reserver', on_delete=django.db.models.deletion.CASCADE, related_name='reserver', to='accounts.user')),
                ('reserving_studio_id', models.ForeignKey(db_column='studio_reserve', on_delete=django.db.models.deletion.CASCADE, related_name='studio_reserve', to='studio.studio')),
            ],
        ),
    ]
