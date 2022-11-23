import json

from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance

from LokimoTest.LokimoTest.domain.DTOs.AverageDTO import AdSummaryByType
from LokimoTest.LokimoTest.models.AdModel import Ad


def debug(txt):
    with open('/LokimoTest/app_logs.txt', 'w') as file:
        file.write(json.dumps(txt))


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


def apply_ad_filter_radius(queryset, center_x, center_y, radius):
    if radius <= 0 or radius is None:
        return queryset
    if center_x is None or center_y is None:
        return queryset

    center = Point(x=center_x, y=center_y)
    return queryset.filter(position__distance_lt=(center, Distance(m=radius)))


def general_filter_search(ObjClass, queryset, request):
    result = apply_generic_query_filter(ObjClass, queryset, request.GET)
    result = apply_ad_filter_radius(
        result,
        float(request.GET['x']) if 'x' in request.GET else None,
        float(request.GET['y']) if 'y' in request.GET else None,
        float(request.GET['r']) if 'r' in request.GET else 500,
    )
    return result


def group_by_rooms(ads: [Ad]) -> AdSummaryByType:
    summary = AdSummaryByType()
    count = [0, 0, 0, 0]
    sum = [0, 0, 0, 0]

    for ad in ads:
        index = 0
        if int(ad['rooms']) > 3:
            index = 3
        count[index] += 1
        sum[index] += float(ad['price'])
        print(index, ad['price'])

    for index, key in enumerate(summary.__dict__):
        print(key, index)
        setattr(summary, key, sum[index] / (count[index] or 1))

    return summary
