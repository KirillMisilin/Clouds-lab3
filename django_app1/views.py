from django.shortcuts import render, redirect
from django_app1.models import Character
from django_app1.forms import CharacterForm, FindCharForm
import json


def index_page(request):
    # with open("../data/data.json", "r") as read_file:
    # characters = json.load(read_file)
    characters = Character.objects.all()
    if characters:
        return render(request, 'django_app1/index.html', {'characters': characters})
    else:
        return redirect('/get_data')


def get_data(request):
    Character.objects.all().delete()
    with open("../data/data.json", "r") as read_file:
        data = json.load(read_file)
    for el in data:
        Character.objects.create(name=el['name'], href=el['href'], img=el['img'])
    return render(request, 'django_app1/get_data.html')


def form(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = CharacterForm()
    context = {
        "form": form
    }
    return render(request, 'django_app1/form.html', context)


def find_char(request):
    if request.method == 'POST':
        characters = Character.objects.filter(name__icontains=request.POST['input_name'])
        form = FindCharForm(request.POST)
        # print(request.POST['input_name'])
        return render(request, 'django_app1/find_char.html', {'form': form, 'characters': characters})
    else:
        form = FindCharForm()
        return render(request, 'django_app1/find_char.html', {'form': form})
