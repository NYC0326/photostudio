# Generated by Django 4.0.4 on 2022-08-19 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('question', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.TextField()),
                ('question_id', models.ForeignKey(db_column='answer', on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='question.question')),
                ('user_answer_id', models.ForeignKey(db_column='user_answer', on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='accounts.user')),
            ],
        ),
    ]