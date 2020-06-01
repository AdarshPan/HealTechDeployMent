from django.shortcuts import render

def loginView(request):
    return render(request,'XrayApp/login.html')

