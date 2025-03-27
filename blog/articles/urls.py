from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name = 'home'),
    path('about',views.about,name = 'about'),
    path('article-details/<int:id>',views.article_details,name = 'details'),

]