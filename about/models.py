from django.db import models
from datetime import datetime
# Create your models here.
class Testimonial(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='tesmon_images', default='default.png')
	carrier = models.CharField(max_length=100)
	desc = models.TextField()

	def __str__(self):
		return self.name

class About_Us(models.Model):
	title = models.CharField(max_length=100)
	desc = models.TextField()
	happy_customers = models.CharField(max_length=100)
	branches = models.CharField(max_length=100)
	partners = models.CharField(max_length=100)
	awards = models.CharField(max_length=100)
	updated_on = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return self.title

	class Meta:

		verbose_name_plural = 'About Us'
