from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
class MyAccuntManager(BaseUserManager):
    def create_user(self,firstname,lastname,email,mobile,username,password=None):
        if not email:
            raise ValueError("User Must have an Email ID")
        if not username:
            raise ValueError("User name is Mandatory")
        if not mobile:
            raise ValueError("User should have a Mobile No")
        user=Account.objects.create(
        firstname=firstname,
        lastname=lastname,
        email=self.normalize_email(email),
        username=username,
        mobile=mobile,

        )
        user.set_password(password)
        user.save(using= self._db)
        return user
    def create_superuser(self,firstname,lastname,email,mobile,username,password):
        user=self.create_user(
        firstname=firstname,
        lastname=lastname,
        email=self.normalize_email(email),
        username=username,
        mobile=mobile,
        password=password,
        )
        is_admin=True
        is_active=True
        is_staff=True
        is_superuser=True
        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    mobile=models.CharField(max_length=12)
    #requird
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    last_login=models.DateTimeField(auto_now_add=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS=['firstname','lastname','username','mobile']
    USERNAME_FIELD='email'
    objects=MyAccuntManager()
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def full_name(self):
        return f'{self.firstname}{self.lastname}'
    def has_module_perms(self,add_label):
        return True
