# -*-coding:utf-8-*-
from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .forms import utilisateurForm, connexionForm, EditionProfil, DocumentForm, PostForm
from django.contrib.auth.models import User
from .models import utilisateur, Profil, Document, Post
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import auth
from django.core.files import File
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Create your views here.

def index(request):
    return render(request, 'doafrica/index.html')


def signin(request):
    if request.method == "POST":
        form = utilisateurForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            lastname = form.cleaned_data["last_name"]
            country = form.cleaned_data["country"]
            telephone = form.cleaned_data["telephone"]
            address = form.cleaned_data["address"]
            account = form.cleaned_data["account"]
            form = Profil.objects.create_user(username=username, password=password, email=email, last_name=lastname,
                                              country=country, telephone=telephone, address=address, account=account,
                                              register_date=timezone.now())
            form.save()
            return redirect('photo')
    else:
        form = utilisateurForm()
        return render(request, 'doafrica/signin.html', {'form': form})


def conlogin(request):
    error = False

    if request.method == "POST":
        form = connexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user is not None:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return redirect('profil')
            else:  # sinon une erreur sera affichée
                error = True
    else:
        form = connexionForm()
        return render(request, 'doafrica/login.html', {'form': form})


def edit_profil(request):
    if request.method == "POST":
        form = EditionProfil(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            lastname = form.cleaned_data["last_name"]
            country = form.cleaned_data["country"]
            telephone = form.cleaned_data["telephone"]
            address = form.cleaned_data["address"]
            account = form.cleaned_data["account"]
    else:
        form = EditionProfil()
        return render(request, 'doafrica/edit_profil.html', {'form': form})


def profil(request):
    """ view charger du profil utilisateur"""

    if request.user.is_authenticated():
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = Post()
                post.titre = form.cleaned_data["titre"]
                post.message = form.cleaned_data["message"]
                post.montant = form.cleaned_data["montant"]
                post.categorie = form.cleaned_data["categorie"]
                post.image = form.cleaned_data["image"]
                post.save()
                return redirect('profil')
        else:
            context={
                'form':PostForm,
                'donnee':Profil.objects.get(user_id=request.user.id),
                #'telephone':Profil.objects.get(user_id=request.user.id),
            }
            return render_to_response("doafrica/profil.html",
                                      context,
                                      context_instance=RequestContext(request))
    else:
        return render(request, 'doafrica/login_error.html')


def conlogout(request):
    logout(request)
    return redirect('conlogin')


def photo(request):
    profil = Profil.objects.latest('user_id')

    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            profil.photo = request.FILES['photo']
            profil.id_card = request.FILES['id_card']
            profil.business_card = request.FILES['business_card']
            profil.save()
            return redirect('profil')
    else:
        form = DocumentForm()
        return render(request, 'doafrica/photo.html', {'form': form})


def association(request):
    """view gerant l'affichage et la creation d'association"""
    if request.user.is_authenticated():
        context={
                'form':PostForm,
                'donnee':Profil.objects.get(user_id=request.user.id),

            }
        return render_to_response("doafrica/asso.html",
                                      context,
                                      context_instance=RequestContext(request))
    else:
        return render(request, 'doafrica/login_error.html')





def sample(request):
    current_user = request.user
    print current_user.id


def admin(request):
    context={
        'users': User.objects.all(),
    }
    return render_to_response("doafrica/admin.html",
                              context,
                              context_instance=RequestContext(request))
