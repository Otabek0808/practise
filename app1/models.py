from django.db import models

# Create your models here.
class Programms(models.Model):
    name = models.CharField(max_length=100)
    CATEGORY_CHOICES = [
        ('antivirus', 'Antivirus'),
        ('os', 'Operatsion sistema'),
        ('mobile', 'Mobil dastur'),
        ('other', 'Boshqa'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    download_link = models.URLField(verbose_name="Yuklab olish uchun URL", blank=True, null=True)
    summary = models.TextField(verbose_name="Faylga izoh bering...")
    image = models.ImageField(upload_to='media/', verbose_name="rasm yuklash", blank=True, null=True)

    def __str__(self):
        return self.name