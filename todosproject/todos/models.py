from uuid import uuid4
from django.db import models


class Users(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday = models.DateField()
    email = models.CharField(max_length=64, unique=True)
