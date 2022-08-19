from django.db import models
from accounts.models import User
from question.models import Question

class Answer(models.Model):
    question_id = models.ForeignKey(Question, related_name='question_id', on_delete=models.CASCADE, db_column='question_id')
    user_answer_id = models.ForeignKey(User, related_name='user_answer_id', on_delete=models.CASCADE, db_column='user_answer_id')
    answer = models.TextField()

    def __str__(self):
        return self.answer