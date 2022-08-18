# Generated by Django 4.0.4 on 2022-08-18 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studio_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('post_num', models.IntegerField()),
                ('pic_folder', models.URLField()),
                ('ceo_id', models.ForeignKey(db_column='ceo_id', on_delete=django.db.models.deletion.CASCADE, related_name='ceo_id', to='accounts.user')),
                ('contact', models.ForeignKey(db_column='contact', on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='accounts.user')),
            ],
        ),
    ]