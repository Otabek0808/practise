from django import forms

from app1.models import Programms


class ProgrammAddForm(forms.Form):
    class Meta:
        model = Programms
        fields = ['category', 'name','summary','download_link', 'image']