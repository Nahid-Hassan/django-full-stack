from django import forms
from django.core import validators

# create own custom validators
# def check_for_z(value):
#     if(value[0].lower() != 'z'):
#         raise forms.ValidationError('Name must be start using character z')


class FromName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter email again: ')
    text = forms.CharField(widget=forms.Textarea, required = False)
    bootcatcher = forms.CharField(required=False, 
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email'] 
        mail = all_clean_data['verify_email']

        if email != mail:
            raise forms.ValidationError('Make sure you emails match')

    # def clean_bootcatcher(self):  
    #     botcatcher = self.cleaned_data['bootcatcher']

    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     else:
    #         return botcatcher

    # This above clean_bootcatcher() is same as validators=[validators.MaxLengthValidator(0)
    # so instead of using self maid validators we can use django.core -> validators
    # which is saved your lot of time. 

    

