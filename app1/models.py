from django.db import models

# Create your models here.
class Programms(models.Model):
    choices = (
        ('Antivirus', '1'),
        ('Dasturlar', '2'),
        ('Operatsion tizimlar', '3'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    document = models.FileField(upload_to='media/', verbose_name="fayl yuklash")
    summary = models.TextField(verbose_name="Faylga izoh bering...")
    def __str__(self):
        return self.name