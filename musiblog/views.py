from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Categories, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View

class AboutMeView(View):
    def get(self, request):
        return render(request, 'about_me.html')

class InicioVista(ListView):
    model = Post
    template_name = 'inicio.html'
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_detalles.html'
    
class AñadirPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'añadir_post.html'
    
    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
class AñadirComentarioView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'añadir_comentarios.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
class AddCategoryView(CreateView):
    model = Categories
    template_name = 'añadir_categoria.html'
    fields = '__all__'
    
class ActualizarPostView(UpdateView):
    model = Post
    template_name = 'actualizar_post.html'
    fields = ['titulo', 'titulo_tag', 'body']
    
class EliminarPostView(DeleteView):
    model = Post
    template_name = 'eliminar_post.html'
    success_url = reverse_lazy('inicio')
    
def CategoryView(request, music):
    category_posts = Post.objects.filter(category=music)
    return render(request, 'categorias.html', {'music':music, 'category_posts':category_posts})