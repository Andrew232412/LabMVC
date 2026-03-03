from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["tytul", "autor", "rok_wydania"]
        widgets = {
            "rok_wydania": forms.NumberInput(attrs={"min": 1, "max": 2100}),
        }
