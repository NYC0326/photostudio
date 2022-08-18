from django.db import models
from accounts.models import User

class Studio(models.Model):
    studio_name = models.CharField(max_length=20)
    ceo = models.ForeignKey(User, related_name='ceo_id', on_delete=models.CASCADE, db_column='ceo_id')    
    location = models.CharField(max_length=100)
    post_num = models.CharField(max_length=5, default='')
    pic_folder = models.CharField(max_length=50)

    def __str__(self):
        return self.studio_name