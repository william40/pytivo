#!/usr/bin/env python


import beacon, httpserver, os, sys

from Config import config

port = config.get('Server', 'Port')

httpd = httpserver.TivoHTTPServer(('', int(port)), httpserver.TivoHTTPHandler)

for section in config.sections():
    if not section == 'Server':
        httpd.add_container(section, config.get(section, 'type'), config.get(section, 'path'))

b = beacon.Beacon()
b.add_service('TiVoMediaServer:' + str(port) + '/http')
b.start()

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    b.stop()
