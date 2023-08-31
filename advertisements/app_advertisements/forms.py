from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from app_advertisements.models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }
    def clean_title(self):
        title = self.cleaned_data['title'].strip()
        if title[0] in ('?', '!', '$', '%'):
            raise ValidationError(
                _('Заголовок не должен начинаться с символов: ?, !, $, %'),
                code='invalid',
            )
        elif len(title) > 128:
            raise ValidationError(
                _('Заголовок слишком длинный - %(value)символов\nнужно мение 128 символов'),
                code='invalid',
                params={'value': len(title)}
            )
        return title