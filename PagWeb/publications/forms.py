from django import forms


class PublicationsForm(forms.Form):
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

    SELL_CHOICES= (
        ('Vender', 'Vender'),
        ('Canjear', 'Canjear'),
    )

    name = forms.CharField(max_length=50)
    category = forms.ChoiceField(choices=CHOICES)
    marca = forms.CharField(max_length=25)
    notes = forms.CharField(max_length=500)
    meth = forms.ChoiceField(choices=SELL_CHOICES)
    price = forms.FloatField()
    change = forms.CharField(max_length=300, required=False)
    img = forms.ImageField()


