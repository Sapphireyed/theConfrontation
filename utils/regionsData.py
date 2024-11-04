def get_regions(side):
    regions = {
        "shire": {
           'name': 'shire',
            'position': 1 if side == 0 else 16,
            'selected': False,
            'available': False,
            'limit': 4
        },
        'good1': {
            'name': 'good1',
            'position': 2 if side == 0 else 15,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'good2': {
            'name': 'good2',
            'position': 3 if side == 0 else 14,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'good3': {
            'name': 'good3',
            'position': 4 if side == 0 else 13,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'good4': {
            'name': 'good4',
            'position': 5 if side == 0 else 12,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'good5': {
            'name': 'good5',
            'position': 6 if side == 0 else 11,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'm1': {
            'name': 'm1',
            'position': 7 if side == 0 else 10,
            'selected': False,
            'available': False,
            'limit': 1
        },
        'm2': {
            'name': 'm2',
            'position': 8 if side == 0 else 9,
            'selected': False,
            'available': False,
            'limit': 1
        },
        'm3': {
            'name': 'm3',
            'position': 9 if side == 0 else 8,
            'selected': False,
            'available': False,
            'limit': 1
        },
        'm4': {
            'name': 'm4',
            'position': 10 if side == 0 else 7,
            'selected': False,
            'available': False,
            'limit': 1
        },
        'evil5': {
            'name': 'evil5',
            'position': 11 if side == 0 else 6,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'evil4': {
            'name': 'evil4',
            'position': 12 if side == 0 else 5,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'evil3': {
            'name': 'evil3',
            'position': 13 if side == 0 else 4,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'evil2': {
            'name': 'evil2',
            'position': 14 if side == 0 else 3,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'evil1': {
            'name': 'evil1',
            'position': 15 if side == 0 else 2,
            'selected': False,
            'available': False,
            'limit': 2
        },
        'mordor': {
            'name': 'mordor',
            'position': 16 if side == 0 else 1,
            'selected': False,
            'available': False,
            'limit': 4
        }
    }
    return regions