from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['done']

    def __str__(self):
        return self.content
