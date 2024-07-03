from django.db import models

class Course(models.Model):
    # SEMESTER_CHOICE = {
    #     (1, "Semestre 1"),
    #     (2, "Semestre 2"),
    # }

    first_name = models.CharField(max_length=255, null=True, unique=True, verbose_name="nom")
    last_name = models.CharField(max_length=255, null=True, unique=True, verbose_name="prénom")
    email = models.EmailField(blank=True, null=True, verbose_name="email")
    phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="téléphone")
    country = models.CharField(max_length=255, blank=True, null=True, verbose_name="pays")
    city = models.CharField(max_length=255, blank=True, null=True, verbose_name="ville")
    region = models.CharField(max_length=255, blank=True, null=True, verbose_name="region")
    departement = models.CharField(max_length=255, blank=True, null=True, verbose_name="departement")
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name="province")
    father_full_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="nom du parent")
    father_phone_number = models.CharField(max_length=255, blank=True, null=True, verbose_name="numéro du parent")
    father_email = models.EmailField(blank=True, null=True, verbose_name="email du père")
    father_live_city = models.CharField(max_length=255, blank=True, null=True, verbose_name="residence du parent")
    father_work = models.CharField(max_length=255, blank=True, null=True, verbose_name="occupation du parent")
    gender = models.CharField(max_length=255, blank=True, null=True, verbose_name="sexe")
    bord_date = models.DateField(blank=True, null=True, verbose_name="date de naissance")
    place_of_birth = models.CharField(max_length=255, blank=False, null=False, verbose_name="lieu de naissance")
    last_updated = models.DateTimeField(auto_now=True, verbose_name="dernière mise à jour")
    created_at = models.DateField(blank=True, null=True, auto_created=True, auto_now_add=True)
    # level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="niveau" )
    # department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="département")
    # program = models.ForeignKey(CourseProgram, on_delete=models.SET_NULL, null=True, verbose_name="proramme concerné")
    # semester = models.IntegerField(null=False, blank=False, choices=SEMESTER_CHOICE, verbose_name="semestre", default=1)
    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "inscription"
        verbose_name_plural = "inscriptions"

