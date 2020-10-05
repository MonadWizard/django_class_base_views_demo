from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())







