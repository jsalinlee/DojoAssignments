from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Manager
class UserManager(models.Manager):
    def validation(self, email):
        if EMAIL_REGEX.match(email):
            return True
        else:
            return False

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    userManager = UserManager()
