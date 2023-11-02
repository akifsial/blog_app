from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import Post


class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2=forms.CharField(label="Again Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields=['username','first_name','email']
        labels={'username':'Username','first_name':'Full Name'}

        widgets={"username":forms.TextInput(attrs={'class':'form-control'}),
                "first_name":forms.TextInput(attrs={'class':'form-control'}),
                "last_name":forms.TextInput(attrs={'class':'form-control'}),
                "email":forms.TextInput(attrs={'class':'form-control'}),
                "password1":forms.TextInput(attrs={'class':'form-control'})}
        

class LoginForm(AuthenticationForm):
    # password1=forms.CharField(label="Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))

    # password2=forms.CharField(label="Again Password" , widget=forms.PasswordInput(attrs={'class':'form-control'}))

        username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
        password=forms.CharField(label=('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

   
class PostForm(forms.ModelForm):
     
     class Meta:
          model=Post
          fields=['title','desc']

          widgets={"title":forms.TextInput(attrs={'class':'form-control'}),
                "desc":forms.TextInput(attrs={'class':'form-control'}),
                }
           

# class PostForm(forms.Form):
#      class Meta:
#           model=Post
#           fields=['title','desc']
#           label_tags={'title':'Title','desc':'Description'}