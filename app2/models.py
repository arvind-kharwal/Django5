from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
    # def __str__(self):
    #    return self.email
    
    #def __str__(self):
    #    return str(self.age)