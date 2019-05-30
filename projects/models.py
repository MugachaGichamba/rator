from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


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

    def get_absolute_url(self):
        return reverse('home')


class Rating(models.Model):
    content = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
    design = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
    usability = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)], default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('home')

