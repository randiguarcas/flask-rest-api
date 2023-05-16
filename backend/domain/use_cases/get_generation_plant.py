from slugify import slugify
from domain.Plant import Plant


def group_data(data):
    unified_data = {}

    for item in data:
        name = item['name']
        value = float(item['value'])

        name_parts = name.rsplit(' ', 1)
        name_prefix = name_parts[0]
        name_suffix = name_parts[1] if len(name_parts) > 1 else ""

        if name_prefix in unified_data:
            unified_data[name_prefix]['value'] += value
            unified_data[name_prefix]['count'] += 1
        else:
            unified_data[name_prefix] = {
                'name': name_prefix, 'value': value, 'count': 1}

        if name_suffix:
            unified_data[name_prefix]['name'] += " " + name_suffix

    return list(unified_data.values())


def get_generation_plants(data, name):
    coincidences = []

    for item in group_data(data):
        if name in item['name']:
            coincidences.append(item)

    return coincidences
