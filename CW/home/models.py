from django.db import models

# Create your models here.
class userInfo(models.Model):
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 20)


class stuInfo(models.Model):
    username = models.CharField(max_length=50)
    first_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)
    email = models.EmailField( max_length=255)
    phone_no = models.CharField(max_length=12)
    guardian_name = models.CharField( max_length=255)
    caste = models.CharField( max_length=255)
    age = models.CharField( max_length=255)
    nationality = models.CharField( max_length=255)
    gender = models.CharField( max_length=255)
    address = models.CharField( max_length=255)
    status = models.BooleanField(default = False)

class feed(models.Model):
    name = models.CharField(max_length=50)
    feedback = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now = True)