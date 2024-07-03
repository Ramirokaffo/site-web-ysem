from django import forms


class InscriptionForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

    first_name = forms.CharField(max_length=255, label="nom")
    last_name = forms.CharField(max_length=255, label="prénom")
    email = forms.EmailField(label="email")
    phone_number = forms.CharField(max_length=255, label="téléphone")
    country = forms.CharField(max_length=255, label="pays")
    city = forms.CharField(max_length=255, label="ville")
    region = forms.CharField(max_length=255, label="region")
    departement = forms.CharField(max_length=255, label="departement")
    province = forms.CharField(max_length=255, label="province")
    father_full_name = forms.CharField(max_length=255, label="nom du parent")
    father_phone_number = forms.CharField(max_length=255, label="numéro du parent")
    father_email = forms.EmailField(label="email du père")
    father_live_city = forms.CharField(max_length=255, label="residence du parent")
    father_work = forms.CharField(max_length=255, label="occupation du parent")
    gender = forms.CharField(max_length=255, label="sexe")
    bord_date = forms.DateField(label="date de naissance")
    place_of_birth = forms.CharField(max_length=255, label="lieu de naissance")

    template_name = "inscription/form_snippet/inscription_form.html"
