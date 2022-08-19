from django.db import models
from studio.models import Studio
from django.conf import settings

# Create your models here.
def get_img_storage_path(instance, filename):
    return '%s/%s/%s' % (settings.MEDIA_ROOT, instance.studio_portfolio.studio_name, filename)

class Photo(models.Model):
    studio_portfolio = models.ForeignKey(Studio, related_name='studio_portfolio', on_delete=models.CASCADE, db_column="studio_id_photo")
    pic = models.ImageField(blank=True, null=True, upload_to=get_img_storage_path)
    title = models.CharField(max_length=50)
    camera = models.CharField(max_length=50)

    def __str__(self):
        return self.title