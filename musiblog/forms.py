from django import forms
from .models import Post, Categories, Comment

choices = Categories.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'category', 'body', 'subtitle', 'header_image')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control'}),

        }
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'titulo_tag', 'body', 'subtitle')
        
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'subtitle': forms.Textarea(attrs={'class': 'form-control'}),

        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }