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

def apply_radius_filter(queryset,radius):
    return queryset