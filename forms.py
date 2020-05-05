from django import forms
from .models import Blog


class Blogform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body','image']