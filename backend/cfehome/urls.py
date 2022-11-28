
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('auth/', obtain_auth_token), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v2/', include('cfehome.routers'))

]
