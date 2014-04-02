from emilia.climbs.models import Book, Climb, Region
from emilia.extensions import db


def install():
    """ Adds Book, Climb and Region data to database. """
    fixtures = [
        {
            'book': ("greatest",
                     "100 Greatest Cycling Climbs",
                     "100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                ("cheddar-gorge", 1, "Cheddar Gorge", "Cheddar, Somerset", 6665302),
                ("weston-hill", 2, "Weston Hill", "Weston, Bath", 6665281),
                ("crowcombe-combe", 3, "Crowcombe Combe", "Crowcombe, Somerset", 6665343),
                ("porlock", 4, "Porlock", "Porlock, Somerset", 6665361),
                ("dunkery-beacon", 5, "Dunkery Beacon", "South-West", 6665334),
                ("exmoor-forest", 6, "Exmoor Forest", "South-West", 6665364),
                ("challacombe", 7, "Challacombe", "South-West", 6665368),
                ("dartmeet", 8, "Dartmeet", "South-West", 6665214),
                ("haytor-vale", 9, "Haytor Vale", "South-West", 6665314),
                ("widecombe", 10, "Widecombe", "South-West", 6665221),
                ("rundlestone", 11, "Rundlestone", "South-West", 6665277),
                ("salcombe-hill", 12, "Salcombe Hill", "South-West", 6691752),
                ("dovers-hill", 13, "Dover's Hill", "South-West", 6681432),
                ("box-hill", 14, "Box Hill", "South-East", 6695759),
                ("yorks-hill", 15, "York's Hill", "South-East", 6691251),
                ("white-lane", 16, "White Lane", "South-East", 6691229),
                ("leith-hill", 17, "Leith Hill", "South-East", 6691321),
                ("white-downs", 18, "White Downs", "South-East", 6691301),
                ("the-wall", 19, "The Wall", "South-East", 6691343),
                ("toys-hill", 20, "Toys Hill", "South-East", 6691062),
                ("steyning-bostal", 21, "Steyning Bostal", "South-East", 6691367),
                ("ditchling-beacon", 22, "Ditchling Beacon", "South-East", 6691384),
                ("whiteleaf", 23, "Whiteleaf", "South-East", 6681416),
                ("streatley-hill", 24, "Streatley Hill", "South-East", 6665255),
                ("combe-gibbet", 25, "Combe Gibbet", "South-East", 6665230),
                ("mott-street", 26, "Mott Street", "South-East", 6691219),
                ("swains-lane", 27, "Swains Lane", "South-East", 6691038),
                ("michaelgate", 28, "Michaelgate", "Midlands", 6691237),
                ("terrace-hill", 29, "Terrace Hill", "Midlands", 6691047),
                ("monsal-head", 30, "Monsal Head", "Midlands", 6687943),
                ("bank-road", 31, "Bank Road", "Midlands", 6677679),
                ("riber", 32, "Riber", "Midlands", 6677656),
                ("winnats-pass", 33, "Winnats Pass", "Midlands", 6698034),
                ("rowsley-bar", 34, "Rowsley Bar", "Midlands", 6681397),
                ("curbar-edge", 35, "Curbar Edge", "Midlands", 6687953),
                ("mow-cop", 36, "Mow Cop", "Midlands", 6687912),
                ("peaslows", 37, "Peaslows", "Midlands", 6820230),
                ("jiggers-bank", 38, "Jiggers Bank", "Midlands", 6681373),
                ("the-burway", 39, "The Burway", "Midlands", 6681340),
                ("shibden-wall", 40, "Shibden Wall", "Yorkshire", 6690966),
                ("pea-royd-lane", 41, "Pea Royd Lane", "Yorkshire", 6697336),
                ("jackson-bridge", 42, "Jackson Bridge", "Yorkshire", 6691287),
                ("holme-moss", 43, "Holme Moss", "Yorkshire", 6691272),
                ("halifax-lane", 44, "Halifax Lane", "Yorkshire", 6690955),
                ("park-rash", 45, "Park Rash", "Yorkshire", 6687990),
                ("oxnop-scar", 46, "Oxnop Scar", "Yorkshire", 6688073),
                ("malham-cove", 47, "Malham Cove", "Yorkshire", 6688083),
                ("langcliffe-scar", 48, "Langcliffe Scar", "Yorkshire", 6688008),
                ("buttertubs", 49, "Buttertubs", "Yorkshire", 6697314),
                ("fleet-moss", 50, "Fleet Moss", "Yorkshire", 6687966),
                ("tan-hill", 51, "Tan Hill. ", "Yorkshire", 6661216),
                ("greenhow-hill", 52, "Greenhow Hill", "Yorkshire", 6690987),
                ("norwood-edge", 53, "Norwood Edge", "Yorkshire", 6691028),
                ("boltby-bank", 54, "Boltby Bank", "Yorkshire", 6696481),
                ("rosedale-chimney", 55, "Rosedale Chimney", "Yorkshire", 6690945),
                ("white-horse-bank", 56, "White Horse Bank", "Yorkshire", 6690931),
                ("the-stang", 57, "The Stang", "Yorkshire", 6691007),
                ("carlton-bank", 58, "Carlton Bank", "Yorkshire", 6691019),
                ("crawleyside", 59, "Crawleyside", "North-East", 6681219),
                ("peth-bank", 60, "Peth Bank", "North-East", 6681185),
                ("winters-gibbet", 61, "Winters Gibbet", "North-East", 6677593),
                ("chapel-fell", 62, "Chapel Fell", "North-East", 6678141),
                ("mennock-pass", 63, "Mennock Pass", "Scotland", 6697054),
                ("cairn-o-mount", 64, "Cairn o' Mount", "Scotland", 6674408),
                ("the-cairnwell", 65, "The Cairnwell", "Scotland", 6674420),
                ("the-lecht", 66, "The Lecht", "Scotland", 6674394),
                ("cairn-gorm", 67, "Cairn Gorm", "Scotland", 6674377),
                ("rest-and-be-thankfull", 68, "Rest and be Thankfull", "Scotland", 6697031),
                ("bealach-na-ba", 69, "Bealach-na-Ba", "Scotland", 6671117),
                ("cat-and-fiddle", 70, "Cat and Fiddle", "Nort-West", 6681311),
                ("swiss-hill", 71, "Swiss Hill", "Nort-West", 6687924),
                ("the-rake", 72, "The Rake", "Nort-West", 6688059),
                ("garsdale-head", 73, "Garsdale Head", "Nort-West", 6677557),
                ("nick-of-pendle", 74, "Nick of Pendle", "Nort-West", 6688055),
                ("trough-of-bowland", 75, "Trough of Bowland", "Nort-West", 6688001),
                ("jubilee-tower", 76, "Jubilee Tower", "Nort-West", 6688053),
                ("hartside", 77, "Hartside", "Nort-West", 6681248),
                ("lamps-moss", 78, "Lamps Moss", "Nort-West", 6687980),
                ("cross-of-greet", 79, "Cross of Greet", "Nort-West", 6688035),
                ("honister-pass", 80, "Honister Pass", "Nort-West", 6677352),
                ("newlands-hause", 81, "Newlands Hause", "Nort-West", 6677326),
                ("whinlatter-pass", 82, "Whinlatter Pass", "Nort-West", 6695737),
                ("kirkstone-pass", 83, "Kirkstone Pass", "Nort-West", 6677526),
                ("hardknott-pass", 84, "Hardknott Pass", "Nort-West", 6677392),
                ("wrynose-pass", 85, "Wrynose Pass", "Nort-West", 6677446),
                ("the-shelf", 86, "The Shelf", "Wales", 6696494),
                ("moel-arthur", 87, "Moel Arthur", "Wales", 6671074),
                ("penbarra", 88, "Penbarra", "Wales", 6671057),
                ("the-road-to-hell", 89, "The Road to Hell", "Wales", 6671093),
                ("horseshoe-pass", 90, "Horseshoe Pass", "Wales", 6671043),
                ("bwlch-y-groes", 91, "Bwlch-y-Groes", "Wales", 6670984),
                ("ffordd-penllech", 92, "Ffordd Penllech", "Wales", 6670845),
                ("devils-staircase", 93, "Devil's Staircase", "Wales", 6670829),
                ("llangynidr-mountain", 94, "Llangynidr Mountain", "Wales", 6665336),
                ("black-mountain", 95, "Black Mountain", "Wales", 6670907),
                ("bryn-du", 96, "Bryn Du", "Wales", 6670929),
                ("the-tumble", 97, "The Tumble", "Wales", 6665321),
                ("rhigos", 98, "Rhigos", "Wales", 6670960),
                ("the-bwlch", 99, "The Bwlch", "Wales", 6697363),
                ("constitution-hill", 100, "Constitution Hill", "Wales", 6670867),
            ]
        },
        {
            'book': ("another",
                     "Another 100 Greatest Cycling Climbs",
                     "Another 100 Greatest Cycling Climbs: A Road Cyclist's Guide to Britain's Hills"),
            'climbs': [
                ("gold-hill", 101, "Gold Hill", "Shaftesbury, Dorset", 944629),
                ("zig-zag-hill", 102, "Zig Zag Hill", "Shaftesbury, Dorset", 944629),
                ("park-hill", 103, "Park Hill", "Longleat, Dorset", 944629),
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
            'region': ('south-west', 'South-west'),
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
            ],
        },
        {
            'region': ('south-east', 'South-east'),
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
            'region': ('midlands', 'Midlands'),
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
            'region': ('yorkshire', 'Yorkshire'),
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
            'region': ('north-east', 'North-east'),
            'climbs': [
                # 100 Greatest Cycling Climbs
                'crawleyside',
                'peth-bank',
                'winters-gibbet',
                'chapel-fell',
            ],
        },
        {
            'region': ('scotland', 'Scotland'),
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
            'region': ('nort-west', 'Nort-West'),
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
            'region': ('wales', 'Wales'),
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
    ]

    for obj in fixtures:
        region = Region(*obj['region'])
        db.session.add(region)

        for slug in obj['climbs']:
            climb = Climb.query.filter_by(slug=slug).first()
            climb.region = region
            db.session.add(climb)

    db.session.commit()
