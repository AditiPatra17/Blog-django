from django.contrib.auth.models import AbstractUser, UserManager as DefaultUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserManager(DefaultUserManager):
    def managers(self):
        return self.filter(is_manager=True)

class User(AbstractUser):
    # Add any custom user fields here
    picture = models.ImageField(upload_to='media/', default='default.png', null=True)
    is_manager = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Add related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_set'  # Add a related_name here
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set'  # Add a related_name here
    )

    def __str__(self):
        return self.username
