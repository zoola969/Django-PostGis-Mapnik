from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from test_task_2.forms import MapForm, MapSearch
from test_task_2.utils import handle_uploaded_file, map_render
from test_task_2.models import Map


def index_view(request, maps = None):
    template = loader.get_template('index.html')
    context = {
        'maps': maps
    }
    return HttpResponse(template.render(context, request))


def map_view(request, map_id):
    template = loader.get_template('map.html')
    map_render(map_id)
    context = {}
    return HttpResponse(template.render(context, request))


def get_map(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            map_name = form.cleaned_data['map_name']
            handle_uploaded_file(request.FILES['file_field'], map_name)
            map_query = Map.objects.last()
            map_id = map_query.id
            map_render(map_id)
            return redirect('/map/'+str(map_id))
    return index_view(request)


def search_map(request):
    if request.method == 'POST':
        form = MapSearch(request.POST)
        if form.is_valid():
            map_name = form.cleaned_data['map_search']
            if map_name == '':
                maps = Map.objects.all()
            else:
                maps = Map.objects.filter(name__icontains=map_name)
            return index_view(request, maps)
        else:
            return (index_view(request, maps=None))
    else:
        return (index_view(request, maps=None))