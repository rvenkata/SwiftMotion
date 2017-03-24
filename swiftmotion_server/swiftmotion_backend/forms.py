from django import forms


class UploadCSVForm(forms.Form):
    filename = forms.CharField(max_length=64)
    csv = forms.FileField()  #
