from django.urls import path
from .views import home,register,dashboard,companies,drives,apply_drive,application_status
urlpatterns=[
     path('',home,name='home'),
     path('home/',home,name='home_page'),
     path('register/',register,name='register'),
     path('dashboard/',dashboard,name='dashboard'),
     path('companies/',companies,name='companies'),
     path('drives/',drives,name='drives'),
     path('apply/<int:drive_id>/',apply_drive,name='apply_drive'),
     path('application_status/',application_status,name='application_status')
]
     