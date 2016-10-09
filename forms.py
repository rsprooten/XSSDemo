from django.forms import ModelForm
from .models import levelEen

class AuthorForm(ModelForm):
    class Meta:
        model = levelEen
        fields = '__all__'