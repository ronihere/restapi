from django.db import models

# Create your models here.
class Product1(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=20,blank=False)
    prod_url = models.URLField(max_length=300,blank=False)
    prod_desc = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"{self.prod_name} : Id ---> {self.prod_id}"
    

class Product2(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=20,blank=False)
    prod_url = models.URLField(max_length=300,blank=False)
    prod_desc = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"{self.prod_name} : Id ---> {self.prod_id}"


class Product3(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=20,blank=False)
    prod_url = models.URLField(max_length=300,blank=False)
    prod_desc = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"{self.prod_name} : Id ---> {self.prod_id}"


class Product4(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=20,blank=False)
    prod_url = models.URLField(max_length=300,blank=False)
    prod_desc = models.CharField(max_length=200,blank=False)
    def __str__(self):
        return f"{self.prod_name} : Id ---> {self.prod_id}"
    