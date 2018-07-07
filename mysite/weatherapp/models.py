from django.db import models

# Create your models here.
class City(models.Model):
	name = models.CharField(max_length = 25)  # City Name in sqlite3 database!

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'cities'  #Show verbose name on admin dashboard!

			
