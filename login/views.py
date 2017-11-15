# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from login.models import User
from django.template import loader
from django import forms
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import (
	FormView,RedirectView,CreateView,TemplateView)
from django.contrib.auth import (
	login as auth_login,logout as auth_logout,authenticate,
	update_session_auth_hash)
from passlib.hash import pbkdf2_sha256
from django.forms import ModelForm, TextInput, TextInput, EmailField
# from .forms import UserCreateForm,PasswordRecoveryForm


class LoginForm(ModelForm):
	class Meta:
		model = User
		widgets = {
		'password': forms.PasswordInput(),
		}
		fields = ['user_id', 'password']

def user_login(request, template_name='login/login_form.html'):
	# login = get_object_or_404(Login, pk=pk)
	form = LoginForm(request.POST or None)
	if form.is_valid():
		user_id = request.POST['user_id']
		password = request.POST['password']
		register_ids = User.objects.filter(user_id=user_id)
		if register_ids:
			for register_id in register_ids:
				enc_password = register_id.password
				password = str(password)
				enc_password = str(enc_password)
				# pbkdf2_sha256.using(rounds=1)
				set_password = pbkdf2_sha256.verify(password,enc_password)
				if enc_password :
					return redirect('music_list')
		else:
			messages.error(request,'Wrong password is Wrong')
	return render(request, template_name, {'form': form})

class RegisterForm(ModelForm):
	class Meta:
		model = User
		widgets = {
		'password': forms.PasswordInput(),
		'confirm_password': forms.PasswordInput(),
		'email' : TextInput(attrs={'placeholder': 'Enter the Email ID *','required': False}),
		}
		fields = ['user_id', 'password','confirm_password','email','is_active']


def register_list(request, template_name='login/register_list.html'):
    register = User.objects.all()
    data = {}
    data['all_register'] = register
    return render(request, template_name, data)


def register_create(request, template_name='login/register_form.html'):
	form = RegisterForm(request.POST or None)
	if request.method == 'POST':
		user_id =request.POST['user_id']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		email = request.POST['email']
		is_active = request.POST['is_active']
		if password == confirm_password:
			enc_password = pbkdf2_sha256.encrypt('password',rounds=29000,salt_size=32)
			User.objects.create(
				user_id = user_id,
				password = enc_password,
				confirm_password = enc_password,
				email = email,
				is_active = is_active
				)
			# form.save()
			return redirect('register_list')
		else:
			# messages.error(request,'Password and Confirm Password is not match')
			return render(request, template_name, {
				'form': form,
				'error_message':'Password and Confirm Password is not matchsss',
				})
	return render(request, template_name, {'form': form})


def register_update(request, pk, template_name='login/register_form.html'):
    register = get_object_or_404(User, pk=pk)
    form = RegisterForm(request.POST or None, instance=register)
    if form.is_valid():
        form.save()
        return redirect('register_list')
    return render(request, template_name, {'form': form})


def register_delete(request, pk, template_name='login/register_confirm_delete.html'):
    register = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        register.delete()
        return redirect('register_list')
    return render(request, template_name, {'object': register})