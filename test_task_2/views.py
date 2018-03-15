from django.http import HttpResponse
from django.template import loader
from test_task_2.forms import MapForm
from test_task_2.utils import handle_uploaded_file, map_render


def index_view(request, rendered_map=None):
    template = loader.get_template('index.html')
    context = {
        'rendered_map': rendered_map
    }
    return HttpResponse(template.render(context, request))


def get_map(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file_field'])
            map_render()
            return index_view(request) #, rendered_map=rendered_map)
    return index_view(request)



