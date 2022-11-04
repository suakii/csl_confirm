from django.db import models
from django.contrib.auth.models import User


class StudentInform(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    inform1 = models.CharField(max_length=100, blank=True)
    inform2 = models.CharField(max_length=100, blank=True)
    inform3 = models.CharField(max_length=100, blank=True)
    inform4 = models.CharField(max_length=100, blank=True)
    inform5 = models.CharField(max_length=100, blank=True)
    inform6 = models.CharField(max_length=100, blank=True)
    inform7 = models.CharField(max_length=100, blank=True)
    inform8 = models.CharField(max_length=100, blank=True)
    inform9 = models.CharField(max_length=100, blank=True)
    inform10 = models.CharField(max_length=100, blank=True)




class SubjectInform(models.Model):
    inform0 = models.CharField(max_length=100, blank=True)
    inform1 = models.CharField(max_length=100, blank=True)
    inform2 = models.CharField(max_length=100, blank=True)
    inform3 = models.CharField(max_length=100, blank=True)
    inform4 = models.CharField(max_length=100, blank=True)
    inform5 = models.CharField(max_length=100, blank=True)
    inform6 = models.CharField(max_length=100, blank=True)
    inform7 = models.CharField(max_length=100, blank=True)
    inform8 = models.CharField(max_length=100, blank=True)
    inform9 = models.CharField(max_length=100, blank=True)
    inform10 = models.CharField(max_length=100, blank=True)



