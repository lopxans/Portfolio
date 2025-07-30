from django.db import models
from datetime import date

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=13)
    message = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    delete_time = models.DateTimeField(null=True)   
    deleted_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='certificate_photo/', blank=True, null=True)
    issued_date = models.DateField(default=date.today)
      
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    delete_time = models.DateTimeField(null=True)   
    deleted_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    image = models.ImageField(upload_to='project_photo/', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.CharField(max_length=200)
     
    created_at = models.DateTimeField(auto_now_add=True)
    is_delete = models.BooleanField(default=False)
    delete_time = models.DateTimeField(null=True)
    deleted_time = models.DateTimeField(null=True)
    

    def __str__(self):
        return self.title