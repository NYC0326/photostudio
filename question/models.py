from django.db import models
from accounts.models import User
from studio.models import Studio

class Question(models.Model):
    studio_id = models.ForeignKey(Studio, related_name='studio_question', on_delete=models.CASCADE, db_column='studio_question')
    user_question_id = models.ForeignKey(User, related_name='user_question', on_delete=models.CASCADE, db_column='user_question')
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()

    def __str__(self):
        return self.title