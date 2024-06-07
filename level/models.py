from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True, verbose_name="nom")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "niveau d'étude"
        verbose_name_plural = "niveaux d'étude"

