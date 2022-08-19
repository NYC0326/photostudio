from django.db import models
from accounts.models import User

class Studio(models.Model):
    studio_name = models.CharField(max_length=20)
    ceo_id = models.ForeignKey(User, related_name='ceo_id', on_delete=models.CASCADE, db_column='ceo_id')    
    location = models.CharField(max_length=100)
    post_num = models.CharField(max_length=5, default='')
    info = models.CharField(max_length=100, default='', null=True)
    intro = models.TextField(default='', null=True)
    insta_id = models.CharField(max_length=100, default='', null=True)

    def __str__(self):
        return self.studio_name