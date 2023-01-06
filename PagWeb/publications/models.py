from django.db import models

class Publications(models.Model):
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

    SELL_METHOD = (
        ('Vender', 'Vender'),
        ('Canjear', 'Canjear'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(choices = CHOICES, max_length=25)
    marca = models.CharField(max_length=25)
    mehtod = models.CharField(choices = SELL_METHOD, max_length= 10)
    notes = models.CharField(max_length=500)

