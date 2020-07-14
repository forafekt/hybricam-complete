from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    edited = forms.BooleanField(
        widget=forms.HiddenInput(), required=False, initial=False
    )
    image = forms.ImageField(required=False)
    content = forms.Textarea()

    class Meta:
        model = Article
        fields = ["title", "content", "image", "tags", "status", "edited"]
