# Generated by Django 4.0.4 on 2022-08-19 06:58

from django.db import migrations, models
import photo.models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_alter_photo_camera_alter_photo_pic_alter_photo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=photo.models.get_img_storage_path),
        ),
    ]
