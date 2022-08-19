# Generated by Django 4.0.4 on 2022-08-18 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_user_contact'),
        ('studio', '0006_remove_question_studio_remove_question_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('question', models.TextField()),
                ('studio', models.ForeignKey(db_column='studio_id', on_delete=django.db.models.deletion.CASCADE, related_name='studio_id', to='studio.studio')),
                ('user', models.ForeignKey(db_column='user_question_id', default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_question_id', to='accounts.user')),
            ],
        ),
    ]
