from django.db import models
from studio.models import Studio

class CategoryStudio(models.Model): 
    studio_category = models.ForeignKey(Studio, related_name='studio_category', on_delete=models.CASCADE, db_column='studio_category')
    category_indiv = models.BooleanField(default=False)
    category_indivStudio = models.BooleanField(default=False)
    category_indivOutdoor = models.BooleanField(default=False)
    category_family = models.BooleanField(default=False)
    category_child = models.BooleanField(default=False)
    category_couple = models.BooleanField(default=False)
    category_friend = models.BooleanField(default=False)
    category_event = models.BooleanField(default=False)
    category_pet = models.BooleanField(default=False)
    category_commercial = models.BooleanField(default=False)
    category_food = models.BooleanField(default=False)
    category_video = models.BooleanField(default=False)