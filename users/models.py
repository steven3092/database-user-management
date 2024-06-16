import datetime

from django.db import models
from django.utils import timezone

class ListOfUser(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=True, verbose_name='ID')
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    create_date = models.DateTimeField()
    def __str__(self):
        return self.name
        
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
