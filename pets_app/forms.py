from django import forms
from .models import Pet, Category

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'age', 'category', 'image']

    def __init__(self, *args, **kwargs):      # Majburiy qilish kk bo'lsa
        super().__init__(*args, **kwargs)
        self.fields['category'].required = True
        self.fields['category'].empty_label = "Kategoriyani tanlang"

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Yosh manfiy bo'lishi mumkin emas")
        elif age > 200:
            raise forms.ValidationError("Jonvor yoshi shubhali katta")
        return age

    def clean_name(self):
        name:str = self.cleaned_data['name']
        if len(name.strip()) < 2:
            raise forms.ValidationError("Ismi juda ham qisqa")
        elif len(name.strip()) > 100:
            raise forms.ValidationError("Ismi juda uzun")
        return name
    
    def clean_species(self):
        species:str = self.cleaned_data['species']
        if len(species.strip()) < 2:
            raise forms.ValidationError("Bunday qisqa Tur nomi mavjud emas")
        elif len(species.strip()) > 100:
            raise forms.ValidationError("Ismi juda uzun")
        return species