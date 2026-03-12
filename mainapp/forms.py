from django import forms
from  .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'author', 'content', 'image']
        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
           'author': forms.TextInput(attrs={'class': 'form-control'}),
           'content': forms.Textarea(attrs={'class': 'form-control', 'rows':'3'}),
           'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }