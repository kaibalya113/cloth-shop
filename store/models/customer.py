from django.db import models
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=500)

    def register(self):
        self.save()