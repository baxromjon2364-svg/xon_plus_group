from django.db import models

# Create your models here.
class Product(models.Model):
    rasm=models.ImageField(upload_to='static')
    ishlab_chiqarilgan_joyi=models.CharField(max_length=34)
    nomi=models.CharField(max_length=67)
    izoh=models.TextField()

    def __str__(self):
        return self.nomi

class OrderRequest(models.Model):
    ism = models.CharField(max_length=100)
    telefon = models.CharField(max_length=20)
    uskuna_nomi = models.CharField(max_length=200, blank=True, null=True)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ism} - {self.telefon}"

class CompletedProject(models.Model):
    nomi = models.CharField(max_length=200) # Masalan: "Bag'dod tumanidagi g'isht zavodi liniyasi"
    joyi = models.CharField(max_length=150) # Masalan: "Farg'ona, Bag'dod"
    rasm = models.ImageField(upload_to='completed_projects/') # O'rnatilgan uskunaning haqiqiy rasmi
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomi} ({self.joyi})"
