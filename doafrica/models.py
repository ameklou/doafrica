from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class utilisateur(models.Model):
	""" Model pour l'enregistrement des utilisateurs sur le site"""
	account_choice=(
		('A','Entrepreneur'),
		('B','Cabinet'),
		('C','Investisseur'),
		)
	premium_choice=(
		('A','Free'),
		('B','Argent'),
		('C','Gold'),
		)
	username=models.CharField(max_length=30)
	lastname=models.CharField(max_length=50)
	firstname=models.CharField(max_length=50)
	email=models.EmailField()
	password=models.CharField(max_length=255)
	telephone=models.IntegerField()
	country=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	biography=models.TextField()
	slug=models.SlugField(max_length=100)
	twitter=models.CharField(max_length=255)
	facebook=models.CharField(max_length=255)
	linkedin=models.CharField(max_length=255)
	photo=models.ImageField(max_length=255)
	account=models.CharField(max_length=1, choices=account_choice)
	activated=models.CharField(max_length=5, null=True)
	active=models.CharField(max_length=5, null=True)
	premium=models.CharField(max_length=1, choices=premium_choice)
	register_date=models.DateField(auto_now_add=True)
	id_card=models.ImageField(max_length=255)
	business_card=models.ImageField(max_length=255)

	def __str__(self):
		return self.username


class Profil(User):
	""" model utilisateurs"""
	account_choice=(
		('A','Entrepreneur'),
		('B','Cabinet'),
		('C','Investisseur'),
		)
	premium_choice=(
		('A','Free'),
		('B','Argent'),
		('C','Gold'),
		)
	user= models.OneToOneField(User)
	telephone=models.IntegerField(null=True)
	country=models.CharField(max_length=50)
	address=models.CharField(max_length=50)
	biography=models.TextField()
	slug=models.SlugField(max_length=100)
	twitter=models.CharField(max_length=255)
	facebook=models.CharField(max_length=255)
	linkedin=models.CharField(max_length=255)
	photo=models.ImageField(upload_to="photo/")
	account=models.CharField(max_length=1, choices=account_choice)
	activated=models.CharField(max_length=5, null=True)
	active=models.CharField(max_length=5, null=True)
	premium=models.CharField(max_length=1, choices=premium_choice)
	register_date=models.DateField(auto_now_add=True)
	id_card=models.ImageField(upload_to="photo/")
	business_card=models.ImageField(upload_to="photo/")

	def __str__(self):
		return self.user.username    	





class Post(models.Model):
	""" model pour la publication de """
	secteur_choice=(
		('A','commercial'),
		('B','agricole'),
		('C','service'),
		('D','social'),
		)
	author=models.ForeignKey(User)
	titre=models.CharField(max_length=255)
	message=models.TextField()
	date_de_pub=models.DateField(auto_now_add=True)
	montant=models.IntegerField()
	categorie=models.CharField(max_length=1, choices=secteur_choice)
	image=models.ImageField(upload_to="projet")
	recolte=models.IntegerField(null=True)
	valide=models.CharField(max_length=5, null=True)


class Document(models.Model):
	docfile = models.FileField(upload_to='documents/')

class Groupe(models.Model):
    """ Model gerant les groupes d'utilisateurs"""
    name=models.CharField(max_length=255)
    description=models.TextField()
    author=models.ForeignKey(User)
    image=models.ImageField(upload_to="groupe")

class GroupePost(models.Model):
    """Model gerant les publications ds les groupes """
    groupe=models.ForeignKey(Groupe)
    message=models.TextField()
    image=models.ImageField()
    publication=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User)


class GroupeMember(models.Model):
    """ model gerant les membres d'un groupe
    """
    membre=models.ForeignKey(User)
    groupe=models.ForeignKey(Groupe)