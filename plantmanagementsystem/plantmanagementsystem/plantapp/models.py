from django.db import models

# Create your models here.
class Plant(models.Model):

    profile=models.ImageField(upload_to='profile_images/',null=True)
    pid=models.AutoField(primary_key=True)
    pname=models.CharField(max_length=50)
    pfamily=models.CharField(max_length=50,null=True)
    psoiltype=models.CharField(max_length=50,null=True)
    pheight=models.IntegerField()
    pror=models.CharField(max_length=50,null=True)
    possiblediseases=models.CharField(max_length=200)

    def  __str__(self):
        return self.pname