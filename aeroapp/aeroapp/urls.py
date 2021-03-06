"""aeroapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls', namespace='core')),  
    path('redessociais/', include('socialnetworks.urls', namespace='socialnetworks')),
    path('aeronaves/', include('aircrafts.urls', namespace='aircrafts')),
    path('contas/', include('accounts.urls', namespace='accounts')),
    path('paises/', include('countries.urls', namespace='countries')),
    path('estados/', include('states.urls', namespace='states')),
    path('cidades/', include('cities.urls', namespace='cities')),
    path('passageiros/', include('passengers.urls', namespace='passengers')),
    path('tickets/', include('tickets.urls', namespace='tickets')),
    path('flights/', include('flights.urls', namespace='flights')),
    path('extras/', include('extras.urls', namespace='extras')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)