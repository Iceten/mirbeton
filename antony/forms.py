from django.db.models import fields
from django import forms
from . import models
from django.core import validators

work_type_choices = [('path', 'Allée'), ('stairs', 'Escaliers'),
                     ('slab', 'Dalles'), ('other', 'Autre')]

surface_choices = [('under5m2', 'Inférieur à 5m²'), ('under10m2',
                                                     'Entre 5m² et 10m²'), ('above10m2', 'Supérieur à 10m²')]


class LeadConsultForm(forms.ModelForm):
    lead_consult_form = forms.BooleanField(
        widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Lead
        fields = ('work_type', 'surface', 'first_name',
                  'last_name', 'email', 'phone', 'zipcode')

    work_type = forms.CharField(widget=forms.RadioSelect(choices=work_type_choices, attrs={
                                'class': 'subsection-prospect-form--wrapper-form__form--wrapper-radio__wrap-choices'}), required=False)

    surface = forms.CharField(widget=forms.Select(choices=surface_choices, attrs={
                              'class': 'subsection-prospect-form--wrapper-form__form--wrapper-select__wrap-choices'}), required=False)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'subsection-prospect-form--wrapper-form__form--firstname', 'area-required': 'true', 'data-msg-required': 'Merci d\'indiquer votre prenom s\'il vous plaît', 'placeholder': " PRENOM "}), label='Prenom')

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'subsection-prospect-form--wrapper-form__form--lastname', 'area-required': 'true', 'data-msg-required': 'Merci d\'indiquer votre nom s\'il vous plaît', 'placeholder': " NOM "}), label='Nom')

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'subsection-prospect-form--wrapper-form__form--email', 'area-required': 'true', 'data-msg-required': 'Merci d\'indiquer votre email s\'il vous plaît', 'placeholder': " EMAIL "}), label='Email')

    phone = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'subsection-prospect-form--wrapper-form__form--phone', 'area-required': 'true', 'data-msg-required': 'Merci d\'indiquer votre numéro de téléphone s\'il vous plaît', 'placeholder': " TELEPHONE "}), label='Téléphone')

    zipcode = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'subsection-prospect-form--wrapper-form__form--zipcode', 'area-required': 'true', 'data-msg-required': 'Merci d\'indiquer votre code postal s\'il vous plaît', 'placeholder': " CODE POSTAL"}), label='Code Postal')
