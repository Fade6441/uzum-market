from django.db.models import CharField, TextChoices
from django.contrib.auth.models import AbstractUser


class UserTypeChoices(TextChoices):
    ADMIN = 'admin', 'Admin'
    OPERATOR = 'operatr', 'Operator'
    REGULATOR = 'regulator', 'Regulator'
    MODERATOR = 'moderator', 'Moderator'

class CustomUser(AbstractUser):
    phone_number = CharField(max_length=20, default='111', blank=True, null=True)
