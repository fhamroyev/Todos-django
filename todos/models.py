from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=7)
    delete_icon = models.ImageField(default='delete-icon-image-15.jpg')
    edit_icon = models.ImageField(default='edit-icon-images-26.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
