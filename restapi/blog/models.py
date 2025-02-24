from django.db import models

# Create your models here.

#Define the custom user manager:

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin #Define user model


class CustomerUserManager(BaseUserManager): #class inherit's from BaseUserManager
    #pass
    #"""docstring for ."""

    def create_user(self,email,first_name,last_name,extra_fields,password=None):  #Manager contain's helper functions/methods create_user & create_superuser
        if not email:
            raise ValueError("The Email field is required")
            email = self.normalize_email(email)
            user = self.model(email=email,first_name=first_name,last_name=last_name,**extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

        def create_superuser(self,email,first_name,last_name,password=None,**extra_fields):
            extra_fields.setdefault('is_staff',True)
            extra_fields.setdefault('is_superuser',True)
            if extra_fields.get('is_staff') is not true:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
               raise ValueError('Superuser must have is_superuser=True.')
            #    pass
            return self.create_user(email,first_name,last_name,extra_fields,password)

#Define the `User` model:
class CustomUser(AbstractBaseUser,PermissionsMixin): #Customer user model
    #"""docstring for ."""
     email = models.EmailField(unique=True)
     first_name = models.CharField(max_length=30,blank=True)
     last_name = models.CharField(max_length=30,blank=True)
     is_active = models.BooleanField(default=True)
     is_staff = models.BooleanField(default=False)

#    objects = UserManager()
     USERNAME_FIELD = 'email'
     #REQUIRED_FIELDS['first_name','last_name']

     objects=CustomerUserManager()

     def __str__(self):
         return self.email
