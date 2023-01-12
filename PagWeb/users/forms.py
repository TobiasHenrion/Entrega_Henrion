from django import forms 


class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=1000)
    phone = forms.CharField(max_length=15)
    birth = forms.DateField(widget=DateInput)