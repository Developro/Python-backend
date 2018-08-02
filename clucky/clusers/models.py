from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# Эти модели были сгенерированны автоматически. Необходимо всё перепроверить.

ROLES = (('USER', 'USER'),
         ('ADMIN', 'ADMIN')
         )
STATUS = (('ACTIVE', 'ACTIVE'),
          ('DISABLED', 'DISABLED'),
          ('BANNED', 'BANNED')
          )


class UserManager(BaseUserManager):

    def create_user(self, login, email, password=None):
        """
        Creates new user
        :param login: login for user
        :param email: email of user
        :param password: password for that user
        :return: User instance
        """

        if not login:
            raise ValueError('Users must have a login')

        if not email:
            raise ValueError('Users must have an email')

        user = self.model(login=login, email=self.normalize_email(email))

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, login, email, password):

        user = self.create_user(login=login, email=email, password=password)
        user.role = 'ADMIN'

        user.save()

        return user


class User(AbstractBaseUser):
    login = models.CharField(unique=True, max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=64, db_column='password_hash')
    avatar = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=128, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS, default='ACTIVE', null=False)
    role = models.CharField(max_length=5, choices=ROLES, default='USER', null=False)
    access_token_hash = models.CharField(max_length=64, blank=True, null=True)
    acc_action_token_hash = models.CharField(max_length=64, blank=True, null=True)
    refresh_token_hash = models.CharField(max_length=64, blank=True, null=True)
    regstamp = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(db_column='last_visit')

    objects = UserManager

    USERNAME_FIELD = 'login'

    class Meta:
        managed = False
        db_table = 'users'


    def __str__(self):
        return self.login

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.role == 'ADMIN':
            return True
        return False

    @property
    def is_admin(self):
        if self.role == 'ADMIN':
            return True
        return False

    @property
    def is_active(self):
        if self.status == 'ACTIVE':
            return True
        return False



