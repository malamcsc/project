from dateutil.parser import parse
import datetime

def srrdate(str_date):
	return parse(str_date).strftime('%Y-%m-%d %H:%M:%S') + " " + 'IST'

def root(num):
	return num*num
