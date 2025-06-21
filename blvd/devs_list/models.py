from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    company = models.CharField(max_length=100)
    linkedin_url = models.URLField()

    def __str__(self):
        return self.name
