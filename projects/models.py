from django.db import models

# Create your models here
class Project(models.Model):
    description = models.TextField(max_length=1000, null=False)
    iconName = models.CharField(max_length=60, null=True) 
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.title