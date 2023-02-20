from django.db import models
from django.contrib.auth.models import User
# from  PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ForeignKey(
        "Section", on_delete=models.CASCADE, null=True, blank=True)
    # image = models.ImageField(default='default.png', uplaod_to='profile_pics')
    bio = models.CharField(max_length=2000, blank=True)
    skills = models.CharField(max_length=2000, blank=True)
    aoi = models.CharField(max_length=2000, blank=True)
    github = models.CharField(max_length=2000, blank=True)
    linkedin = models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    

# class Grade(models.Model):
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#     test1 = models.CharField(max_length=2000, blank= True)
#     test2 = models.CharField(max_length=2000, blank= True)
#     test3 = models.CharField(max_length=2000, blank= True)
    
#     test1d = models.ImageField(upload_to= 'plots', blank = True)
#     test2d = models.ImageField(upload_to= 'plots', blank = True)
#     test3d = models.ImageField(upload_to= 'plots', blank = True)
    
#     test1pd = models.ImageField(upload_to= 'plots', blank = True)
#     test2pd = models.ImageField(upload_to= 'plots', blank = True)
#     test3pd = models.ImageField(upload_to= 'plots', blank = True)
    
#     test1p = models.ImageField(upload_to= 'plots', blank = True)
#     test2p = models.ImageField(upload_to= 'plots', blank = True)
#     test3p = models.ImageField(upload_to= 'plots', blank = True)
 
    
class Section(models.Model):
    section = models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.section
    
    
class Questions(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, blank=True)
    question_field = models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return self.question_filed
    

class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer_field = models.CharField(max_length=2000, blank=True)
    
    def __str__(self):
        return f"{self.user} answered {self.answer_field}"
    