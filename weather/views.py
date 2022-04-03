from django.shortcuts import render

def forecast(request):
    return render(request, 'weather/weather.html')