from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,AbstractUser

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, Nom, prenom, email, telephone, adresse, is_admin, is_cadre, is_chef_dep, is_sous_dir,is_content_admin, password):
        """
        Creates and saves a User with the given data
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            adresse=adresse,
            telephone=telephone,
            Nom=Nom,
            prenom=prenom,
            is_admin=is_admin,
            is_cadre=is_cadre,
            is_chef_dep=is_chef_dep,
            is_sous_dir=is_sous_dir,
            is_content_admin=is_content_admin
        )

        user.set_password(password)
        user.save(using=self._db)
        print(user.email)
        return user

    def create_superuser(self, Nom, prenom, email, telephone, adresse, is_admin, is_cadre, is_chef_dep, is_sous_dir,is_content_admin, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(password=password,
                                email=self.normalize_email(email),
                                adresse=adresse,
                                telephone=telephone,
                                Nom=Nom,
                                prenom=prenom,
                                is_admin=is_admin,
                                is_cadre=is_cadre,
                                is_chef_dep=is_chef_dep,
                                is_sous_dir=is_sous_dir,
                                is_content_admin=is_content_admin
                                )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class Meta:
        db_table = 'auth_user'

    objects = MyUserManager()
    username = None
    Nom = models.CharField(max_length=50, default="user")
    prenom = models.CharField(max_length=50, default="prenom")
    email = models.EmailField('email address', unique=True)
    telephone = models.CharField(max_length=255, default="tel")
    adresse = models.CharField(max_length=255, default="adresse")
    is_admin = models.BooleanField('admin status', default=False)
    is_cadre = models.BooleanField('Cadre status', default=False)
    is_chef_dep = models.BooleanField('Chef Departement status', default=False)
    is_sous_dir = models.BooleanField('Sous Directeur status', default=False)
    is_content_admin = models.BooleanField('Content admin status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['Nom', 'prenom', 'telephone', 'adresse', 'is_admin','is_cadre', 'is_chef_dep', 'is_sous_dir', 'is_content_admin']

    def __str__(self):
        return self.email
