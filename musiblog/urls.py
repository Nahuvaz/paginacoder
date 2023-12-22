from django.urls import path
from . views import InicioVista, BlogDetailView, AñadirPostView, ActualizarPostView, EliminarPostView, AddCategoryView, CategoryView, AboutMeView, AñadirComentarioView
from django.urls import include


urlpatterns = [
    path('', InicioVista.as_view(), name='inicio'),
    path('detalle/<int:pk>', BlogDetailView.as_view(), name='blog-detalle'),
    path('añadir_post/', AñadirPostView.as_view(), name='añadir_post'),
    path('detalle/editar/<int:pk>', ActualizarPostView.as_view(), name='actualizar_post'),
    path('detalle/<int:pk>/eliminar', EliminarPostView.as_view(), name='eliminar_post'),
    path('añadir_categoria/', AddCategoryView.as_view(), name='añadir_categoria'),
    path('categories/<str:music>/', CategoryView, name='categorias'),
    path('<int:uid>/', include('miembros.urls')),
    path('about_me/ ', AboutMeView.as_view(), name='about_me'),
    path('detalle/<int:pk>/comment/', AñadirComentarioView.as_view(), name='añadir_comentarios'),
    #path('<int:uid>/password/', PasswordsChangeView.as_view())
]
