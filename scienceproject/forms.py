from django import forms


class GuForm(forms.Form):
    gu = forms.ChoiceField()        