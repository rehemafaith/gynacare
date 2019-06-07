from django import forms 
from .models import Comments,Share,Profile


class ShareForm(forms.ModelForm):
  class Meta:
    model = Share
    fields = ('myid','story')


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')