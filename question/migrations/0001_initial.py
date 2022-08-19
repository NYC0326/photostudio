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
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.TextField()),
                ('studio_id', models.ForeignKey(db_column='studio_question', on_delete=django.db.models.deletion.CASCADE, related_name='studio_question', to='studio.studio')),
                ('user_question_id', models.ForeignKey(db_column='user_question', on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to='accounts.user')),
            ],
        ),
    ]
