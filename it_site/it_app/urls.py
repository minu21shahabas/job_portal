from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('jobs',views.jobs,name='jobs'),
    path('jobfair',views.jobfair,name='jobfair'),
    path('aboutpage',views.aboutpage,name='aboutpage'),


]