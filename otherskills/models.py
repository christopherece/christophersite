from django.db import models

# Create your models here.
class OtherSkill(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    link = models.CharField(max_length=200)

    class Media:
        db_table = 'otherskills'
        
    def __str__(self):
        return self.name