from django.urls import path,include
from restapi import views





urlpatterns = [
    path('',views.apiOverview,name ='apiOverview'),
    path('prod1-list/',views.prod1, name='prod1'),
    path('prod2-list/',views.prod2, name='prod2'),
    path('prod3-list/',views.prod3, name='prod3'),
    path('prod4-list/',views.prod4, name='prod4'),
    
]