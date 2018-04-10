#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
import time, re, sys
import json
import pystache
import logging

# À éventuellement modifier
filename = '/usr/syno/share/nginx/Portal.mustache'
tosearch = "\n        proxy_http_version      1.1;"
toreplace = "\n        proxy_http_version      1.1;\n        proxy_set_header      Upgrade    $http_upgrade;\n        proxy_set_header      Connection    \"upgrade\";\n        proxy_read_timeout      86400;"
# date et heure
asctime = time.asctime( time.localtime() )
##################################
try:

    with open(filename, 'r') as file :
        filedata = file.read()
    filedata = filedata.replace(tosearch,toreplace)
    with open(filename, 'w') as file:
        file.write(filedata)
finally:
    sys.exit()
