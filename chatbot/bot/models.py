from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    useremail = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return f"{self.user_name} \n {self.user_email}"

class SupportTicket(models.Model):
    support_ticket = models.CharField(max_length=100)

    def __str__(self):
        return self.support_ticket