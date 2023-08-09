from django import forms

class LoginForm(forms.Form):
    login_name = forms.CharField(label = 'Enter your login name', max_length=10, required=True)

    def clean_login_name(self):
        data = self.cleaned_data['login_name']
        first_letter = data[0]
        if first_letter.isdigit():
            raise forms.ValidationError
        return data
