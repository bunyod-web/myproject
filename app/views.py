from django.shortcuts import render
from .models import Index
from django import  db

def index(request):
    main1 = Index.objects.all()
    context = {
        "main1": main1
    }
    return render(request, 'index.html', context)
