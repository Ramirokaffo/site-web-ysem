from django.db import models

class Student(models.Model):
    label = models.CharField(max_length=255, null=True, unique=True, verbose_name="Etudiant")
    description = models.TextField(blank=True, null=True, verbose_name="description du cours")
    creditCount = models.IntegerField(blank=False, null=False, verbose_name="nombre de crédit")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "cours"
        verbose_name_plural = "cours"

