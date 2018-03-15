from django import forms


class MapForm(forms.Form):
    file_field = forms.FileField(required=True)