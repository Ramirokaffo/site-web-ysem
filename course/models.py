from django.db import models
from student.models import Student
from staff.models import Staff
from department.models import Department
from course_program.models import CourseProgram
from django.core.exceptions import ValidationError


def validate_pdf_file(value):
    if not value.name.upper().endswith(('.PDF')):
        raise ValidationError("Le fichier doit être au format pdf")
  

class Level(models.Model):
    label = models.CharField(max_length=255, null=True, unique=True, verbose_name="label du niveau d'étude")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "niveau d'étude"
        verbose_name_plural = "niveaux d'étude"
        ordering = ['-created_at']



class Course(models.Model):
    label = models.CharField(max_length=255, null=True, unique=True, verbose_name="label")
    description = models.TextField(blank=True, null=True, verbose_name="description")
    creditCount = models.IntegerField(blank=False, null=False, verbose_name="crédit")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="niveau" )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="département")
    program = models.ForeignKey(CourseProgram, on_delete=models.SET_NULL, null=True, verbose_name="proramme concerné")

    def __str__(self):
        return self.label

    class Meta:
        verbose_name = "cours"
        verbose_name_plural = "cours"


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
        verbose_name = "cours attribué à l'étudiant"
        verbose_name_plural = "cours attribués aux étudiants"


class TeacherCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, verbose_name="cours")
    teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, verbose_name="enseignant")
    # ebook_file = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[validate_pdf_file], verbose_name="Livre au format pdf")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.course.label + " ~ " + self.teacher.user.username

    class Meta:
        verbose_name = "cours attribué à l'enseignant"
        verbose_name_plural = "cours attribués aux enseignants"



class TeacherSubmittedCourse(models.Model):
    teacher_course = models.ForeignKey(TeacherCourse, on_delete=models.SET_NULL, null=True, verbose_name="cours de l'enseignant")
    course_outline = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[validate_pdf_file], verbose_name="plan du cours au format pdf")
    course_document = models.FileField(blank=True, null=True, upload_to='ebook/pdf/%Y/%m/%d', validators=[validate_pdf_file], verbose_name="support du cours format pdf")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)

    def __str__(self):
        return str(self.teacher_course)

    class Meta:
        verbose_name = "support de cours"
        verbose_name_plural = "supports de cours"



