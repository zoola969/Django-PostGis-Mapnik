import uuid
import zipfile
import mapnik

from django.contrib.gis.utils import LayerMapping
from django.db.models.signals import pre_save

from test_task_2.models import TestFields, Map


def make_filepath(instance, filename):
    new_filename = "%s.%s" % (uuid.uuid4(),
                             filename.split('.')[-1])
    return '/'.join([instance.__class__.__name__.lower(), new_filename])


def handle_uploaded_file(f, map_name):
    with open('media/SHP.zip', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    z = zipfile.ZipFile('media/SHP.zip', 'r')
    z.extractall('media/SHP/')
    map = Map(name=map_name)
    map.save()
    mapping = {'productivi': 'productivi',
               'mpoly': 'POLYGON',
               }
    lm = LayerMapping(TestFields, 'media/SHP/test_fields.shp', mapping, transform=False)

    def pre_save_callback(sender, instance, *args, **kwargs):
        instance.field = map

    pre_save.connect(pre_save_callback, sender=TestFields)
    lm.save(verbose=True)
    pre_save.disconnect(pre_save_callback, sender=TestFields)


def map_render(map_id):

    m = mapnik.Map(1920,1080)
    m.background = mapnik.Color('steelblue')

    params = dict(dbname='test_task',table='(select * from test_task_2_testfields where field_id=' + str(map_id) + ') as gay',user='test_user',password='qwerty123')
    postgis = mapnik.PostGIS(**params)
    lyr = mapnik.Layer('PostGis Layer')
    lyr.datasource = postgis

######## main style
    main_rule = mapnik.Rule()
    main_style = mapnik.Style()

    main_style.rules.append(main_rule)
    m.append_style('main', main_style)

######### red style for productivi <= 30
    red_filter = mapnik.Filter("[productivi] <= 30")
    red_style = mapnik.Style()
    red_rule = mapnik.Rule()
    red_rule.filter = red_filter

    polygon_symbolizer = mapnik.PolygonSymbolizer()
    polygon_symbolizer.fill = mapnik.Color('#FF0000')
    red_rule.symbols.append(polygon_symbolizer)

    red_style.rules.append(red_rule)
    m.append_style('red', red_style)

    # orange style for productivi >= 31 and < 70
    orange_filter = mapnik.Filter("([productivi] > 30) and ([productivi] < 70)")
    orange_style = mapnik.Style()
    orange_rule = mapnik.Rule()
    orange_rule.filter = orange_filter

    polygon_symbolizer = mapnik.PolygonSymbolizer()
    polygon_symbolizer.fill = mapnik.Color('#FF8000')
    orange_rule.symbols.append(polygon_symbolizer)

    orange_style.rules.append(orange_rule)
    m.append_style('orange', orange_style)

######## green style for productivi >+ 70
    green_filter = mapnik.Filter("([productivi] >= 70)")
    green_style = mapnik.Style()
    green_rule = mapnik.Rule()
    green_rule.filter = green_filter

    polygon_symbolizer = mapnik.PolygonSymbolizer()
    polygon_symbolizer.fill = mapnik.Color('#00FF00')
    green_rule.symbols.append(polygon_symbolizer)

    green_style.rules.append(green_rule)
    m.append_style('green', green_style)

######## render
    lyr.styles.append('main')
    lyr.styles.append('red')
    lyr.styles.append('orange')
    lyr.styles.append('green')

    m.layers.append(lyr)
    m.zoom_all()

    mapnik.render_to_file(m, 'media/Map/map.png', 'png');
