from django.db import models

class Components(models.Model):
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

    name = models.CharField(max_length=50, verbose_name= 'Nombre')
    category = models.CharField(choices = CHOICES, max_length=25)
    marca = models.CharField(max_length=25)
    specification = models.CharField(default="", max_length=500)
    price = models.FloatField()
    img = models.ImageField(upload_to="componentes")

    def __str__(self):
        return self.name