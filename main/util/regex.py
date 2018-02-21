import re

def find_number_in_string(regex):
	return int(re.findall('\d+', regex)[0])