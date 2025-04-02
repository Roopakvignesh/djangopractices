from django.urls import path
from . import views
urlpatterns=[
    path('',views.activities_list,name='alist'),
    path('activitiesdetails/<int:id>',views.activities_details,name='adet'),

]
