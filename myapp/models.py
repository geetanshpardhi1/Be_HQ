from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    resume_file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
   

    def __str__(self):
        return self.title
    
