# coding=utf-8

from emilia.climbs.models import Book, Climb, Region
from emilia.extensions import db


def install():
    """ Adds Book, Climb and Region data to database. """
    fixtures = [
        {
            'book': ('greatest',
                     u'100 Greatest Cycling Climbs',
                     u'100 Greatest Cycling Climbs: A Road Cyclist\'s Guide to Britain\'s Hills',
                     u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                     '/static/img/greatest-cover.jpg',
                     'http://www.franceslincoln.com/100-greatest-cycling-climbs'),
            'climbs': [
                ('cheddar-gorge', 1, u'Cheddar Gorge', u'Cheddar, Somerset', 3, 6665302),
                ('weston-hill', 2, u'Weston Hill', u'Weston, Bath', 4, 6665281),
                ('crowcombe-combe', 3, u'Crowcombe Combe', u'Crowcombe, Somerset', 8, 6665343),
                ('porlock', 4, u'Porlock', u'Porlock, Somerset', 9, 6665361),
                ('dunkery-beacon', 5, u'Dunkery Beacon', u'Porlock, Somerset', 10, 6665334),
                ('exmoor-forest', 6, u'Exmoor Forest', u'Lynmouth, Devon', 3, 6665364),
                ('challacombe', 7, u'Challacombe', u'Woolacombe, Devon', 6, 6665368),
                ('dartmeet', 8, u'Dartmeet', u'Dartmeet, Devon', 6, 6665214),
                ('haytor-vale', 9, u'Haytor Vale', u'Bovey Tracey, Devon', 5, 6665314),
                ('widecombe', 10, u'Widecombe', u'Widecome-in-the-Moor, Devon', 7, 6665221),
                ('rundlestone', 11, u'Rundlestone', u'Tavistock, Devon', 7, 6665277),
                ('salcombe-hill', 12, u'Salcombe Hill', u'Sidmouth, Devon', 5, 6691752),
                ('dovers-hill', 13, u'Dover\'s Hill', u'Chipping Campden, Gloucestershire', 5, 6681432),
                ('box-hill', 14, u'Box Hill', u'Dorking, Surrey', 3, 6695759),
                ('yorks-hill', 15, u'York\'s Hill', u'Sevenoaks, Kent', 6, 6691251),
                ('white-lane', 16, u'White Lane', u'Limpsfield, Surrey', 5, 6691229),
                ('leith-hill', 17, u'Leith Hill', u'Dorking, Surrey', 6, 6691321),
                ('white-downs', 18, u'White Downs', u'Dorking, Surrey', 8, 6691301),
                ('the-wall', 19, u'The Wall', u'Forest Row, East Sussex', 5, 6691343),
                ('toys-hill', 20, u'Toys Hill', u'Edenbridge, Kent', 7, 6691062),
                ('steyning-bostal', 21, u'Steyning Bostal', u'Steyning, West Sussex', 15, 6691367),
                ('ditchling-beacon', 22, u'Ditchling Beacon', u'Ditchling, East Sussex', 6, 6691384),
                ('whiteleaf', 23, u'Whiteleaf', u'Princes Risborough, Buckinghamshire', 6, 6681416),
                ('streatley-hill', 24, u'Streatley Hill', u'Streatley, West Berkshire', 5, 6665255),
                ('combe-gibbet', 25, u'Combe Gibbet', u'Hungerford, West Berkshire', 5, 6665230),
                ('mott-street', 26, u'Mott Street', u'High Beach, Essex', 3, 6691219),
                ('swains-lane', 27, u'Swains Lane', u'Highgate, London', 4, 6691038),
                ('michaelgate', 28, u'Michaelgate', u'Lincoln, Lincolnshire', 4, 6691237),
                ('terrace-hill', 29, u'Terrace Hill', u'Vale of Belvoir, Leicestershire', 1, 6691047),
                ('monsal-head', 30, u'Monsal Head', u'Bakewell, Derbyshire', 3, 6687943),
                ('bank-road', 31, u'Bank Road', u'Matlock, Derbyshire', 8, 6677679),
                ('riber', 32, u'Riber', u'Matlock, Derbyshire', 9, 6677656),
                ('winnats-pass', 33, u'Winnats Pass', u'Castleton, Derbyshire', 8, 6698034),
                ('rowsley-bar', 34, u'Rowsley Bar', u'Rowsley, Derbyshire', 6, 6681397),
                ('curbar-edge', 35, u'Curbar Edge', u'Curbar, Derbyshire', 6, 6687953),
                ('mow-cop', 36, u'Mow Cop', u'Mow Cop, Staffordshire', 9, 6687912),
                ('peaslows', 37, u'Peaslows', u'Chapel-en-le-Frith, Derbyshire', 4, 6820268),
                ('jiggers-bank', 38, u'Jiggers Bank', u'Ironbridge, Shropshire', 3, 6681373),
                ('the-burway', 39, u'The Burway', u'Church Stretton, Shropshire', 9, 6681340),
                ('shibden-wall', 40, u'Shibden Wall', u'Halifax, West Yorkshire', 8, 6690966),
                ('pea-royd-lane', 41, u'Pea Royd Lane', u'Stocksbridge, Sheffield', 8, 6697336),
                ('jackson-bridge', 42, u'Jackson Bridge', u'Jackson Bridge, Holmfirth', 7, 6691287),
                ('holme-moss', 43, u'Holme Moss', u'Holmfirth, Kirklees', 5, 6691272),
                ('halifax-lane', 44, u'Halifax Lane', u'Luddenden, Calderdale', 8, 6690955),
                ('park-rash', 45, u'Park Rash', u'Kettlewell, Yorkshire Dales', 9, 6687990),
                ('oxnop-scar', 46, u'Oxnop Scar', u'Askrigg, Yorkshire Dales', 7, 6688073),
                ('malham-cove', 47, u'Malham Cove', u'Malham, Yorkshire Dales', 7, 6688083),
                ('langcliffe-scar', 48, u'Langcliffe Scar', u'Langcliffe, Yorkshire Dales', 7, 6688008),
                ('buttertubs', 49, u'Buttertubs', u'Swaledale, Yorkshire Dales', 8, 6697314),
                ('fleet-moss', 50, u'Fleet Moss', u'Hawes, Yorkshire Dales', 9, 6687966),
                ('tan-hill', 51, u'Tan Hill', u'Langwaithe, Yorkshire Dales', 3, 6661216),
                ('greenhow-hill', 52, u'Greenhow Hill', u'Pateley Bridge, North Yorkshire', 6, 6690987),
                ('norwood-edge', 53, u'Norwood Edge', u'Otley, Leeds', 5, 6691028),
                ('boltby-bank', 54, u'Boltby Bank', u'Boltby, North Yorkshire', 7, 6696481),
                ('rosedale-chimney', 55, u'Rosedale Chimney', u'Rosedale Abbey, North Yorkshire Moors', 10, 6690945),
                ('white-horse-bank', 56, u'White Horse Bank', u'Kilburn, North Yorkshire Moors', 7, 6690931),
                ('the-stang', 57, u'The Stang', u'Langwaithe, North Yorkshire', 6, 6691007),
                ('carlton-bank', 58, u'Carlton Bank', u'Carlton-in-Cleveland, North Yorkshire', 7, 6691019),
                ('crawleyside', 59, u'Crawleyside', u'Stanhope, Durham', 7, 6681219),
                ('peth-bank', 60, u'Peth Bank', u'Lanchester, Durham', 4, 6681185),
                ('winters-gibbet', 61, u'Winters Gibbet', u'Elsdon, Northumberland', 5, 6677593),
                ('chapel-fell', 62, u'Chapel Fell', u'St. John\s Chapel, Durham', 9, 6678141),
                ('mennock-pass', 63, u'Mennock Pass', u'Mennock, Drumfris and Galloway', 5, 6697054),
                ('cairn-o-mount', 64, u'Cairn o\' Mount', u'Fettercairn, Aberdeenshire', 7, 6674408),
                ('the-cairnwell', 65, u'The Cairnwell', u'Spittal of Glenshee, Perth and Kinross', 6, 7011208),
                ('the-lecht', 66, u'The Lecht', u'Cock Bridge, Aberdeenshire', 10, 6674394),
                ('cairn-gorm', 67, u'Cairn Gorm', u'Aviemore, Highland', 6, 6674377),
                ('rest-and-be-thankful', 68, u'Rest and be Thankful', u'Cairndow, Argyll and Bute', 6, 6697031),
                ('bealach-na-ba', 69, u'Bealach-na-Ba', u'Applecross, Highland', 11, 6671117),
                ('cat-and-fiddle', 70, u'Cat and Fiddle', u'Macclesfield, Cheshire', 4, 6681311),
                ('swiss-hill', 71, u'Swiss Hill', u'Alderley Edge, Cheshire', 5, 6687924),
                ('the-rake', 72, u'The Rake', u'Ramsbottom, Lancashire', 8, 6688059),
                ('garsdale-head', 73, u'Garsdale Head', u'Garsdale Head, Cumbria', 7, 6677557),
                ('nick-of-pendle', 74, u'Nick of Pendle', u'Sabden, Lancashire', 6, 6688055),
                ('trough-of-bowland', 75, u'Trough of Bowland', u'Skyes, Forest of Bowland, Lancashire', 4, 6688001),
                ('jubilee-tower', 76, u'Jubilee Tower', u'Quernmore, Lancashire', 6, 6688053),
                ('hartside', 77, u'Hartside', u'Melmerby, Cumbria', 5, 6681248),
                ('lamps-moss', 78, u'Lamps Moss', u'Nateby, Cumbria', 7, 6687980),
                ('cross-of-greet', 79, u'Cross of Greet', u'Slaidburn, Lancashire', 6, 6688035),
                ('honister-pass', 80, u'Honister Pass', u'Buttermere, Cumbria', 9, 6677352),
                ('newlands-hause', 81, u'Newlands Hause', u'Buttermere, Cumbria', 8, 6677326),
                ('whinlatter-pass', 82, u'Whinlatter Pass', u'Braithwaite, Cumbria', 5, 6695737),
                ('kirkstone-pass', 83, u'Kirkstone Pass', u'Ambleside, Cumbria', 7, 6677526),
                ('hardknott-pass', 84, u'Hardknott Pass', u'Eskdale, Cumbria', 10, 6677392),
                ('wrynose-pass', 85, u'Wrynose Pass', u'Little Langdale, Cumbria', 10, 6677446),
                ('the-shelf', 86, u'The Shelf', u'Ruthin, Denbighshire', 6, 6696494),
                ('moel-arthur', 87, u'Moel Arthur', u'Llangwyfan, Denbighshire', 7, 6671074),
                ('penbarra', 88, u'Penbarra', u'Llanbedr-Dyffryn-Clwyd, Denbighshire', 9, 6671057),
                ('the-road-to-hell', 89, u'The Road to Hell', u'Denbigh, Denbighshire', 8, 6671093),
                ('horseshoe-pass', 90, u'Horseshoe Pass', u'Llangollen, Denbighshire', 7, 6671043),
                ('bwlch-y-groes', 91, u'Bwlch-y-Groes', u'Dinas Mawddwy, Gwynedd', 10, 6670984),
                ('ffordd-penllech', 92, u'Ffordd Penllech', u'Harlech, Gwynedd', 9, 6670845),
                ('devils-staircase', 93, u'Devil\'s Staircase', u'Abergwesyn, Powys', 9, 6670829),
                ('llangynidr-mountain', 94, u'Llangynidr Mountain', u'Llangydir, Powys', 7, 6665336),
                ('black-mountain', 95, u'Black Mountain', u'Llangadog, Carmarthenshire', 6, 6670907),
                ('bryn-du', 96, u'Bryn Du', u'Aberdale, Rhondda Cynon Taff', 7, 6670929),
                ('the-tumble', 97, u'The Tumble', u'Govilon, Monmouthshire', 7, 6665321),
                ('rhigos', 98, u'Rhigos', u'Hirwaun, Rhondda Cynon Taff', 6, 6670960),
                ('the-bwlch', 99, u'The Bwlch', u'Price Town, Bridgend', 5, 6697363),
                ('constitution-hill', 100, u'Constitution Hill', u'Swansea', 4, 6670867),
            ]
        },
        {
            'book': ('another',
                     u'Another 100 Greatest Cycling Climbs',
                     u'Another 100 Greatest Cycling Climbs: A Road Cyclist\'s Guide to Britain\'s Hills',
                     u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                     '/static/img/another-cover.jpg',
                     'http://www.franceslincoln.com/another-100-greatest-cycling-climbs'),
            'climbs': [
                ('gold-hill', 101, u'Gold Hill', u'Shaftesbury, Dorset', 7, 689528),
                ('zig-zag-hill', 102, u'Zig Zag Hill', u'Shaftesbury, Dorset', 4, 772570),
                ('park-hill', 103, u'Park Hill', u'Longleat, Dorset', 4, 700550),
                ('frocester-hill', 104, u'Frocester Hill', u'Frocester, Gloucestershire', 5, 667813),
            ]
        },
        {
            'book': ('hellingen',
                     u'Hellingen: Belgium\'s Greatest Cycling Climbs',
                     u'Hellingen: A Road Cyclist\'s Guide to Belgium\'s Greatest Cycling Climbs',
                     u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                     '/static/img/hellingen-cover.jpg',
                     'http://www.franceslincoln.com/hellingen'),
            'climbs': [
                ('kemmelberg', 1, u'Kemmelberg', u'Flanders', 1, 641316),
                ('mur-de-huy', 31, u'Mur de Huy', u'Wallonia', 1, 617076),
            ]
        },
        {
            'book': ('le-tour',
                     u'100 Greatest Cycling Climbs of the Tour de France',
                     u'100 Greatest Cycling Climbs of the Tour de France: A Cyclist\'s Guide to Riding the Mountains of the Tour',
                     u'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
                     '/static/img/le-tour-cover.jpg',
                     'http://www.franceslincoln.com/100-greatest-cycling-climbs-of-the-tour-de-france'),
            'climbs': [
                ('alpe-d-huez', 1, u'Alpe d\'Huez', u'Isère, France', 1, 661401),
                ('col-du-tourmalet', 2, u'Col Du Tourmalet', u'Midi-Pyrénées, France', 1, 652848),
            ]
        },
    ]

    for obj in fixtures:
        book = Book(*obj['book'])
        db.session.add(book)

        for climb in obj['climbs']:
            climb = Climb(*climb, book=book)
            db.session.add(climb)

    db.session.commit()

    fixtures = [
        {
            'region': ('south-west', u'South-west', 'd76e2c', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'cheddar-gorge',
                'weston-hill',
                'crowcombe-combe',
                'porlock',
                'dunkery-beacon',
                'exmoor-forest',
                'challacombe',
                'dartmeet',
                'haytor-vale',
                'widecombe',
                'rundlestone',
                'salcombe-hill',
                'dovers-hill',

                # Another 100 Greatest Cycling Climbs
                'gold-hill',
                'zig-zag-hill',
                'park-hill',
                'frocester-hill',
            ],
        },
        {
            'region': ('south-east', u'South-east', 'cc2228', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'box-hill',
                'yorks-hill',
                'white-lane',
                'leith-hill',
                'white-downs',
                'the-wall',
                'toys-hill',
                'steyning-bostal',
                'ditchling-beacon',
                'whiteleaf',
                'streatley-hill',
                'combe-gibbet',
                'mott-street',
                'swains-lane',
            ],
        },
        {
            'region': ('midlands', u'Midlands', 'b81188', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'michaelgate',
                'terrace-hill',
                'monsal-head',
                'bank-road',
                'riber',
                'winnats-pass',
                'rowsley-bar',
                'curbar-edge',
                'mow-cop',
                'peaslows',
                'jiggers-bank',
                'the-burway',
            ],
        },
        {
            'region': ('yorkshire', u'Yorkshire', '52318e', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'shibden-wall',
                'pea-royd-lane',
                'jackson-bridge',
                'holme-moss',
                'halifax-lane',
                'park-rash',
                'oxnop-scar',
                'malham-cove',
                'langcliffe-scar',
                'buttertubs',
                'fleet-moss',
                'tan-hill',
                'greenhow-hill',
                'norwood-edge',
                'boltby-bank',
                'rosedale-chimney',
                'white-horse-bank',
                'the-stang',
                'carlton-bank',
            ],
        },
        {
            'region': ('north-east', u'North-east', '2266af', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'crawleyside',
                'peth-bank',
                'winters-gibbet',
                'chapel-fell',
            ],
        },
        {
            'region': ('scotland', u'Scotland', '00acec', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'mennock-pass',
                'cairn-o-mount',
                'the-cairnwell',
                'the-lecht',
                'cairn-gorm',
                'rest-and-be-thankful',
                'bealach-na-ba',
            ],
        },
        {
            'region': ('north-west', u'North-west', '64b053', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'cat-and-fiddle',
                'swiss-hill',
                'the-rake',
                'garsdale-head',
                'nick-of-pendle',
                'trough-of-bowland',
                'jubilee-tower',
                'hartside',
                'lamps-moss',
                'cross-of-greet',
                'honister-pass',
                'newlands-hause',
                'whinlatter-pass',
                'kirkstone-pass',
                'hardknott-pass',
                'wrynose-pass',
            ],
        },
        {
            'region': ('wales', u'Wales', '37794b', 'ffffff'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'the-shelf',
                'moel-arthur',
                'penbarra',
                'the-road-to-hell',
                'horseshoe-pass',
                'bwlch-y-groes',
                'ffordd-penllech',
                'devils-staircase',
                'llangynidr-mountain',
                'black-mountain',
                'bryn-du',
                'the-tumble',
                'rhigos',
                'the-bwlch',
                'constitution-hill',
            ],
        },
        {
            'region': ('flanders', u'Flanders', 'ffe400', '000000'),
            'climbs': [
                # Hellingen: Belgium's Greatest Climbs
                'kemmelberg',
            ],
        },
        {
            'region': ('wallonia', u'Wallonia', 'b3cd0a', '000000'),
            'climbs': [
                # Hellingen: Belgium's Greatest Climbs
                'mur-de-huy',
            ],
        },
        {
            'region': ('alps', u'Alps', '0570B4', 'ffffff'),
            'climbs': [
                # 100 Greatest Tour de France Climbs
                'alpe-d-huez',
            ],
        },
        {
            'region': ('pyrenees', u'Pyrénées', 'e93639', 'ffffff'),
            'climbs': [
                # 100 Greatest Tour de France Climbs
                'col-du-tourmalet',
            ],
        },
    ]

    for obj in fixtures:
        region = Region(*obj['region'])
        db.session.add(region)

        for slug in obj['climbs']:
            climb = Climb.query.filter_by(slug=slug).first()
            climb.region = region
            db.session.add(climb)

    db.session.commit()
