from uuid import uuid4
from django.db import models


class Users(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Project(models.Model):
    project_name = models.CharField(max_length=64)
    users = models.ManyToManyField(Users)


class Task_TODO(models.Model):
    task_text = models.TextField()
    task_enable = models.BooleanField(default=True)
    user = models.ForeignKey(Users, models.PROTECT)

