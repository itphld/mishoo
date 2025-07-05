from django import forms
from .models import Account
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password','class':'form-control'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter Password','class':'form-control'}))
    class Meta:
        model=Account
        fields=['firstname','lastname','mobile','email','password']
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
    def clean(self):
        cleaned_datas=super(RegistrationForm,self).clean()
        password=cleaned_datas.get('password')
        confirm_password=cleaned_datas.get('confirm_password')
        if password!= confirm_password:
            raise forms.ValidationError('Password Doesnt Match')
