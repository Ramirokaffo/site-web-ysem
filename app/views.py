
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from course.models import Course
from django.template.loader import render_to_string
from xhtml2pdf import pisa

def index(request: WSGIRequest):
    
    return render(request=request, template_name="index.html")



def cours_list(request: WSGIRequest):
    courses = Course.objects.all()

    # Générer le contenu HTML du PDF
    template = 'course/courses_list.html'  # Remplacez par le nom de votre template
    context = {'courses': courses}
    
    return render(request, template, context)
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

