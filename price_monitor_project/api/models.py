from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)
    is_active = models.BooleanField(null=False, default=True)
    number_of_followers = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

