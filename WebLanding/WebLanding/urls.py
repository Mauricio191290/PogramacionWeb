"""WebLanding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
#from django.urls import path
from django.urls import include, path,re_path
from django.contrib.auth.views import logout_then_login
from django.config import settings
from django.config.urls.static import static 

urlpatterns = [
    #Manejo la direccion del URL para que se redireccione
    path('admin/', admin.site.urls),
    path('', include ('Landing.urls')),
    path('Login/', include ('Login.urls')),
    path('Dashboard/',include ('Dashboard.urls')),
    path('Register/', include ('Register.urls')),
    path ('logout/',logout_then_login, name = 'logout'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
