from django.contrib import admin
from django.urls import path

from candidate_reg import views as vw

app_name="kpi"

urlpatterns = [
    path('', vw.home, name='home'),
    path('home/', vw.home, name='home'),
    path('candidate/', vw.candidate),
    path('upload/', vw.upload , name='upload'),
    path('visualization/', vw.get_visualization, name='visualization')
]
