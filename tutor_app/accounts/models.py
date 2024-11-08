from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('ta', 'Teaching Assistant'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Resolve conflicts with Django's default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

class TAInfo(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    class_tutoring = models.CharField(max_length=100)
    times_available = models.CharField(max_length=100)
    days_available = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.class_tutoring}"