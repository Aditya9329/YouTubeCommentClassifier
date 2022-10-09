from django import forms


class File(forms.Form):
    upload_file =forms.FileField()