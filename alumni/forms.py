from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'phone')

    #first_name = forms.CharField(max_length = 100)
    #last_name = forms.CharField(max_length = 100)
    #email = forms.CharField(required=False, max_length = 100)
    #phone = forms.CharField(required=False, max_length = 100)

    # form validation
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        # check if name has numbers
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        # check if name has numbers
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        # check format of email address
        return data

    def clean_phone(self):
        data = self.cleaned_data['phone']
        # check format of phone number
        return data

