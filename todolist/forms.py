from django import forms

class TaskBaru(forms.Form):
    judul = forms.CharField(label='Judul', max_length=100)
    deskripsi = forms.CharField(label='Deskripsi', max_length=100)
