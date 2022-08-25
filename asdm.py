import requests
requests.packages.urllib3.disable_warnings()
from base64 import b64encode
from getpass import getpass

un = 'admin'
pw = getpass('Password : ')
unpw = f'{un}:{pw}'
b = b64encode(unpw).decode()
auth = f'Basic {b}'
header = {
	'Authorization':	auth,
}

s = requests.Session()
s.headers.update(header)

host = 'asa01.domain.com'

command = 'show running-config'
payload = (
	f'<?xml version="1.0" encoding="ISO-8859-1"?>'
	f'<config-data config-action="merge" errors="continue">'
	f'<cli id="0">{command}</cli>'
	f'</config-data>'
)

url = f'https://{host}/admin/config'
r = s.post(url, data=payload, verify=False)
print('[I] Status : ',r.status_code)