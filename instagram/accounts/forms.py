from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True,
                                       widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'password_confirm', 'first_name', 'last_name', 'email', 'avatar', 'birthday')

    def clean_password_confirm(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError('Пароли не совпадают')
        return cleaned_data['password_confirm']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    

class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if not get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким логином не зарегистрирован!')
        return email
        
    def clean_password(self):   
        email = self.cleaned_data['email']
        user = get_user_model().objects.get(email=email)
        password = self.cleaned_data['password']
        if user and not user.check_password(password):
            raise forms.ValidationError('Неверный пароль!')
        return password
