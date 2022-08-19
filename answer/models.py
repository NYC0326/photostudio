from django.db import models
from accounts.models import User
from question.models import Question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE, db_column='answer')
    user_answer_id = models.ForeignKey(User, related_name='user_answer', on_delete=models.CASCADE, db_column='user_answer')
    reply = models.TextField()

    def __str__(self):
        return self.reply