from django.db import models

class CustomerGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'CustomerGroups'
        app_label="api"