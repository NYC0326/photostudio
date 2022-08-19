from django.db import models
from accounts.models import User
from studio.models import Studio

class Reserve(models.Model):
    reserver_id = models.ForeignKey(User, related_name='reserver',on_delete=models.CASCADE, db_column='reserver')
    reserving_studio_id = models.ForeignKey(Studio, related_name='studio_reserve', on_delete=models.CASCADE, db_column='studio_reserve')
    start_time_hour = models.IntegerField()
    start_time_minute = models.IntegerField()
    end_time_hour = models.IntegerField()
    end_time_minute = models.IntegerField()
    person_cnt = models.IntegerField()
    admitted = models.BooleanField(default=False)


    def __str__(self):
        return self.studio_name