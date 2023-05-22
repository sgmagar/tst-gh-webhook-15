from django.db import models

class Hello(models.Model):
    hey = models.CharField(max_length=100)
    
    def __str__(self):
        return f"Something {self.hey} heyy"
