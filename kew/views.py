from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
# Create your views here.
def index(request):
    kews = Profile.objects.all()
    return render(request, 'kew/kew.html', {'kews': kews})

