from django.urls  import reverse
from django.db import models

# Create your models here.	
class student(models.Model):
		name = models.CharField(max_length=100)
		fathername = models.CharField(max_length=100)
		classname = models.IntegerField()
		contact = models.CharField(max_length=100)
class Teacher(models.Model):
	name = models.CharField(max_length=100)
	exp = models.IntegerField()
	subject =models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
def get_absolute_url(self):
	return reverse('listteacher')
def get_absolute_url(self):
	return reverse('listteacher',kwargs={'pk':self.pk})
