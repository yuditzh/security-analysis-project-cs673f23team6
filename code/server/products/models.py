from django.db import models
from django.conf import settings

from account import models as account_models

class Product(models.Model):
	LOCATION_CHOICES = [
		("brighton", "Brighton"),
		("allston", "Allston"),
		("cambridge", "Cambridge"),
		("commonwealth-avenue", "Commonwealth Avenue"),
		("huntington-avenue", "Huntington Avenue"),
		("seaport", "Seaport"),
		("downtown", "Downtown"),
		("brookline", "Brookline"),
		("fenway", "Fenway"),
		("backbay", "Backbay"),
		("boylston", "Boylston"),
		("kenmore", "Kenmore"),
	]
	CATEGORY_CHOICES = {
		("books", "Books"),
		("notes", "Notes"),
		("furniture", "House Furniture & Appliances"),
		("others", "Others"),
	}

	user = models.UUIDField()
	title = models.TextField()
	description = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	price = models.TextField(default='0')
	location = models.TextField(choices=LOCATION_CHOICES)
	category = models.TextField(choices=CATEGORY_CHOICES)

	class Meta:
		db_table = 'products'