from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """A class to represent a profile of user

    Attributes:
        user (obj): User linked to the profile
        favorite_city (str): Favorite city of the user

    Methods:
          __str__: display username of the user when str() is called
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
