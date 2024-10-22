# home/forms.py
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline', 'content', 'image']  # Fields the admin can edit
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'cols': 80}),
        }
