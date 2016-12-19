#-*- coding: utf-8 -*-
import requests

global url
url = "http://www.zhihu.com"
global loginURL
loginURL = "https://www.zhihu.com/login/email"

global headers
headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0",
    "Referer" : "http://www.zhihu.com",
    "Host" : "www.zhihu.com"
}

global s
s = requests.session()
global xsft

global data
data = {
    "rememberme" : "true"
}