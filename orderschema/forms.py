from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from orderschema.models import Usermod, Servicemod, Ordermod


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'email')

        widgets = {
            "first_name": TextInput(attrs={
                "required": ''
            }),
            "email": TextInput(attrs={
                "required": ''
            }),
        }


class UsermodForm(forms.ModelForm):
    class Meta:
        model = Usermod
        fields = ('mobile_phone', 'name_org', 'address_org')


class ServicemodForm(forms.ModelForm):
    class Meta:
        model = Servicemod
        fields = ('count',)


class OrdermodForm(forms.ModelForm):
    servicemod = forms.ModelChoiceField(queryset=Servicemod.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Ordermod
        fields = ('servicemod',)
