from django.db import models

class Product(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=1)
	in_stock = models.BooleanField(default=True)
