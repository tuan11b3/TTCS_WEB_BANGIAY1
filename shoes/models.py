from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    details = models.CharField(max_length=300, null=True) # about 50 words
    price_group_id = models.PositiveSmallIntegerField(null=True)
    pmaterial_type_id = models.PositiveSmallIntegerField(null=True)
    ptype_id = models.PositiveSmallIntegerField(null=True)
    pstate_id = models.PositiveSmallIntegerField(null=True)
    gender_id = models.PositiveSmallIntegerField(null=True)
    brand_id = models.PositiveSmallIntegerField(null=True)

    class Meta: 
        permissions = [
            ('special_status', 'Can see all products'),
        ]

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shoe_detail', args=[str(self.id)])