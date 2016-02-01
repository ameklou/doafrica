from django import forms
from models import Profil, Document, Post, Groupe
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea

class utilisateurForm(forms.ModelForm):
	class Meta:
		model=Profil
		fields=('username','last_name','email','password','telephone','country', 'address','account',)
		widgets={
			'username': forms.TextInput(attrs={'class': 'md-input'}),
			'last_name': forms.TextInput(attrs={'class': 'md-input'}),
			'email': forms.TextInput(attrs={'class': 'md-input'}),
			'password': forms.PasswordInput(attrs={'class': 'md-input'}),
			'telephone': forms.TextInput(attrs={'class': 'md-input'}),
			'country': forms.TextInput(attrs={'class': 'md-input'}),
			'address': forms.TextInput(attrs={'class': 'md-input'}),
			'account': forms.Select(attrs={'class': 'md-input'}),
			



		}
class connexionForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'md-input'}), max_length=30, label=u"username")
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'md-input'}), label=u"password")
    


class EditionProfil(forms.ModelForm):
	class Meta:
		model=Profil
		fields=('username','last_name','email','telephone','country', 'address','biography','slug','twitter','facebook','linkedin','first_name',)
		widgets={
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'telephone': forms.TextInput(attrs={'class': 'form-control'}),
			'country': forms.TextInput(attrs={'class': 'form-control'}),
			'address': forms.TextInput(attrs={'class': 'form-control'}),
			'biography': forms.Textarea(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'twitter': forms.TextInput(attrs={'class': 'form-control'}),
			'facebook': forms.TextInput(attrs={'class' : 'form-control'}),
			'linkedin': forms.TextInput(attrs={'class' : 'form-control'}),

			}



class DocumentForm(forms.ModelForm):
	class Meta:
		model=Profil
		fields=('photo','id_card','business_card',)
		widgets={
			'photo': forms.FileInput(attrs={'class': 'filestyle', 'data-buttonName': 'btn-success'}),
			'id_card': forms.FileInput(attrs={'class': 'filestyle', 'data-buttonName': 'btn-success'}),
			'business_card': forms.FileInput(attrs={'class': 'filestyle', 'data-buttonName': 'btn-success'}),
		}


class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('titre','message','montant','categorie','image',)
		widgets={
			'titre': forms.TextInput({'class': 'form-control'}),
			'message': forms.Textarea({'class': 'form-control'}),
			'montant': forms.TextInput({'class': 'form-control'}),
			'categorie': forms.Select({'class': 'form-control'}),
			'image': forms.FileInput({'class': 'filestyle', 'data-buttonName': 'btn-success'}),

		}

class AssoForm(forms.ModelForm):
    class Meta:
        model=Groupe
        fields=('name','description','image',)
        widgets={
            'name':forms.TextInput({'class':'form-control'}),
            'description': forms.Textarea({'class': 'form-control'}),
            'image':forms.FileInput({'class':'filestyle', 'data-buttonName': 'btn-success'}),
        }