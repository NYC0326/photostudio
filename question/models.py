from django.db import models
from accounts.models import User
from studio.models import Studio

class Question(models.Model):
    studio_id = models.ForeignKey(Studio, related_name='studio_id', on_delete=models.CASCADE, db_column='studio_id')
    user_question_id = models.ForeignKey(User, related_name='user_question_id', on_delete=models.CASCADE, db_column='user_question_id')
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    question = models.TextField()

    def __str__(self):
        return self.title