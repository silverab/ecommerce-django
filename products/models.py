from django.db import models

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(null=True, blank=True)
	price = models.DecimalField(max_digits=100, decimal_places=2, default=29.89)
	sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
	slug = models.SlugField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.title)


class ProductImage(models.Model):
	Product = models.ForeignKey(Product, on_delete=models.CASCADE)
	image = models.ImageField(null=True, blank=True)
	featured = models.BooleanField(default=False)
	thumbnail = models.BooleanField(default=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.Product.title