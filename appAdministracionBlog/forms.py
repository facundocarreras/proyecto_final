from django import forms


class cursoFormulario(forms.form):

    name = forms.CharField()
    apellido = forms.CharField()
    fecha_creacion = forms.DateField()
    
