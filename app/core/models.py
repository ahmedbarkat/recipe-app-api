from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
class UserManger(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email Must BE SET.")
        user = self.model(email=self.normalize_email(email),**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        

        
class ActiveUserManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
       
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManger()
    active = ActiveUserManger()


    USERNAME_FIELD = 'email'
    UINQUE_FIELDS = ['email']


class Reciepe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=False)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    order = models.IntegerField(default=0, blank=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'reciepes'
        ordering = ['order']

