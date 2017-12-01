import requests
import json
import sys
import time
import logging

session_id = 10108274
first_photo = 100000
last_photo =  103000
cookie = {'PHPSESSID': 's3dmsckqr507knckkpdj9jamv1'}
logging.basicConfig(filename='log.txt', level=logging.INFO, format='[%(asctime)s] - %(levelname)s - %(message)s', datefmt='%H:%M:%S')

def session_get(session, url):
	ok = 1
	while ok == 1:
		try:
        		answer = requests.get(url, cookies = cookie, timeout = 5)
			ok = 0
		except:
			#print 'retry...'
			logging.info('retry...')
#	print answer.content
        if answer.status_code == 429:
            #print "Too many requests"
	    logging.error('Too many requests')
        else:
            return answer

headers = {
	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.130 Chrome/43.0.2357.130 Safari/537.36',
	'PHPSESSID': 's3dmsckqr507knckkpdj9jamv1',
	'__zlcmid': 'jigvmwr98lTn7C',
	'_ga': 'GA1.2.857241181.1511902356',
}

session = requests.Session()

number = 1
for number in range(first_photo,last_photo):
	address = 'http://zalamo.com/resizer.php?size=400x400&nocrop=1&file=' + str(number) + '&module=client&controller=session&action=edit&single_session_id=' + str(session_id)
	print '[', number, ' z 125] ', address
	logging.info('[%s z 125] %s' % (number, address))
	response = session_get(session, address)
	print response.status_code
	logging.info(response.status_code)
	path = 'photos/' + str(number) + '.jpg'
	with open(path, 'wb') as file_:
		file_.write(response.content)
	number += 1

logging.info('END')
