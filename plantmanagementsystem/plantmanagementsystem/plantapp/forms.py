from django import forms
from .models import Plant

class Plantform(forms.ModelForm):
    class Meta:
        model=Plant
        fields=['profile','pid','pname','pfamily','psoiltype','pheight','pror','possiblediseases']