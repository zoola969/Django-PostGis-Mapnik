from django import forms


class MapForm(forms.Form):
    file_field = forms.FileField(required=True)
    map_name = forms.CharField(required=True)


class MapSearch(forms.Form):
    map_search = forms.CharField(required=False)