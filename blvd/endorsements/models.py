from django.db import models

class Endorsement(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    testimonial = models.TextField()
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name
