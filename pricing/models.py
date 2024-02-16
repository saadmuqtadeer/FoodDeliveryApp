# models.pyS
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description} ({self.type})"

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.IntegerField()
    km_price = models.DecimalField(max_digits=6, decimal_places=2)
    fix_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Pricing for {self.item} in {self.zone} zone by {self.organization}"
