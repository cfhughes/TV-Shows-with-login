from django.db import models
from django.contrib import messages
import re
import bcrypt

class UserManager(models.Manager):
    def login_validate(self, postData):
        errors = {}
        
        user = User.objects.filter(email=postData['email']).first() # Get user based on email address
        if not user:
            errors['email'] = "No user exists with that email address"
        elif not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
            errors['password'] = "Incorrect Password"
        
        return user, errors

    def register_validate(self, postData):
        errors = {}
    
        #RegEx for email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        PASSWORD_REGEX = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d,!@#$%^&*+=]{8,}$')

        if len(postData['email']) < 1:
            errors['email'] = 'Email is required!'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email-invalid'] = 'Invalid Email!'
        user_check = User.objects.filter(email=postData['email'])
        if user_check.exists():
            errors['email_inuse'] = 'That email address is already in use!'
        if len(postData['password']) <= 6:
            errors['password'] = 'Password should more than 6 characters!'
        elif not PASSWORD_REGEX.match(postData['password']):
            errors['password_valid'] = 'Password must contain at least 1 number and capitalization!'
        if postData['password'] != postData['password_confirm']:
            errors['password'] = 'Passwords don\'t match!'
        if len(postData['first_name']) <= 0:
            errors['first_name'] = 'First Name is required!'
        if len(postData['last_name']) <= 0:
            errors['last_name'] = 'Last Name is required!'

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()