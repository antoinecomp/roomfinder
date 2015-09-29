from datetime import datetime
SPAREROOM_COOKIES = {'session_id': '00000000', 'session_key': '000000000000000'}

#WHEN = datetime.strptime("2015-03-01 00:00:00", "%Y-%m-%d %H:%M:%S")
WHEN = datetime.now()
MIN_AVAILABLE_TIME = datetime.strptime("2014-12-01 00:00:00", "%Y-%m-%d %H:%M:%S")
MAX_RENT_PM = 750
FOR = 'males'
TYPE = 'double'

AREAS = ['Paddington', 'Marble Arch', 'Baker Street', 'Oxford Circus', 'Picadilly Circus']

SPAREROOM_PREF_IDS = ['1234567', '1234566', '0000000']

FIELDS = ['score', 'id', 'images', 'prices', 'search', 'available', 'phone']

MARK_OLD = False # True: mark rooms already fetched as old and doesn't show on report

MAX_RESULTS = 20 # max results asked in each request

SLEEP = 1 # time to sleep in sec between requests