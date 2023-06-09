from django import forms
from .models import About, Services, Testi, Skills, Cont, Filtre, Porto

class About_form(forms.ModelForm):
    class Meta:
        model = About
        fields = "__all__"
class Skills_form(forms.ModelForm):
    class Meta:
        model = Skills
        fields = "__all__"
class Testi_form(forms.ModelForm):
    class Meta:
        model = Testi
        fields = "__all__"
class Services_form(forms.ModelForm):
    class Meta:
        model = Services
        fields = "__all__"
class Cont_form(forms.ModelForm):
    class Meta:
        model = Cont
        fields = "__all__"
        
        
class Filtre_form(forms.ModelForm):
    class Meta:
        model = Filtre
        fields = "__all__"
class Porto_form(forms.ModelForm):  
    choice = [(f.filtre, f.filtre) for f in Filtre.objects.all()]
    filtre=forms.ChoiceField(choices=choice)
    class Meta:
        model = Porto
        fields = "__all__"