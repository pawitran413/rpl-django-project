from django.db import models

class Tki(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    nim = models.CharField(max_length=255, null=True)
    angkatan = models.CharField(max_length=255, null=True)
    fakultas = models.CharField(max_length=255, null=True)
    prodi = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Course(models.Model):
    matkul = models.CharField(max_length=255)
    tki = models.ForeignKey(Tki, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return f"Course: {self.matkul} (taken by {self.tki.firstname} {self.tki.lastname})"