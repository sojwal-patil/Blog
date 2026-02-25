from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from django_countries.fields import CountryField 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=15,label="",widget=forms.TextInput(attrs={"class":"input register_form_input w-[350px]" ,"placeholder":"Enter Username"}))

    password = forms.CharField(max_length=20,label="",widget=forms.PasswordInput(attrs={"class":"input register_form_input w-[350px]","placeholder":"Enter Password"}))   


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=10,label="",widget=forms.TextInput(attrs={"class":"input register_form_input w-[350px]","placeholder":"Enter First Name"}))

    last_name = forms.CharField(max_length=10,label="",widget=forms.TextInput(attrs={"class":"input register_form_input w-[350px]","placeholder":"Enter Last Name"}))

    username = forms.CharField(max_length=15,label="",widget=forms.TextInput(attrs={"class":"input register_form_input w-[350px]" ,"placeholder":"Choose a Unique Username"}))

    password = forms.CharField(max_length=20,label="",widget=forms.PasswordInput(attrs={"class":"input register_form_input w-[350px]","placeholder":"Choose a Strong Password"}))

    country = CountryField().formfield(label="",widget=forms.Select(attrs={"class":"select register_form_input w-[350px]"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["country"].choices = [("", "Select your country")] + list(self.fields["country"].choices)[1:]


class SearchForm(forms.Form):
    search_title = forms.CharField(max_length=50,label="",widget=forms.TextInput(attrs={"class":"input w-full mt-10","placeholder":"Search..."}))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content" , "category"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "input input-bordered w-[80%]", 
                "placeholder": "Enter Title"
            }),
            "content": CKEditorWidget(attrs={
                "style": "width: 100%;", # Use 'style' for width, or config below
            }),
            "category" : forms.Select(attrs={
                "class" : "input select w-min"
            })
        }