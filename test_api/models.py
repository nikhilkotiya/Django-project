from django.db import models
from users.models import User

class Compony(models.Model):
    compony_name=models.CharField(max_length=50,null=True, blank=True)
    def __str__(self):
        return self.compony_name

class Test_name(models.Model):
    test_name=models.CharField(max_length=50,null=True)
    compony = models.ForeignKey('Compony', related_name='test',on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.test_name

class Quize(models.Model):
    compony_name = models.ForeignKey(Compony,related_name='comp',on_delete=models.CASCADE)
    test_name= models.ForeignKey(Test_name,on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class Save_test(models.Model):
    test_name = models.CharField(max_length=50,null=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField()
    