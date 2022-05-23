import json
import requests
import sys
import re
from datetime import datetime
from bs4 import BeautifulSoup

if len(sys.argv) != 3:
    print ("enter USERNAME PASSWORD as arguments")

# obligé d'utiliser selenium pour se connecter à instagram ??

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"

# def login(username, password):
#     """Login to Instagram"""

#     time = str(int(datetime.datetime.now().timestamp()))
#     enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"

#     session = requests.Session()
#     # set a cookie that signals Instagram the "Accept cookie" banner was closed
#     session.cookies.set("ig_cb", "2")
#     session.headers.update({'user-agent': user_agent})
#     session.headers.update({'Referer': 'https://www.instagram.com'})
#     res = session.get('https://www.instagram.com')

#     csrftoken = None

#     for key in res.cookies.keys():
#         if key == 'csrftoken':
#             csrftoken = session.cookies['csrftoken']

#     session.headers.update({'X-CSRFToken': csrftoken})
#     login_data = {'username': username, 'enc_password': enc_password}

#     login = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data, allow_redirects=True)
#     session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})

#     cookies = login.cookies
#     print(login.text)

#     session.close()

# insta = login(sys.argv[1], sys.argv[2] )

# url = 'https://www.instagram.com/gianni_coffey/'

# def login(mail, password):
#     s = requests.Session()
#     payload = {
#         'email' : mail,
#         'password' : password
#     }
#     res = s.post('')

# response = requests.get(url)
# if response.ok:
#     soup = BeautifulSoup(response.text, "html.parser")

# f = open("./log.html", "w")

# script = soup.find_all("script", {"type": "text/javascript"})[3].text

# f.write(str(response.text))

# print (soup.find_all("meta"))

# raw_data = script.replace(';', '').replace('window._sharedData = ', '')

# jsondata = json.loads(raw_data)

# user_data = jsondata['entry_data']['LoginAndSignupPage']

# print (user_data)
