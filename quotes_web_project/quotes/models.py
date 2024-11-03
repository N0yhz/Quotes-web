from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=70)
    born_date = models.CharField(max_length=70, null=True, blank=True)
    born_location = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.quote