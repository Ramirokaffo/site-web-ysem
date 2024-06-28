from django.contrib import admin

from .models import Course, Level, TeacherCourse, TeacherSubmittedCourse
from xhtml2pdf import pisa
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import smart_str
from django.utils.translation import gettext_lazy as _
from io import BytesIO
from zipfile import ZipFile


class LevelAdmin(admin.ModelAdmin):
    search_fields = ["label"]
    date_hierarchy = "created_at"


class CourseAdmin(admin.ModelAdmin):

    list_display = ("label", "creditCount", "created_at", "last_updated", "level", "semester")
    date_hierarchy = "created_at"
    list_filter = ["semester", "level", "creditCount"]
    save_as = True
    save_on_top = True
    search_fields = ["label", "description", "level__label"]
    search_help_text = "Rechercher un cours via son label ou sa description"
    autocomplete_fields = ["level"]

    actions = ["export_as_pdf"]

    @admin.action(description="Imprimer en pdf")
    def export_as_pdf(self, request, queryset):
        # Générer le contenu HTML du PDF
        courses = queryset
        template = 'course/courses_list.html'  # Remplacez par le nom de votre template
        context = {'courses': courses}
        html = render_to_string(template, context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="courses.pdf"'

        # Créer un objet pisaStatus
        status = pisa.CreatePDF(
            html, dest=response, encoding='UTF-8'
        )
        status = pisa.CreatePDF(
            html, dest=response, encoding='UTF-8'
        )

        # Vérifier si la génération du PDF a réussi
        if status.err:
            return HttpResponse('Erreur lors de la génération du PDF: ' + str(status.err))
        else:
            return response

        # return HttpResponseRedirect("/cours_list/")


# class StudentCourseAdmin(admin.ModelAdmin):

#     list_display = ("course", "student", "note", "created_at", "last_updated", )
#     date_hierarchy = "created_at"
#     list_filter = ["student", "course", "course__level"]
#     save_as = True
#     save_on_top = True
#     search_fields = ["student__matricule","student__user__first_name",  "course__label"]
#     search_help_text = "Rechercher via le label du cours ou le nom de l'étudiant"
#     autocomplete_fields = ["course", "student"]


class TeacherCourseAdmin(admin.ModelAdmin):

    list_display = ("course", "teacher", "created_at", "last_updated", )
    date_hierarchy = "created_at"
    list_filter = ["teacher", "course", "course__level"]
    save_as = True
    save_on_top = True
    search_fields = ["teacher__user__first_name",  "course__label"]
    search_help_text = "Rechercher via le label du cours ou le nom de l'enseigant"

    autocomplete_fields = ["course", "teacher"]



class TeacherSubmittedCourseAdmin(admin.ModelAdmin):

    list_display = ("teacher_course", "created_at", "last_updated", )
    date_hierarchy = "created_at"
    list_filter = ["teacher_course", "teacher_course__course", "teacher_course__teacher"]
    save_as = True
    save_on_top = True
    actions = ["export_as_pdf"]
    search_fields = ["teacher_course__teacher__user__first_name",  "teacher_course__course__label"]
    search_help_text = "Rechercher via le label du cours ou le nom de l'enseigant"

    autocomplete_fields = ["teacher_course"]

    
    @admin.action(description="Télécharger les cours sélectionnés")
    def export_as_pdf(self, request, queryset):
        """
        Fonction pour télécharger les cours sélectionnés au format ZIP.

        Args:
            self: Objet admin.ModelAdmin
            request: Objet HttpRequest
            queryset: QuerySet de TeacherSubmittedCourse
        """

        # Vérifier si des cours ont été sélectionnés.
        if not queryset:
            self.message_user(request, _("Veuillez sélectionner des cours à télécharger."))
            return

        # Créer un objet BytesIO pour le fichier ZIP.
        zip_buffer = BytesIO()
        with ZipFile(zip_buffer, 'w') as zip_file:
            for course in queryset:
                # Extraire le nom de fichier du chemin du fichier.
                course_outline_filename = course.course_outline.name.split('/')[-1]
                course_document_filename = course.course_document.name.split('/')[-1]

                # Ajouter les fichiers au fichier ZIP.
                zip_file.writestr(course_outline_filename, course.course_outline.read())
                zip_file.writestr(course_document_filename, course.course_document.read())

        # Positionner le pointeur du buffer au début.
        zip_buffer.seek(0)

        # Créer une réponse HttpResponse.
        response = HttpResponse(zip_buffer.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={course.teacher_course}.zip'
        return response

    




admin.site.register(Level, LevelAdmin)
admin.site.register(Course, CourseAdmin)
# admin.site.register(StudentCourse, StudentCourseAdmin)
admin.site.register(TeacherCourse, TeacherCourseAdmin)
admin.site.register(TeacherSubmittedCourse, TeacherSubmittedCourseAdmin)







