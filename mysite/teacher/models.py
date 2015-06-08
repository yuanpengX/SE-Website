from django.db import models

# Create your models here.
class Question(models.Model):
    QuestionId = models.CharField(max_length=20)
    Stem = models.CharField(max_length=2000);
    OptionA = models.CharField(max_length=100);
    OptionB = models.CharField(max_length=100);
    OptionC = models.CharField(max_length=100,blank=True);
    OptionD = models.CharField(max_length=100,blank=True);
    Type = models.IntegerField;
    Difficulty = models.FloatField;
    Flag = models.BooleanField;
    Answer = models.CharField(max_length=20);
    Charpter = models.CharField(max_length=20);
    Course = models.CharField(max_length=20);

class Paper(models.Model):
    PaperId = models.CharField(max_length=20);
    QID = models.CharField(max_length=400);
    Creater = models.CharField(max_length=20);
    ClassId = models.CharField(max_length=20);