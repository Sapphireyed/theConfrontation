def get_regions(side):
    def_h = 90
    mordor_h = 140
    shire_h = 120
    m_h = 60
    regions = {
        "shire": {
           'name': 'shire',
            'position': 1 if side == 0 else 16,
            'height': shire_h,
            'selected': False,
            'available': False,
            'limit': 4,
            'top_to': ['good1', 'good2'],
            'next_to': [],
            'bottom_to': []
        },
        'good1': {
            'name': 'good1',
            'position': 2 if side == 0 else 15,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['good3', 'good4'] if side == 0 else ['shire'],
            'next_to': ['good2'],
            'bottom_to': ['shire'] if side == 0 else ['good3', 'good4']
        },
        'good2': {
            'name': 'good2',
            'position': 3 if side == 0 else 14,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['good4', 'good5'] if side == 0 else ['shire'],
            'next_to': ['good1'],
            'bottom_to': ['shire'] if side == 0 else ['good4', 'good5']
        },
        'good3': {
            'name': 'good3',
            'position': 4 if side == 0 else 13,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m1', 'm2'] if side == 0 else ['good1'],
            'next_to': ['good4'],
            'bottom_to': ['good1']if side == 0 else ['m1', 'm2']
        },
        'good4': {
            'name': 'good4',
            'position': 5 if side == 0 else 12,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m2', 'm3'] if side == 0 else ['good1', 'good2'],
            'next_to': ['good3', 'good5'],
            'bottom_to': ['good1', 'good2'] if side == 0 else ['m2', 'm3']
        },
        'good5': {
            'name': 'good5',
            'position': 6 if side == 0 else 11,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m3', 'm4'] if side == 0 else ['good2'],
            'next_to': ['good4'],
            'bottom_to': ['good2'] if side == 0 else ['m3', 'm4']
        },
        'm1': {
            'name': 'm1',
            'position': 7 if side == 0 else 10,
            'height': m_h,
            'selected': False,
            'available': False,
            'limit': 1,
            'top_to': ['evil3'] if side == 0 else ['good5'],
            'next_to': ['m2'],
            'bottom_to': ['good3'] if side == 0 else ['good5']
        },
        'm2': {
            'name': 'm2',
            'position': 8 if side == 0 else 9,
            'height': m_h,
            'selected': False,
            'available': False,
            'limit': 1,
            'top_to': ['evil3', 'evil4'] if side == 0 else ['good4', 'good5'] ,
            'next_to': ['m1', 'm2'],
            'bottom_to': ['good3', 'good4'] if side == 0 else ['evil4', 'evil5']
        },
        'm3': {
            'name': 'm3',
            'position': 9 if side == 0 else 8,
            'height': m_h,
            'selected': False,
            'available': False,
            'limit': 1,
            'top_to': ['evil5', 'evil4'] if side == 0 else ['good3', 'good4'] ,
            'next_to': ['m2', 'm4'],
            'bottom_to': ['good4', 'good5']  if side == 0 else ['evil3', 'evil4']
        },
        'm4': {
            'name': 'm4',
            'position': 10 if side == 0 else 7,
            'height': m_h,
            'selected': False,
            'available': False,
            'limit': 1,
            'top_to': ['evil5'] if side == 0 else ['good3'],
            'next_to': ['m3'],
            'bottom_to': ['good5'] if side == 0 else ['evil3']
        },
        'evil5': {
            'name': 'evil5',
            'position': 11 if side == 0 else 6,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m1', 'm2'] if side == 1 else ['evil2'],
            'next_to': ['evil4'],
            'bottom_to': ['evil2'] if side == 1 else ['m3', 'm4']
        },
        'evil4': {
            'name': 'evil4',
            'position': 12 if side == 0 else 5,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m2', 'm3'] if side == 1 else ['evil1', 'evil2'],
            'next_to': ['evil3', 'evil5'],
            'bottom_to': ['evil1', 'evil2'] if side == 1 else ['m2', 'm3']
        },
        'evil3': {
            'name': 'evil3',
            'position': 13 if side == 0 else 4,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['m3', 'm4'] if side == 1 else ['evil1'],
            'next_to': ['evil4'],
            'bottom_to': ['evil1'] if side == 1 else ['m1', 'm2']
        },
        'evil2': {
            'name': 'evil2',
            'position': 14 if side == 0 else 3,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['evil4', 'evil5'] if side == 1 else ['mordor'],
            'next_to': ['evil1'],
            'bottom_to': ['mordor'] if side == 1 else ['evil3', 'evil4']
        },
        'evil1': {
            'name': 'evil1',
            'position': 15 if side == 0 else 2,
            'height': def_h,
            'selected': False,
            'available': False,
            'limit': 2,
            'top_to': ['evil3', 'evil4'] if side == 1 else ['mordor'],
            'next_to': ['evil2'],
            'bottom_to': ['mordor'] if side == 1 else ['evil3', 'evil4']
        },
        'mordor': {
            'name': 'mordor',
            'position': 16 if side == 0 else 1,
            'height': mordor_h,
            'selected': False,
            'available': False,
            'limit': 4,
            'top_to': ['evil1', 'evil2'],
            'next_to': [],
            'bottom_to': []
        }
    }
    return regions