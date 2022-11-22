from django import forms

class crear_consolas(forms.Form):

    nombre_consola = forms.CharField(max_length=50)
    marca_consola = forms.CharField(max_length=50)
    precio_consola = forms.IntegerField()

class crear_accesorios(forms.Form):

    nombre_accesorio = forms.CharField(max_length=50)
    tipo_accesorio = forms.CharField(max_length=50)