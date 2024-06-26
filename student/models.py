from django.db import models
from django.contrib.auth.models import User, Group


class Student(models.Model):
    GENDER_CHOICE = (
        ("H", "Homme", ),
        ("F", "Femme", )
    )
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name="utilisateur correspondant")
    gender = models.CharField(blank=False, max_length=2, null=False, verbose_name="Sexe", default="H", choices=GENDER_CHOICE)
    born_date = models.DateField(blank=False, null=True, verbose_name='date de naissance')
    phone = models.CharField(blank=True, max_length=15, null=False, verbose_name="numéro de téléphone")
    matricule = models.CharField(blank=False, max_length=15, unique=True, null=False, verbose_name="matricule de l'étudiant")
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "étudiant"
        verbose_name_plural = "étudiants"

