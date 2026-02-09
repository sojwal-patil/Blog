from django import forms
from . import models

class AuthorForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"input"}))
    username = forms.CharField(max_length=25,widget=forms.TextInput(attrs={"class":"input"}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={"type":"date","class":"input dateofbirth-class"}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = ["title","category","contains"]
        widgets = {
            "title" : forms.TextInput(attrs={"class":"input","placeholder":"Enter Title"}),
            "category" : forms.Select(attrs={"class":"select"}),
            "contains" : forms.Textarea(attrs={"class":"input post-text-area","placeholder":"Start Typing"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields.values():
            f.label = None
