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

    SELL_CHOICES= (
        ('Vender', 'Vender'),
        ('Canjear', 'Canjear'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(choices = CHOICES, max_length=25)
    marca = models.CharField(max_length=25)
    meth = models.CharField(choices = SELL_CHOICES, max_length= 10)
    notes = models.CharField(max_length=500)
    img = models.ImageField(upload_to="publications", default="")
    change = models.CharField(max_length=300, default="")
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name


