from django import forms

class ComentarioFormulario(forms.Form):
    descripcion=forms.CharField(max_length=100,label="Comentario",widget=forms.Textarea)
    