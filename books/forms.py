from django import forms
from .models import Book
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['title', 'description', 'pages_quantity', 'price', 'cover_type', 'size', 'exist']

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
            'cover_type': forms.TextInput(
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

            'exist': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input',
                }
            )
        }
        # 'publication_date': forms.DateInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': "Дата публикации"
        #     }
        # ),
        # 'photo': forms.TextInput(
        #     attrs={
        #         'class': 'form-control',
        #         'placeholder': "Фотография обложки"
        #     }
        # ),

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


    # def clean_pages_quantity(self):
    #
    #     pages_quantity = self.cleaned_data['pages_quantity']
    #     if re.match(r'\D', pages_quantity):
    #         raise ValidationError('Некорректный ввод')
    #     return pages_quantity

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class':'form-control', }),
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



# class BookForm(forms.Form):
#
#     title = forms.CharField(max_length=50,
#                            min_length=2,
#                            strip=True,
#                            label="Наименование книги",)
#     description = forms.CharField(max_length=600,
#                                   min_length=2,
#                                   strip=True,
#                                   widget=forms.Textarea,
#                                   label="Описание",
#                                   initial="Описание")
#     pages_quantity = forms.CharField(max_length=4,
#                                   min_length=2,
#                                   strip=True,
#                                   label="Количество страниц")
#     price = forms.FloatField(min_value=1,
#                                # step_size=10,
#                                label="Стоимость")
#                                 # initial=40)
#     cover_type = forms.CharField(max_length=20,
#                                   min_length=2,
#                                   strip=True,
#                                   label="Тип обложки",
#                                   initial='Мягкий переплет')
#     size = forms.CharField(max_length=12,
#                            min_length=2,
#                            strip=True,
#                            label="Размер",)
#     publication_date = forms.DateField(label="Дата публикации")
#                                        # widget=forms.SelectDateWidget,
#     photo = forms.ImageField(required=False,
#                              label="Фотография обложки")