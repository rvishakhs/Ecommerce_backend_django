from django.shortcuts import render

def home(request):
    # This now correctly looks for 'home.html' in your new templates folder
    return render(request, 'home.html')