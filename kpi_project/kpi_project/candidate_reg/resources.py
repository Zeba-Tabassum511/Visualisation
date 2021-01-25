from import_export import resources
from .models import Candidate
from django import forms

class CandidateResource(resources.ModelResource):
    class meta:
        model = Candidate

class SelectionForm(forms.Form):
    selection=forms.ChoiceField(choices=(('CHRT','KPI Report Charts'),('BAR','KPI Report Bars')))

