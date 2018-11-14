from django import forms
from django.contrib.auth.models import User
class Registration(forms.ModelForm):
    username=forms.CharField(label='username',max_length=40,required=True)
    password1 = forms.CharField(max_length=32, required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=32, required=True,widget=forms.PasswordInput)
    email_id=forms.CharField(label='email',max_length=200, required=True )
    class Meta:
        model=User
        fields=('username','email_id','password1','password2')
    def clean_username(self):
        user = self.cleaned_data.get('username').lower()
        check = User.objects.filter(username=user)
        if check.count() > 0:
            raise forms.ValidationError(' The username is already in use please choose different one')
        else:
            return user

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('The passwords did not match')
        if not(password1) and not(password2):
            raise forms.ValidationError('Please fill the password fields')
        if len(password1) < 8:
            raise forms.ValidationError('The password must be atleast 8 characters')
        return True

    def clean_email(self):
        # check if the email is unique
        email = self.cleaned_data.get('email')
        check = User.objects.filter(email=email)
        if check.count():
            raise forms.ValidationError('This email already exists')
        return email;

    def save(self):
        #saves the data to database
        user = User.objects.create_user(
        username=self.cleaned_data.get('username'),
        password=self.cleaned_data.get('password1'),
        email=self.cleaned_data.get('email'),
        )
