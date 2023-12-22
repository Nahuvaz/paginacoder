from typing import Any
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import SignUpForm, EditProfileForm, PaginaPerfilForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from musiblog.models import Perfil

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_exitosa')

def password_exitosa(request):
    return render(request, 'registration/password_exitosa.html', {})

class MostrarPerfilView(DetailView):
    model = Perfil
    template_name = 'registration/usuario_perfil.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(MostrarPerfilView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Perfil, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context
    
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editar_perfil.html'
    success_url = reverse_lazy('inicio')
    
    def get_object(self):
        return self.request.user
    
class EditarPaginaPerfilView(generic.UpdateView):
    model = Perfil
    template_name = 'registration/editar_perfil_pagina.html'
    fields = ['bio', 'imagen_perfil']
    success_url = reverse_lazy('inicio')
    
class CrearPerfilPageView(CreateView):
    model = Perfil
    form_class = PaginaPerfilForm
    template_name = 'registration/crear_perfil_pagina.html'
    #fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    