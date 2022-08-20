from django.db import models

from api.lib.utils import name_regex, phone_regex
from api.models.customerGroup import CustomerGroup

class Customer(models.Model):

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=False, validators=[name_regex])
    last_name = models.CharField(max_length=100, null=False, blank=False, validators=[name_regex])
    address = models.TextField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=12, null=False, blank=False, unique=True, validators=[phone_regex])
    email = models.EmailField(unique=True, null=False, blank=False)
    group = models.ForeignKey(CustomerGroup, related_name='group', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = 'Customers'
        app_label="api"