"""
URL configuration for perso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin, name='admin'),
    path('', home,name='home'),
    path('editAbout/<int:id>', editAbout,name='editAbout'),
    path('editSkills/<int:id>', editSkills,name='editSkills'),
    path('editServices/<int:id>', editServices,name='editServices'),
    path('editTesti/<int:id>', editTesti,name='editTesti'),
    path('editPortfolio/<int:id>', editPortfolio,name='editPortfolio'),
    path('editContact/<int:id>', editContact,name='editContact'),
    path('showSkills/', showSkills,name='showSkills'),
    path('showServices/', showServices,name='showServices'),
    path('showTesti/', showTesti,name='showTesti'),
    path('showContact/', showContact,name='showContact'),
    path('showPorto/', showPorto,name='showPorto'),
    path('showSkills/destroySkills/<int:id>', destroySkills),
    path('showServices/destroyServices/<int:id>', destroyServices),
    path('showTesti/destroyTesti/<int:id>', destroyTesti),
    path('showTesti/destroyTesti/<int:id>', destroyTesti),
    path('showPorto/destroyPorto/<int:id>', destroyPorto),
    path('addSkills/', addSkills,name='addSkills'),
    path('addServices/', addServices,name='addServices'),
    path('addTesti/', addTesti,name='addTesti'),
    path('addFiltre/', addFiltre,name='addFiltre'),
    path('addPorto/', addPorto,name='addPorto'),
    path('addFiltre/', addFiltre,name='addFiltre'),
]
