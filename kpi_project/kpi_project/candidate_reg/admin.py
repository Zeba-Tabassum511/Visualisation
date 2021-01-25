from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from candidate_reg.models import Candidate

# Register your models here.
@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin):
    
    list_display =('Fullname','Email_id','Employee_id','Designation','Domain','Password')