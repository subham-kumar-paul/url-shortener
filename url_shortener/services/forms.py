from django import forms
from .models import Url

class UrlForm(forms.ModelForm):
    # alias = forms.CharField(initial=None, required=False)
    class Meta:
        model = Url
        fields = ['target_url', 'alias']
        widgets = {
            'target_url' : forms.TextInput(attrs={'class': 'form-control','id':'staticUrl', 'placeholder': 'Paste URL', 'name':'URL'}),
            'alias' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias', 'name':'alias', 'title': 'This field is not mandatory, you can leave it blank, automatically an alias will be assigned but if you choose to enter it should be an unique one'}),
        }

        def clean_alias(self):
            alias = self.cleaned_data['alias']
            if Url.objects.filter(alias=alias).exists():
                raise forms.ValidationError("This alias is already in use.")
            return alias