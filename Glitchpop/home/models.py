from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

class Register(models.Model):
    nam=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    ph=models.CharField(max_length=12)
    prog=models.CharField(max_length=122, null=True)
    goal=models.CharField(max_length=122, null=True)

    def __str__(self):
        return self.name
    def __str__(self):
        return self.nam

    
    