from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,ProfileLink,Contact

class userRegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username' : forms.TextInput(attrs={'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Your Email'}),
            
        }

class updateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields='__all__'
        exclude=('user',)

class addLinksForm(forms.ModelForm):
    class Meta:
        model=ProfileLink
        fields='__all__'
        exclude=('user',)
        widgets={
            'link_name':forms.TextInput(attrs={'class':"form-control", 'placeholder':'Link Name'}),
            'link':forms.TextInput(attrs={'class':"form-control", 'placeholder':'Link/Http adress'}),
        }
        

class editProfileLinkForm(forms.ModelForm):
    class Meta:
        model=ProfileLink
        fields='__all__'
        
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
        exclude=('created',)
        widgets={
            'name': forms.TextInput(attrs={'placeholder':'Your Name'}),
            'surname': forms.TextInput(attrs={'placeholder':'Your Surname'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email'}),
            'summary': forms.Select(attrs={'placeholder':'Choose Topic'}),
            'topic': forms.Textarea(attrs={'placeholder':'Write your issue here'})

        }        



