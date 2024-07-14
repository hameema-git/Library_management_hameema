from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
    

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

class SignUpForm(UserCreationForm):
        first_name=forms.CharField(max_length=50)
        last_name=forms.CharField(max_length=50)
        email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
        age=forms.IntegerField()
    
        class Meta:
            model = User
            fields = ['first_name','last_name','username','age' ,'email', 'password1', 'password2']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
            self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter'})
            self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter'})
            self.fields['username'].help_text=""
            self.fields['age'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Age'})
            self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
            self.fields['password1'].help_text ='<span style="color:yellow;font-size:15px;">(Must contain atleast 8 characters long and contain a mix of letters and numbers.)</span>'
            self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})
            self.fields['password2'].help_text = '<span style="color:yellow;font-size:15px;">(Re-enter the same password)</span>'
            self.fields['password2'].label='Confirm password'