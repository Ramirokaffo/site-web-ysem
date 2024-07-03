from django.db import models
from django.contrib.auth.models import User
from course.models import Level, Course

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

    


class StudentLevel(models.Model):
    GENDER_CHOICE = (
        ("H", "Homme", ),
        ("F", "Femme", )
    )
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name="étudiant")
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, verbose_name="niveau")
    # gender = models.CharField(blank=False, max_length=2, null=False, verbose_name="Sexe", default="H", choices=GENDER_CHOICE)
    # born_date = models.DateField(blank=False, null=True, verbose_name='date de naissance')
    # phone = models.CharField(blank=True, max_length=15, null=False, verbose_name="numéro de téléphone")
    # matricule = models.CharField(blank=False, max_length=15, unique=True, null=False, verbose_name="matricule de l'étudiant")
    
    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name = "étudiant par niveau"
        verbose_name_plural = "étudiants par niveaux"


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name="cours")
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name="étudiant")
    note = models.FloatField(blank=True, max_length=15, null=True, verbose_name="note de l'étudiant")
    appreciation = models.TextField(blank=True, max_length=500, null=True, verbose_name="appréciation")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    catching_up = models.BooleanField(null=False, verbose_name="rattrapé", default=False)

    def __str__(self):
        return self.course.label + " ~ " + self.student.user.username

    class Meta:
        verbose_name = "cours par étudiant"
        # verbose_name_plural = "cours attribués aux étudiants"

