from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(blank=False, upload_to='project_pics')
    description = models.TextField()
    link = models.URLField(
        max_length=128,
        db_index=True,
        unique=True,
        blank=True
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
