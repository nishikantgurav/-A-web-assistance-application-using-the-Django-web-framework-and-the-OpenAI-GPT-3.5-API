from django import forms
from django.forms import Textarea
class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('question', 'Question'),
                                          ('other', 'Other')])
    Subject = forms.CharField(required=False)
    body = forms.CharField(widget=Textarea)


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length=100)