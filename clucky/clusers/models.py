from django.db import models

# Create your models here.

# Эти модели были сгенерированны автоматически. Необходимо всё перепроверить.

class Users(models.Model):
    login = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=64)
    access_token_hash = models.CharField(max_length=64, blank=True, null=True)
    acc_action_token_hash = models.CharField(max_length=64, blank=True, null=True)
    refresh_token_hash = models.CharField(max_length=64, blank=True, null=True)
    status = models.CharField(max_length=8)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'