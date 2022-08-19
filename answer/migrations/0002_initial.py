# Generated by Django 4.0.4 on 2022-08-18 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_user_contact'),
        ('answer', '0001_initial'),
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(db_column='question_id', on_delete=django.db.models.deletion.CASCADE, related_name='question_id', to='question.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(db_column='user_answer', default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='accounts.user'),
        ),
    ]
