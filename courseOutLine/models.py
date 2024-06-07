from django.db import models
from django.contrib.auth.models import User, Group
from course.models import Course

class CourseOutline(models.Model):
    GENDER_CHOICE = (
        ("H", "Homme", ),
        ("F", "Femme", )
    )
    enseignant = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, verbose_name="Enseignant correspondant")
    course = models.OneToOneField(Course, on_delete=models.SET_NULL, null=True, verbose_name="Cours correspondant")
    ebook_file = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', verbose_name="plan de cours au format pdf")
    
    def __str__(self):
        return self.enseignant + " " + self.course

    class Meta:
        verbose_name = "plan du cours"
        verbose_name_plural = "plans du cours"


