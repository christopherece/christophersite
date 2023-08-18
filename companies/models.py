from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    hire_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True, null=True)
    logo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name
    

class Experience(models.Model):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=500, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.description