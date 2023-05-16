from django.db import models

class Hello(models.Model):
    hey = models.CharField(max_length=100)