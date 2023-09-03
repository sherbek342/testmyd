from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.
def index(request):
    lifs = Articles.objects.order_by('-date')
    return render( request, 'lifs/index.html', {'lifs': lifs})


def create(request):

    error = ''
    if request.method =='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lifs_home')
        else:
            error = 'Ощибка'


    form = ArticlesForm()

    data = {
        'form': form
    }


    return render(request, 'lifs/create.html', data)