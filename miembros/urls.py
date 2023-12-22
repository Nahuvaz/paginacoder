from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, MostrarPerfilView, EditarPaginaPerfilView, CrearPerfilPageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('editar_perfil/', UserEditView.as_view(), name='editar_perfil'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/cambiar_contraseña.html')),
    path('password_exitosa/ ', views.password_exitosa, name='password_exitosa'),
    path('<int:pk>/perfil/ ', MostrarPerfilView.as_view(), name='usuario_perfil'),
    path('<int:pk>/editar_perfil_pagina ', EditarPaginaPerfilView.as_view(), name='editar_perfil_pagina'),
    path('crear_perfil_pagina/ ', CrearPerfilPageView.as_view(), name='crear_perfil_pagina'),
]
