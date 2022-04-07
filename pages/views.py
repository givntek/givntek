from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    text = """ truc bidule chouette """
    return render(request, 'pages/index.html')