from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserFeedbackModel(models.Model):

    MY_CHOICES = (
        ('a', 'Very good'),
        ('b', 'good'),
        ('c', 'Average'),
        ('d', 'Bad'),

    )

    

    Rate_us = models.CharField(max_length=1, choices=MY_CHOICES,blank=True)
    
    comment= models.TextField()

    

    def __str__(self):

        return self.Rate_us






