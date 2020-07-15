from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    # featured    = models.BooleanField(default=False) # null=True, default=True

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view')
        
    def get_success_url(self):
        return reverse('view')
