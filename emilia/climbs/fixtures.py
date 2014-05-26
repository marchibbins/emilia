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
                ('cheddar-gorge', 1, u'Cheddar Gorge', u'Cheddar, Somerset', 6665302),
                ('weston-hill', 2, u'Weston Hill', u'Weston, Bath', 6665281),
                ('crowcombe-combe', 3, u'Crowcombe Combe', u'Crowcombe, Somerset', 6665343),
                ('porlock', 4, u'Porlock', u'Porlock, Somerset', 6665361),
                ('dunkery-beacon', 5, u'Dunkery Beacon', u'South-West', 6665334),
                ('exmoor-forest', 6, u'Exmoor Forest', u'South-West', 6665364),
                ('challacombe', 7, u'Challacombe', u'South-West', 6665368),
                ('dartmeet', 8, u'Dartmeet', u'South-West', 6665214),
                ('haytor-vale', 9, u'Haytor Vale', u'South-West', 6665314),
                ('widecombe', 10, u'Widecombe', u'South-West', 6665221),
                ('rundlestone', 11, u'Rundlestone', u'South-West', 6665277),
                ('salcombe-hill', 12, u'Salcombe Hill', u'South-West', 6691752),
                ('dovers-hill', 13, u'Dover\'s Hill', u'South-West', 6681432),
                ('box-hill', 14, u'Box Hill', u'South-East', 6695759),
                ('yorks-hill', 15, u'York\'s Hill', u'South-East', 6691251),
                ('white-lane', 16, u'White Lane', u'South-East', 6691229),
                ('leith-hill', 17, u'Leith Hill', u'South-East', 6691321),
                ('white-downs', 18, u'White Downs', u'South-East', 6691301),
                ('the-wall', 19, u'The Wall', u'South-East', 6691343),
                ('toys-hill', 20, u'Toys Hill', u'South-East', 6691062),
                ('steyning-bostal', 21, u'Steyning Bostal', u'South-East', 6691367),
                ('ditchling-beacon', 22, u'Ditchling Beacon', u'South-East', 6691384),
                ('whiteleaf', 23, u'Whiteleaf', u'South-East', 6681416),
                ('streatley-hill', 24, u'Streatley Hill', u'South-East', 6665255),
                ('combe-gibbet', 25, u'Combe Gibbet', u'South-East', 6665230),
                ('mott-street', 26, u'Mott Street', u'South-East', 6691219),
                ('swains-lane', 27, u'Swains Lane', u'South-East', 6691038),
                ('michaelgate', 28, u'Michaelgate', u'Midlands', 6691237),
                ('terrace-hill', 29, u'Terrace Hill', u'Midlands', 6691047),
                ('monsal-head', 30, u'Monsal Head', u'Midlands', 6687943),
                ('bank-road', 31, u'Bank Road', u'Midlands', 6677679),
                ('riber', 32, u'Riber', u'Midlands', 6677656),
                ('winnats-pass', 33, u'Winnats Pass', u'Midlands', 6698034),
                ('rowsley-bar', 34, u'Rowsley Bar', u'Midlands', 6681397),
                ('curbar-edge', 35, u'Curbar Edge', u'Midlands', 6687953),
                ('mow-cop', 36, u'Mow Cop', u'Midlands', 6687912),
                ('peaslows', 37, u'Peaslows', u'Midlands', 6820230),
                ('jiggers-bank', 38, u'Jiggers Bank', u'Midlands', 6681373),
                ('the-burway', 39, u'The Burway', u'Midlands', 6681340),
                ('shibden-wall', 40, u'Shibden Wall', u'Yorkshire', 6690966),
                ('pea-royd-lane', 41, u'Pea Royd Lane', u'Yorkshire', 6697336),
                ('jackson-bridge', 42, u'Jackson Bridge', u'Yorkshire', 6691287),
                ('holme-moss', 43, u'Holme Moss', u'Yorkshire', 6691272),
                ('halifax-lane', 44, u'Halifax Lane', u'Yorkshire', 6690955),
                ('park-rash', 45, u'Park Rash', u'Yorkshire', 6687990),
                ('oxnop-scar', 46, u'Oxnop Scar', u'Yorkshire', 6688073),
                ('malham-cove', 47, u'Malham Cove', u'Yorkshire', 6688083),
                ('langcliffe-scar', 48, u'Langcliffe Scar', u'Yorkshire', 6688008),
                ('buttertubs', 49, u'Buttertubs', u'Yorkshire', 6697314),
                ('fleet-moss', 50, u'Fleet Moss', u'Yorkshire', 6687966),
                ('tan-hill', 51, u'Tan Hill. ', u'Yorkshire', 6661216),
                ('greenhow-hill', 52, u'Greenhow Hill', u'Yorkshire', 6690987),
                ('norwood-edge', 53, u'Norwood Edge', u'Yorkshire', 6691028),
                ('boltby-bank', 54, u'Boltby Bank', u'Yorkshire', 6696481),
                ('rosedale-chimney', 55, u'Rosedale Chimney', u'Yorkshire', 6690945),
                ('white-horse-bank', 56, u'White Horse Bank', u'Yorkshire', 6690931),
                ('the-stang', 57, u'The Stang', u'Yorkshire', 6691007),
                ('carlton-bank', 58, u'Carlton Bank', u'Yorkshire', 6691019),
                ('crawleyside', 59, u'Crawleyside', u'North-East', 6681219),
                ('peth-bank', 60, u'Peth Bank', u'North-East', 6681185),
                ('winters-gibbet', 61, u'Winters Gibbet', u'North-East', 6677593),
                ('chapel-fell', 62, u'Chapel Fell', u'North-East', 6678141),
                ('mennock-pass', 63, u'Mennock Pass', u'Scotland', 6697054),
                ('cairn-o-mount', 64, u'Cairn o\' Mount', u'Scotland', 6674408),
                ('the-cairnwell', 65, u'The Cairnwell', u'Scotland', 7011208),
                ('the-lecht', 66, u'The Lecht', u'Scotland', 6674394),
                ('cairn-gorm', 67, u'Cairn Gorm', u'Scotland', 6674377),
                ('rest-and-be-thankfull', 68, u'Rest and be Thankfull', u'Scotland', 6697031),
                ('bealach-na-ba', 69, u'Bealach-na-Ba', u'Scotland', 6671117),
                ('cat-and-fiddle', 70, u'Cat and Fiddle', u'North-West', 6681311),
                ('swiss-hill', 71, u'Swiss Hill', u'North-West', 6687924),
                ('the-rake', 72, u'The Rake', u'North-West', 6688059),
                ('garsdale-head', 73, u'Garsdale Head', u'North-West', 6677557),
                ('nick-of-pendle', 74, u'Nick of Pendle', u'North-West', 6688055),
                ('trough-of-bowland', 75, u'Trough of Bowland', u'North-West', 6688001),
                ('jubilee-tower', 76, u'Jubilee Tower', u'North-West', 6688053),
                ('hartside', 77, u'Hartside', u'North-West', 6681248),
                ('lamps-moss', 78, u'Lamps Moss', u'North-West', 6687980),
                ('cross-of-greet', 79, u'Cross of Greet', u'North-West', 6688035),
                ('honister-pass', 80, u'Honister Pass', u'North-West', 6677352),
                ('newlands-hause', 81, u'Newlands Hause', u'North-West', 6677326),
                ('whinlatter-pass', 82, u'Whinlatter Pass', u'North-West', 6695737),
                ('kirkstone-pass', 83, u'Kirkstone Pass', u'North-West', 6677526),
                ('hardknott-pass', 84, u'Hardknott Pass', u'North-West', 6677392),
                ('wrynose-pass', 85, u'Wrynose Pass', u'North-West', 6677446),
                ('the-shelf', 86, u'The Shelf', u'Wales', 6696494),
                ('moel-arthur', 87, u'Moel Arthur', u'Wales', 6671074),
                ('penbarra', 88, u'Penbarra', u'Wales', 6671057),
                ('the-road-to-hell', 89, u'The Road to Hell', u'Wales', 6671093),
                ('horseshoe-pass', 90, u'Horseshoe Pass', u'Wales', 6671043),
                ('bwlch-y-groes', 91, u'Bwlch-y-Groes', u'Wales', 6670984),
                ('ffordd-penllech', 92, u'Ffordd Penllech', u'Wales', 6670845),
                ('devils-staircase', 93, u'Devil\'s Staircase', u'Wales', 6670829),
                ('llangynidr-mountain', 94, u'Llangynidr Mountain', u'Wales', 6665336),
                ('black-mountain', 95, u'Black Mountain', u'Wales', 6670907),
                ('bryn-du', 96, u'Bryn Du', u'Wales', 6670929),
                ('the-tumble', 97, u'The Tumble', u'Wales', 6665321),
                ('rhigos', 98, u'Rhigos', u'Wales', 6670960),
                ('the-bwlch', 99, u'The Bwlch', u'Wales', 6697363),
                ('constitution-hill', 100, u'Constitution Hill', u'Wales', 6670867),
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
                ('gold-hill', 101, u'Gold Hill', u'Shaftesbury, Dorset', 689528),
                ('zig-zag-hill', 102, u'Zig Zag Hill', u'Shaftesbury, Dorset', 772570),
                ('park-hill', 103, u'Park Hill', u'Longleat, Dorset', 700550),
                ('frocester-hill', 104, u'Frocester Hill', u'Frocester, Gloucestershire', 667813),
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
                ('kemmelberg', 1, u'Kemmelberg', u'Flanders', 641316),
                ('mur-de-huy', 31, u'Mur de Huy', u'Wallonia', 617076),
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
                ('alpe-d-huez', 1, u'Alpe d\'Huez', u'Isère, France', 661401),
                ('col-du-tourmalet', 2, u'Col Du Tourmalet', u'Midi-Pyrénées, France', 652848),
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
                'rest-and-be-thankfull',
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
