from django.shortcuts import render

#access the html templates here aka views
def home(request):
    return render(request, 'base.html')
