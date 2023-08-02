from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin,)
# Create your models here.


class UserManager(BaseUserManager):
    """manager for users"""

    def create_user(self, email, passowrd=None, **extra_field):
        """Create,save and return new user"""
        user = self.model(email=email, **extra_field)
        user.set_password(passowrd)
        user.save(using=self._db)
        return user


class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager

    USERNAME_FIELD = 'email'
