from django import forms
from .models import Write

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['title','body', 'state']