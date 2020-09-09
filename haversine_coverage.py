import random


def haversine(lat1, lng1, lat2, lng2):
    return random.randint(0, 20)


locations = [
    {'id': 1000, 'zip_code': '37069', 'lat': 45.35, 'lng': 10.84},
    {'id': 1001, 'zip_code': '37121', 'lat': 45.44, 'lng': 10.99},
    {'id': 1001, 'zip_code': '37129', 'lat': 45.44, 'lng': 11.00},
    {'id': 1001, 'zip_code': '37133', 'lat': 45.43, 'lng': 11.02},
]

shoppers = [
    {'id': 'S1', 'lat': 45.46, 'lng': 11.03, 'enabled': True},
    {'id': 'S2', 'lat': 45.46, 'lng': 10.12, 'enabled': True},
    {'id': 'S3', 'lat': 45.34, 'lng': 10.81, 'enabled': True},
    {'id': 'S4', 'lat': 45.76, 'lng': 10.57, 'enabled': True},
    {'id': 'S5', 'lat': 45.34, 'lng': 10.63, 'enabled': True},
    {'id': 'S6', 'lat': 45.42, 'lng': 10.81, 'enabled': True},
    {'id': 'S7', 'lat': 45.34, 'lng': 10.94, 'enabled': True},
]

len_locations = len(locations)


def per_counter(x, y, locations):
    n = 0
    for location in locations:
        # if the distance less than 10 km shopper cover this point
        if haversine(x, y, location['lat'], location['lng']) < 10:
            n += 1
    return (n / len_locations) * 100


def haversine_sort(coverages):
    l = []
    while len(coverages) > 0:
        max = -1
        index = -1
        for i, coverage in enumerate(coverages):
            if coverage['coverage'] > max:
                max = coverage['coverage']
                index = i
        data = coverages[index]
        l.append(data)
        coverages.remove(data)
    return l


def haversine_coverage(locations, shoppers):
    coverages = []
    for shopper in shoppers:
        d = dict()
        d['shopper_id'] = shopper['id']
        d['coverage'] = per_counter(shopper['lat'], shopper['lng'], locations)
        coverages.append(d)
    return haversine_sort(coverages)


if __name__ == '__main__':
    coverages = haversine_coverage(locations, shoppers)
    print(coverages)
