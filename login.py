# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import time
import Image
from pytesser import pytesser
import os
import json
from globalVal import *


def get_xsrf():
    """
    Get the parameter : _xsrf
    """
    req = s.get(url, headers=headers)
    print req

    soup = BeautifulSoup(req.text, 'html.parser')
    xsrf = soup.find('input', {'name':'_xsrf', 'type':'hidden'}).get('value')
    data['_xsrf'] = xsrf

def get_captcha():
    """

    """
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r=%s&type=login' % t
    req = s.get(captcha_url, headers=headers)
    with open('captcha.jpg',"wb") as f:
        f.write(req.content)
        f.close()
    image = Image.open('captcha.jpg')
    image.show()
    captcha = raw_input("Input:")
    data['captcha'] = captcha

def login():
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req = s.get(url, headers=headers)
        with open('zhihu.html','w') as f:
            f.write(req.content)
            f.close()
            print "login successful"
    else:
        email = raw_input("email: ")
        password = raw_input("password: ")
        data['email'] = email
        data['password'] = password
        get_xsrf()
        get_captcha()
        loginREQ = s.post(loginURL, headers=headers, data=data)
        print loginREQ.json()
        if not loginREQ.json()[u'r']:
            print s.cookies.get_dict()
            with open('cookiefile',"wb") as f:
                json.dump(s.cookies.get_dict(),f)
            print "Login Successful"
        else:
            print "login fail"






