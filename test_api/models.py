from django.db import models
from users.models import User
import uuid 
class Company(models.Model):
    company_name=models.CharField(max_length=50,null=True,blank=True)#unique=True
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    tagline=models.TextField(null=True,blank=True)
    website_url=models.URLField(max_length=200,blank=True,null=True)
    company_type=models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.company_name

class Test_name(models.Model):
    test_name=models.CharField(max_length=50,null=True)
    company= models.ForeignKey(Company,max_length=50,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.test_name

class Quize(models.Model):
    company= models.ForeignKey(Company,null=True,on_delete=models.CASCADE)
    test = models.ForeignKey(Test_name,null=True,on_delete=models.CASCADE)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    def __str__(self):
        return self.question

class Save_test(models.Model):
    company= models.ForeignKey(Company,null=True,on_delete=models.CASCADE)
    test = models.ForeignKey(Test_name,null=True,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField()