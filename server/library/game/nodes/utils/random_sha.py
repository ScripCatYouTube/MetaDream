from hashlib import sha256
from datetime import datetime

def get_string_time():
	now_time = datetime.now()

	return now_time.strftime('%f:%X-%x.%z.%Z.%j')


def get_sha_string(string_time):
	return sha256( string_time.encode('utf-8') ).hexdigest()

def get_name_file(end = '.json'):
	return get_sha_string( get_string_time() ) + end