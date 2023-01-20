from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page , name='home'),
    path('restapi/',include('restapi.urls'))
    # path('api-auth/', include('rest_framework.urls'))
]
