from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Notes


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким адресом электронной почты уже существует.')
        return email


class ToValidateNotesForm(forms.ModelForm):
    CHOICES = [
        ('soc', 'Социальные науки'),
        ('gum', 'Гуманитарные науки'),
        ('est', 'Естественные и точные науки'),
        ('med', 'Медицинские науки'),
        ('tech', 'Техника и технологии'),
        ('selhoz', 'Сельскохозяйственные науки')
    ]
    doc_name = forms.CharField(label='Название документа')
    doc_file = forms.FileField(label='Загрузите файл в формате docx или doc')
    category_status = forms.ChoiceField(choices=CHOICES, label='Выберите категорию')

    class Meta:
        model = Notes
        fields = '__all__'
        exclude = ('node_id','state_status',)

    def clean_doc_name(self):
        doc_name = self.cleaned_data['doc_name']

        if Notes.objects.filter(doc_name=doc_name).exists():
            raise forms.ValidationError('Документ с таким именем уже существует. Пожалуйста, выберите другое название для документа!')
        return doc_name