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
#########################################################################################################
    #CAESER CIPHER 
    path("caeserCipher",views.caeserCipher,name="caeserCipher"),
    path("caeserCipherEncryption",views.caeserCipherEncryption,name="caeserCipherEncryption"),
    path("caeserCipherDecryption",views.caeserCipherDecryption,name="caeserCipherDecryption"),
#########################################################################################################
    #MONOALPHABETIC CIPHER
    path("monoalphabeticCipher",views.monoalphabeticCipher,name="monoalphabeticCipher"),
    path("monoalphabeticCipherEncryption",views.monoalphabeticCipherEncryption,name="monoalphabeticCipherEncryption"),
    path("monoalphabeticCipherDecryption",views.monoalphabeticCipherDecryption,name="monoalphabeticCipherDecryption"),
##########################################################################################################
    #PLAYFAIR CIPHER
    path("playfairCipher",views.playfairCipher,name="playfairCipher"),
    path("playfairCipherEncryption",views.playfairCipherEncryption,name="playfairCipherEncryption"),
    path("playfairCipherDecryption",views.playfairCipherDecryption,name="playfairCipherDecryption"),
############################################################################################################
    #HILL CIPHER
    path("hillCipher",views.hillCipher,name="hillCipher"),
    path("hillCipherEncryption",views.hillCipherEncryption,name="hillCipherEncryption"),
    path("hillCipherDecryption",views.hillCipherDecryption,name="hillCipherDecryption"),
#########################################################################################################
    #POLYALPHABETIC CIPHER
    path("polyalphabeticCipher",views.polyalphabeticCipher,name="polyalphabeticCipher"),
    path("polyalphabeticCipherEncryption",views.polyalphabeticCipherEncryption,name="polyalphabeticCipherEncryption"),
    path("polyalphabeticCipherDecryption",views.polyalphabeticCipherDecryption,name="polyalphabeticCipherDecryption"),

#########################################################################################################
    #ONE TIME PAD
    path("onetimePad",views.onetimePad,name="onetimePad"),
    path("onetimePadEncryption",views.onetimePadEncryption,name="onetimePadEncryption"),
    path("onetimePadDecryption",views.onetimePadDecryption,name="onetimePadDecryption"),
]
