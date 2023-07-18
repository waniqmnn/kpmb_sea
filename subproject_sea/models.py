from django.db import models

# Create your models here.

class Student(models.Model):
    Studentid = models.CharField(max_length = 11,primary_key = True)
    Studentname = models.CharField(max_length = 100)
    Spassword = models.CharField(max_length=100)
    Studentphone = models.CharField(max_length=12)
    Studentprogramme = models.CharField(max_length = 100)

    def __str__(self):
        return self.Studentid

class Level(models.Model):
    Levelid = models.CharField(max_length = 6,primary_key = True)
    Leveldescription = models.TextField()

    def __str__(self):
        return self.Levelid

class Category(models.Model):
    Categoryid = models.CharField(max_length = 6,primary_key = True)
    Categorydescription = models.TextField()

    def __str__(self):
        return self.Categoryid

class Achievement(models.Model):
    Studentid = models.ForeignKey(Student,on_delete = models.CASCADE)
    Levelid = models.ForeignKey(Level,on_delete = models.CASCADE)
    Categoryid = models.ForeignKey(Category,on_delete = models.CASCADE)
    Award = models.CharField(max_length = 100)
    Achievement_date = models.DateField()
    Event = models.CharField(max_length = 100)

class Admin(models.Model):
    adminid = models.CharField(max_length=5,primary_key=True)
    name = models.CharField(max_length=100)
    apassword = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

