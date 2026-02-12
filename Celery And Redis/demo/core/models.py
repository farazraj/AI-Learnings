from django.db import models

# Create your models here.

class Submission(models.Model):
    name = models.CharField(max_length=100)
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {'Done' if self.processed else 'Pending'}"
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    processed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({'Sent' if self.processed else 'Pending'})"

