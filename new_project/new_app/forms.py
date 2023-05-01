from django import forms

class RegisterName(forms.Form):
    your_name=forms.CharField()
    your_email=forms.EmailField()
    your_address=forms.ChoiceField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False)
    
    def clean_botcatcher(self):
        botcatcher=self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            raise forms.ValidationError("length error")
        return botcatcher