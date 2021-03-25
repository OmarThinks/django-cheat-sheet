from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(max_length=100)
	in_stock = models.BooleanField(default=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, 
		null=False, blank=False, default=1)
