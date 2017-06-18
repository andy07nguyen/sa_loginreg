from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
import re, bcrypt
from datetime import datetime
import datetime
# Create your models here.
#USER MANAGER:
class UserManager(models.Manager):
#     #REGISTRATION CLASS:
    def register(self, postData):
        print "FROM MODEL: ", postData

#USER CLASS MODEL:
class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()


    # def __str__(self):
    #     return "First Name : " + self.first_name + "Last Name:  " + self.last_name + "ID:  " + str(self.id) + "\n"
