from django.db import models

# Create your models here.
class ptarkalis(models.Model):
    tarkaliname=models.CharField(max_length=30)
    tarkaliprice=models.FloatField()
    tarkalicode=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.tarkaliname
    

