from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
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
    return render(request, 'new_show.html', context)

def shows_create(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.add_message(request, messages.ERROR, v, extra_tags=k)
            return redirect(f'/shows/new')
        network = Network.objects.get(id=request.POST['network'])
        Show.objects.create(title=request.POST['title'], desc=request.POST['desc'], debut=request.POST['debut'], network=network)
        num = Show.objects.get(title=request.POST['title'])
        num = num.id
        return redirect(f'/shows/{num}')
    else:
        return redirect('/shows')

def show_info(request, num):
    show = Show.objects.get(id=num)
    context = {
    'show': show,
    }
    return render(request, 'show_info.html', context)

def show_edit(request, num):
    networks = Network.objects.all()
    show = Show.objects.get(id=num)
    debut = str(show.debut)
    context = {
    'networks': networks,
    'show': show,
    'debut': debut
    }
    return render(request, 'edit_show.html', context)

def show_update(request, num):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        print(errors)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.add_message(request, messages.ERROR, v, extra_tags=k)
            return redirect(f'/shows/{num}/edit')
        show = Show.objects.get(id=num)
        show.title = title=request.POST['title']
        show.debut = request.POST['debut']
        show.desc = request.POST['desc']
        show.network = Network.objects.get(id=request.POST['network'])
        show.save()
    else:
        return redirect(f'/shows/{num}/edit')
    return redirect(f'/shows/{num}')

def show_destroy(request, num):
    show = Show.objects.get(id=num)
    show.delete()
    return redirect('/')
