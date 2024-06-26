from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner', 'created_at', 'updated_at')

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        word_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in word_list:
            if word in cleaned_data:
                raise forms.ValidationError(f'использование слова "{word}" недопустимо')
        return cleaned_data
