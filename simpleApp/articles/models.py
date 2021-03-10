from django.db import models

# Create your models here.


class Article(models.Model):
	title = models.CharField(max_length=100) 
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	# On creating a new article, the new date will be automatically
	# set to now
	# Add author later
	# Add thumbnail later
	
	def __str__(self):
		return self.title
