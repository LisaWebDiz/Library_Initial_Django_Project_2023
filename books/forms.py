import re

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'pages_quantity', 'price', 'cover_type', 'size', 'photo', 'exist']

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'floatingInput',
                    'placeholder': "Наименование книги"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Описание"
                }
            ),
            'pages_quantity': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Количество страниц"
                }
            ),
            'price': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Стоимость"
                }
            ),
            'cover_type':  forms.Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Тип обложки"
                }
            ),
            'size': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Размер"
                }
            ),
            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'accept': 'image/*'
                }
            ),
            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Наименование должно начинаться с имени автора')
        return title

    def clean_size(self):

        size = self.cleaned_data['size']
        if re.match(r'\D', size):
            raise ValidationError('Укажите размер в цифрах')
        return size


class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )
    password2 = forms.CharField(
        label='Введите пароль повторно',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Ваш логин',
        widget=forms.TextInput(attrs={'class': 'form-control', }),
        min_length=2,
    )
    password = forms.CharField(
        label='Ваш пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', }),
    )


class ContactForm(forms.Form):
    subject = forms.CharField(
        label="Тема сообщения",
        widget=forms.TextInput(
            attrs={'class': 'form-control'},
        )
    )
    content = forms.CharField(
        label="Текст сообщения",
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 11, },
        )
    )
