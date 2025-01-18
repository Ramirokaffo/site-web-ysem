from django.shortcuts import render
from inscription.forms import InscriptionForm
# Create your views here.

def index(request):
    form = InscriptionForm()
    return render(request=request, template_name="inscription/form_snippet/inscription_form.html", context={"form": form})
    # return render(request=request, template_name="inscription/create.html", context={"form": form})