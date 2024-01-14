from django.db import models

# Create your models here.
class Servers(models.Model):

    STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS, default='active')
    def __str__(self):
        return self.name
    


class ServerTypes(models.Model):
    server = models.ForeignKey(Servers, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name