import json
import urllib
url = 'http://www.virustotal.com/vtapi/v2/ip-address/report'
parameters = {'ip': '74.125.34.46', 'apikey': '9eb947072e601590beafd95d1f2397f3b87550504458551de846ab7b5d0c6796'}
response = urllib.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
response_dict = json.loads(response)
print response_dict