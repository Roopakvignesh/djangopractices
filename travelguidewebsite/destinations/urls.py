from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='home'),
    path('dlist',views.destination_list,name='dlist'),
    
    path('destinationdetails/<int:id>',views.destination_details,name='ddet'),

]
