from django.shortcuts import render, HttpResponse, redirect
from .models import Show, Network
# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    shows = Show.objects.all()
    context = {
    'shows': shows,
    }
    return render(request, 'all_shows.html', context)

def shows_new(request):
    networks = Network.objects.all()
    context = {
    'networks': networks,
    }
    print(networks, '*********************************')
    return render(request, 'new_show.html', context)

def shows_create(request):
    if request.method == 'POST':
        if request.POST['network'] == 'Choose...':
            return redirect(f'/shows/new')
        network = Network.objects.get(id=request.POST['network'])
        Show.objects.create(title=request.POST['title'], desc=request.POST['desc'], debut=request.POST['debut'])
    num = Show.objects.get(title=request.POST['title'])
    num = num.id
    return redirect(f'/shows') # add individual number later
