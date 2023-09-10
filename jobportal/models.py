from os import name
from django.db import models
from autoslug import AutoSlugField
from django.db.models.deletion import CASCADE



# Create your models here.


# class Category(models.Model):
#     name=models.CharField(max_length=200)
#     slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

#     def __str__(self):
#         return self.name

class Category2(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True)

    def __str__(self):
        return self.name



class Job2(models.Model):
    category=models.ForeignKey(Category2,on_delete=CASCADE)
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=50,null=True)
    city=models.CharField(max_length=200)
    location=models.CharField(max_length=300)
    timing=models.CharField(max_length=100)
    salary=models.IntegerField()
    desc=models.TextField()
    
    def __str__(self) :
        return self.name




class JobApply(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    criteria=models.CharField(max_length=200)
    exp=models.IntegerField()
    # resume=models.CharField(max_length=200)
    resume=models.FileField(upload_to='image',max_length=250,null=True,default=None)

    def __str__(self):
        return self.name


class Company(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name=models.CharField(max_length=200)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)
    image=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

class Curriculum(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    resume=models.FileField(upload_to='image',max_length=250,null=True,default=None)
    carrier=models.CharField(max_length=200)
    email=models.EmailField(blank=True,unique=False)
    
    salary=models.IntegerField()
    exp=models.IntegerField()
    desc=models.TextField()
   
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    address=models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Service(models.Model):
    name=models.CharField(max_length=50)
    slug=AutoSlugField(populate_from='name',unique=True,null=True,default=None)

    def __str__(self):
        return self.name