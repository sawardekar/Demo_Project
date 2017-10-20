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
		for register_id in register_ids:
			set_password =register_id.password
			if set_password == password :
				return redirect('music_list')
	return render(request, template_name, {'form': form})

class RegisterForm(ModelForm):
	class Meta:
		model = User
		widgets = {
		'password': forms.PasswordInput(),
		'confirm_password': forms.PasswordInput(),
		}
		fields = ['user_id', 'password','confirm_password','email','is_active']


def register_list(request, template_name='login/register_list.html'):
    register = User.objects.all()
    data = {}
    data['all_register'] = register
    return render(request, template_name, data)


def register_create(request, template_name='login/register_form.html'):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('register_list')
    return render(request, template_name, {'form': form})


def register_update(request, pk, template_name='login/register_form.html'):
    register = get_object_or_404(User, pk=pk)
    form = RegisterForm(request.POST or None, instance=song)
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