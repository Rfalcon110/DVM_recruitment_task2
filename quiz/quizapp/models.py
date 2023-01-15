from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    quiz_name=models.CharField(max_length=200,) 

    def __str__(self) -> str:
        return self.quiz_name


class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    question_text=models.CharField(max_length=200,null=True,blank=True)
    choice_1=models.CharField(max_length=200,null=True,blank=True)
    choice_2=models.CharField(max_length=200,null=True,blank=True)
    choice_3=models.CharField(max_length=200,null=True,blank=True)
    choice_4=models.CharField(max_length=200,null=True,blank=True)
    answer=models.CharField(max_length=200,null=True,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    def  __str__(self):
        return self.question_text


class Result(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    correct=models.IntegerField(default=0)
    wrong=models.IntegerField(default=0) 
    total=models.IntegerField(default=0)
    quiz_given=models.BooleanField(default=False)  
 
      





        