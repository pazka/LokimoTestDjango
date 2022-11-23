import json

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


def apply_generic_query_filter(ObjClass, queryset, query_params):
    model_keys = ObjClass.__dict__.keys()
    filter_params = {}

    for key in query_params:
        if key not in model_keys:
            continue

        if ',' in query_params[key]:
            filter_params[key + "__in"] = query_params[key].split(',')
        else:
            filter_params[key] = query_params[key]

    return queryset.filter(**filter_params)


def debug(txt):
    with open('/LokimoTest/app_logs.txt', 'w') as file:
        file.write(json.dumps(txt))


def apply_ad_filter_radius(queryset, center_x, center_y, radius):
    if radius <= 0 or radius is None:
        return queryset
    if center_x is None or center_y is None:
        return queryset

    center = Point(x=center_x, y=center_y)
    return queryset.filter(position__distance_lt=(center, Distance(m=radius)))
