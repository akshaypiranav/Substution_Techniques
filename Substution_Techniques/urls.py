"""
URL configuration for Substution_Techniques project.

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
from APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    #CAESER CIPHER 
    path("caeserCipher",views.caeserCipher,name="caeserCipher"),
    path("caeserCipherEncryption",views.caeserCipherEncryption,name="caeserCipherEncryption"),
    path("caeserCipherDecryption",views.caeserCipherDecryption,name="caeserCipherDecryption"),

    
    path("monoalphabeticCipher",views.monoalphabeticCipher,name="monoalphabeticCipher"),
    path("playfairCipher",views.playfairCipher,name="playfairCipher"),
    path("hillCipher",views.hillCipher,name="hillCipher"),
    path("polyalphabeticCipher",views.polyalphabeticCipher,name="polyalphabeticCipher"),
    path("onetimePad",views.onetimePad,name="onetimePad"),
]
