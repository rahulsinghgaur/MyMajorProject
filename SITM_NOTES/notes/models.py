from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    subject = models.CharField(max_length = 122)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Notes(models.Model):
    subcode = models.CharField(max_length = 15,default="")
    name = models.CharField(max_length = 122)
    branch = models.CharField(max_length = 10,default="")
    sem = models.CharField(max_length = 10)
    notesfile = models.FileField(default="")

    def __str__(self):
        return self.name
    
