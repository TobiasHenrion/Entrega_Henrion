from django import forms 

class ComponentsForm(forms.Form):
    CHOICES = (
    ('Placas de video', 'Placas de video'),
    ('Procesadores', 'Procesadores'),
    ('Motherboards', 'Motherboards'),
    ('Gabinetes', 'Gabinetes'),
    ('Refrigeracion', 'Refrigeracion'),
    ('Almacenamiento', 'Almacenamiento'),        
    ('Memorias Ram', 'Memorias Ram'),
    ('Fuentes', 'Fuentes'),
    ('Perifericos', 'Perifericos'),        
    ('Monitores', 'Monitores'),
    ('Otros', 'Otros'),  
)
    name = forms.CharField(max_length=50)
    category = forms.ChoiceField(choices=CHOICES)
    marca = forms.CharField(max_length=25)
    specification = forms.CharField(max_length=500)
    price = forms.FloatField()
    img = forms.ImageField()


