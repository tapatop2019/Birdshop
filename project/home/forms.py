from django import forms
#В этом файле создаются именно поля связанные с формами
class AddPostForm(forms.Form):
    komentari=forms.CharField(max_length=100, widget=forms.Textarea())
    photo=forms.ImageField(required=False)# required=False поле необязательно вводить
