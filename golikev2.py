import os,sys,re
import datetime
import json
import random
try:
  import requests
except ImportError:
  os.system('pip install requests')
else:
  pass
try:
  from colorama import Back, Fore, Fore, Style, init
except ImportError:
  os.system('pip install colorama')
else:
  pass
try:
  import time
except ImportError:
  os.system('pkg install time')
else:
  pass
try:
  from bs4 import BeautifulSoup
except ImportError:
  os.system('pip3 install beautifulsoup4')
else:
  pass
try:
    import platform
except ImportError:
    os.system('pip install platform')
else:
    pass
try:
    import webbrowser
except ImportError:
    os.system('pip install webbrowser')
else:
    pass
from colorama import Back, Fore, Fore, Style, init
import requests
from bs4 import BeautifulSoup
import time
from time import sleep
import json
os.system('clear')
 
init(autoreset=True)
xanh= "\033[1;96m"
xlacay ="\033[0;32m"
den="\033[1;90m"
do="\033[1;91m"
luc="\033[1;92m"
vang="\033[1;93m"
xduong="\033[1;94m"
hong="\033[1;95m"
trang="\033[1;97m"
vang="\033[1;93m"
syan="\033[1;36m"
luc = "\033[1;32m"
trang = "\033[1;37m"
do = "\033[1;31m"
vang = "\033[0;93m"
hong = "\033[1;35m"
xduong = "\033[1;34m"
lam = "\033[1;36m"
red='\u001b[31;1m'
yellow='\u001b[33;1m'
green='\u001b[32;1m'
blue='\u001b[34;1m'
tim='\033[1;35m'
xanhlam='\033[1;36m'
xam='\033[1;30m'
black='\033[1;19m'
import os,sys
from requests import session
from colorama import Fore, Style
import requests, random, re
from random import randint
import requests,pystyle
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from datetime import date
from datetime import datetime
from time import sleep
time=datetime.now().strftime("%H:%M:%S")
from pystyle import *
data_machine = []
today = date.today()
now = datetime.now()
thu = now.strftime("%A")
ngay_hom_nay = now.strftime("%d")
thang_nay = now.strftime("%m")
nam_ = now.strftime("%Y")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

# Kiểm tra kết nối internet
if check_internet_connection():
    print(f"{luc}Vui Lòng Chờ!!!")
    sleep(0.1)
else:
    print(f"{do}Vui Lòng Kiểm Tra Kết NốI!!!")
    sys.exit()
def get_location_by_ip():
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()

        city = data.get("city")
        region = data.get("region")
        country = data.get("country")
        loc = data.get("loc").split(",")
        latitude, longitude = loc if len(loc) == 2 else (None, None)

        return city, region, country, latitude, longitude
    except Exception as e:
        print(f"Lỗi: {e}")
        return None, None, None, None, None
city, region, country, latitude, longitude = get_location_by_ip()
def get_weather():
    try:
        # Lấy thông tin vị trí từ dịch vụ ipinfo.io
        response = requests.get("https://ipinfo.io")
        data = response.json()
        location = data.get("loc").split(",")
        latitude, longitude = location
        # Lấy thông tin thời tiết từ trang web công cộng
        base_url = f"https://wttr.in/{latitude},{longitude}?format=%t"
        response = requests.get(base_url)
        weather_description = response.text.strip()
        return weather_description
    except Exception as e:
        print(f"Lỗi: {e}")
        return None
weather_description = get_weather()
System.Clear()

def pr3(text):
  lines = text.split('\n')
  for line in lines:
      sys.stdout.write(line+'\n')
      sys.stdout.flush()
      sleep(0.1)
def pr(text):
  for i in range(len(text)+1):
      sys.stdout.write("\r" + text[:i])
      sys.stdout.flush()
      sleep(0.01)
  print()

def time():
  current_time = datetime.datetime.now()

  time = current_time.strftime("%M:%S")
  return time





def changetoken(red,green,white):
  if not os.path.exists("cache_golike_auth.txt"):
   pass
  else:
    text=f'''{green}BẠN MUỐN DÙNG AUTH CŨ HAY ĐỔI AUTH
{red}[{vang}1{red}] ĐỔI AUTH
{red}[{vang}2{red}] DÙNG AUTH CŨ'''
    pr3(text)
    changetoken=int(input(f'{red}NHẬP LỰA CHỌN: {green}'))
    if changetoken==1:
      file_name = 'cache_golike_auth.txt'
      if os.path.exists(file_name):
          os.remove(file_name)
    else:
      pass
      


def banner(red,green,blue,yellow,cyan,pink):
  text=f"""    
\033[1;34m┌═════════════════════════════════════════════════════════════════════════════┐
\033[1;31m █████╗ ████████╗ █████╗ ███╗   ███╗  ████████╗ █████╗  █████╗ ██╗
\033[1;33m██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║  ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;34m███████║   ██║   ██║  ██║██╔████╔██║     ██║   ██║  ██║██║  ██║██║
\033[1;35m██╔══██║   ██║   ██║  ██║██║╚██╔╝██║     ██║   ██║  ██║██║  ██║██║
\033[1;36m██║  ██║   ██║   ╚█████╔╝██║ ╚═╝ ██║     ██║   ╚█████╔╝╚█████╔╝███████╗
\033[1;32m╚═╝  ╚═╝   ╚═╝    ╚════╝ ╚═╝     ╚═╝     ╚═╝    ╚════╝  ╚════╝ ╚══════╝
\033[1;34m┠═════════════════════════════════════════════════════════════════════════════┨
\033[1;34m ➯ Cre : \033[1;31mATOM TOOL
\033[1;34m ➯ Nhóm Zalo : \033[1;37mhttps://zalo.me/g/pdsvkf650
\033[1;34m ➯ Facebook Hoàng Nam : \033[1;37mhttps://facebook.com/nam.nhn131
\033[1;34m ➯ Facebook Bảo Nam : \033[1;37mhttps://facebook.com/61553720436598                               
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
\033[1;34m ➯ Loại Tool: \033[1;37mGolike V2
\033[1;34m└═════════════════════════════════════════════════════════════════════════════┘
{do} ➩ {trang}Ngày{trang} : {vang}{ngay_hom_nay}{lam} |{trang} Tháng{trang}: {vang}{thang_nay} {lam}| {trang}Năm{trang}: {vang}{nam_}{lam} | {trang}Thời Gian: {vang}{time}
{do} ➩ {trang}Thành Phố : {vang}{city} {lam}|{trang} Khu Vực: {vang}{region} {lam}| {trang} Quốc gia: {vang}{country} {lam}| {trang} Tọa độ: {vang}{latitude}, {longitude} {lam}| {trang} Nhiệt độ: {vang}{weather_description}"""
  pr3(text)




def checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    if not os.path.exists("cache_golike_auth.txt"):
      auth=str(input(f'~[+]{trang}NHẬP AUTH:{vang} '))
      headers ={
    'Authorization'	:auth,
    't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
 }
      check=requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).json()
      if check['status']==200:
              name=check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).json()
              #data = json.loads(json_string)
              
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'~[+]{luc}SUCCESS'
              text=f'{lam}TÊN TÀI KHOẢN: {vang} {name}'
              pr(text)
              text=f'{lam}XU HIỆN TẠI :{vang}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{lam}XU CHỜ DUYỆT:{vang}{total_pending_coin}'
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{trang}SELECT {pink}ACC CHẠY NHIỆM VỤ '
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{vang}{i}{red}]: {hong}{globals()[f"{i}"]}'
                  pr(text)
              with open("cache_golike_auth.txt", "w") as state_file:
                state_file.write(auth)
              return auth,check
      else:
        text=f'~[+]{red}FAIL AUTH KHÔNG CHÍNH XÁC>>{green}VUI LÒNG NHẬP LẠI'
        continue 
    else:
        with open('cache_golike_auth.txt') as f:
            lines = f.readlines()
            auth=lines[0]
            headers ={
          'Authorization'	:auth,
          't':	'VFZSWk5VOUVVVEJQUkZGNFRXYzlQUT09',
}
            check=requests.get('https://gateway.golike.net/api/tiktok-account',headers=headers).json()
            if check['status']==200:
              name =check['data'][0]['username']
              hea={
'Authorization':auth
}
# Chuỗi JSON đầu vào
              data=requests.get('https://gateway.golike.net/api/statistics/report',headers=hea).json()
              #data = json.loads(json_string)
              
              # Tính tổng pending coin
              total_pending_coin = 0
              for key, value in data.items():
                  if isinstance(value, dict) and 'pending_coin' in value:
                      total_pending_coin += value['pending_coin']
              xht=data['current_coin']
              text=f'{trang}TÊN TÀI KHOẢN: {lam} {name}'
              pr(text)
              text=f'{trang}XU HIỆN TẠI :{lam}{xht}'
              pr(text)
              # In tổng pending coin
              text=f'{trang}XU CHỜ DUYỆT:{lam}{total_pending_coin}'
              pr(text)
              nicknames = [item['nickname'] for item in check['data'] if 'nickname' in item]
              for i, nickname in enumerate(nicknames, start=1):
                  globals()[f'{i}'] = nickname
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              text=f'~[+]{lam}SELECT {xduong}ACC CHẠY NHIỆM VỤ '
              pr(text)
              # In giá trị của các biến
              for i, nickname in enumerate(nicknames, start=1):
                  text=f'{red}[{vang}{i}{red}]: {luc}{globals()[f"{i}"]}'
                  pr(text)
                  
            return auth, check




def get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  while True :
    
    user_input=input(f'~[+]{random.choice(ranmau)}>{random.choice(ranmau)}>{random.choice(ranmau)}> {green}CHỌN ACC TIKTOK MUỐN CHẠY JOB:{green} ')
    try:
      n = int(user_input)
      if 'data' in check and len(check['data']) >= n:
          idtiktok = check['data'][n-1]['id']
          if idtiktok :
              text=f"{trang}ID CỦA NICKNAME SỐ {n} LÀ: {vang}{idtiktok}"
              pr(text)
              print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
              return idtiktok 
          else:
              text=f"{red}KHÔNG TÌM THẤY NICKNAME TƯƠNG ỨNG."
              pr(text)
      else:
          continue 
    except ValueError:
          pr(f"{red}VUI LÒNG CHỈ NHẬP SỐ.")
          continue 
def getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink):
  startmaxjob=1
  while True :
    hea={
    'Authorization':	auth,
    't':	'VFZSWk5VOUVUWHBOVkUxM1QwRTlQUT09'
}
    a=requests.get(f'https://gateway.golike.net/api/advertising/publishers/tiktok/jobs?account_id={idtiktok}&data=null',headers=hea).json()
    link=a['data']['link']
    id=a['data']['id']
    object_id=a['lock']['object_id']
    os.system(f'termux-open-url {link}')
    
    for k in range(delay,-1,-1):
      mau=random.choice(ranmau)
      print(f'{random.choice(ranmau)}LOADING  {random.choice(ranmau)}>>  {yellow}NVỤ MỚI SAU  {random.choice(ranmau)}>>  {random.choice(ranmau)}[{k}s]',end='\r')
      sleep(1)
    headers = {
        'authorization': auth,
        't': 'VFZSWk5VOUVUVFZOVkZsNVRrRTlQUT09',
}
    
    json_data = {
        'ads_id': id,
        'account_id': idtiktok ,
        'async': True,
        'data': None,
    }
    
    g = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
        headers=headers,
        json=json_data,
    ).json()
    
    if g['status']==200:
      print(f'{green}[{startmaxjob}]{cyan} [{time()}] | {random.choice(ranmau)}SUCCESS |  {green}FOLLOW | {yellow}+{xuthem(auth)}đ')
      startmaxjob+=1
      if startmaxjob == maxjob+1:
        print(f'~[+]{pink}ĐÃ ĐẠT MAX JOB. ')
        return
    if g['status'] !=200:
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVVWGhQVkZFeFRsRTlQUT09',
      }
      
      json_data = {
          'description': 'Báo cáo hoàn thành thất bại',
          'users_advertising_id': id,
          'type': 'ads',
          'provider': 'tiktok',
          'fb_id': idtiktok ,
          'error_type': 3,
      }
      
      requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data).json()
     
      
      headers = {
          'authorization': auth,
          't': 'VFZSWk5VOUVVWGhQVkZFeFQwRTlQUT09',
 }
      
      json_data = {
          'ads_id': id,
          'object_id': object_id,
          'account_id': idtiktok ,
          'type': 'follow',
      }
      skipjob=requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
          headers=headers,
          json=json_data,
      ).json()
      print(f'{green}[{startmaxjob}] {cyan}[{time()}] {end}| {random.choice(ranmau)}  FAIL  {end}|{green} FOLLOW  {end}| {red}ĐÃ BỎ QUA JOB')
      startmaxjob+=1
      if startmaxjob == maxjob+1:
        print(f'~[+]{green}ĐÃ ĐẠT MAX JOB')
        return 




  
  


  
  
  
  
  
  
def xuthem(auth):
  headers = {
      'authorization': auth,
  }
  
  params = {
      'page': '1',
  }
  xu = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/logs', params=params, headers=headers).json()
  if xu['status']==200:
                a = [item['prices'] for item in xu['data'] if 'prices' in item]
                a=a[0]
                return a
  
  
  
  
  
  
  




  
  
  
  
  
#biến
#green='\033[38;5;10m'
blue='\033[38;5;12m'
cyan='\033[38;5;14m'
white='\033[1;39m'
magenta='\033[38;5;5m'
orange='\033[38;5;202m'
xanhnhat = "\033[1;36m"
red = "\033[1;31m"
green = "\033[1;32m"
yellow = "\033[1;33m"
xduong = "\033[1;34m"
pink = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
redb="\033[1;31m"
end='\033[0m'
ranmau=(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)


banner(red,green,blue,yellow,cyan,pink)
print(f'{pink}VERSION 2.0')
changetoken(red,green,white) 
auth,check =checkauth(red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
  
idtiktok =get_id_from_nickname_number(ranmau,check,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
delay =int(input(f'~[+]{red}NHẬP DELAY: {green}'))
maxjob= int(input(f'~[+]{red}NHẬP MAX JOB: {green}'))
print(f'{cyan}KHỞI CHẠY NHIỆM VỤ',end='\r')
sleep(1)
getjob(maxjob,delay,auth,idtiktok,red,blue,green,yellow,cyan,magenta,orange,xanhnhat,xduong,pink)
