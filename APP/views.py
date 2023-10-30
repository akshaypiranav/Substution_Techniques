from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

#CAESER CIPHER
def caeserCipherEncryption(request):
    return render(request, "caeserCipher.html")


def caeserCipherDecryption(request):
    return render(request, "caeserCipher.html")


def caeserCipher(request):
    return render(request, "caeserCipher.html")



def monoalphabeticCipher(request):
    return render(request,"monalphabeticCipher.html")


def playfairCipher(request):
    return render(request,"playfairCipher.html")


def hillCipher(request):
    return render(request,"hillCipher.html")


def polyalphabeticCipher(request):
    return render(request,"polyalphabeticChiper.html")


def onetimePad(request):
    return render(request,"onetimePad.html")
