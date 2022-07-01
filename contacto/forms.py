import email
from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre'}) )
    email = forms.CharField(label='Email',required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
    contenido = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu comentario...'}))