from django.shortcuts import render,redirect
from django.http import HttpResponse

from candidate_reg.models import Candidate
from .resources import CandidateResource, SelectionForm
from tablib import Dataset
from .visualization import Visualization



# Create your views here.

def home(request):

    return render(request, "kpi/home.html")

def candidate(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email_id = request.POST.get('email_id')
        employee_id = request.POST.get('employee_id') 
        designation = request.POST.get('designation')
        domain = request.POST.get('domain')
        password = request.POST.get('password')


        new_candidate = Candidate(Fullname = fullname, Email_id = email_id, Employee_id = employee_id, Designation = designation, Domain = domain, Password = password)

        new_candidate.save()
        #return render(request, 'kpi/home.html')


    return render(request, 'kpi/candidate.html')



def upload(request):
    if request.method=='POST':
        candidate_resource = CandidateResource()
        dataset = Dataset()
        new_candidate = request.FILES['myfile']

        if not new_candidate.name.endswith('xlsx'):
           # messages.info(request,'wrong format')
            return render(request, 'kpi/upload.html')
        
        imported_data= dataset.load(new_candidate.read(),format='xlsx')
        for data in imported_data:
            value = Candidate(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6]
                )

            value.save()
            print(value)

    return render(request, 'kpi/upload.html')

def get_visualization(request):
        if request.method != 'POST':
            return render(request, 'kpi/visualization.html', {
                "form": SelectionForm()
            })
        else:
            try:
                form = SelectionForm(request.POST)
                choice=""
                if(form.is_valid()):
                    choice=form.cleaned_data['selection']
                content=""
                v=Visualization()
                if(choice=='BAR'):
                    content=v.get_bar_plots(fields=['Designation'])
                else:
                    content=v.get_charts(fields=['Domain'])
            except Exception  as e:
                return render(request,'kpi/visualization.html', 
                    {
                        "error_message": "Some error while getting visualization {}".format(e),
                        "form":SelectionForm()
                    }
                )

        return render(request, 'kpi/visualization.html', {"data":content, "form":SelectionForm() })


