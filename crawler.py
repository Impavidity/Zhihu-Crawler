from bs4 import BeautifulSoup
import time
import Image
from pytesser import pytesser
import os
import json
from globalVal import *
from login import *
from get_answer import *


if __name__=="__main__":
    login()
    while True:
    	#qID = raw_input("Question ID: ")
    	get_answer("37167038")
    	break