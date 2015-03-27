__author__ = 'defremov'

from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('db_connect.conf')

source_creds = config.get('Source Database', 'source_user') + '/' + config.get('Source Database', 'source_pass') \
               + '@' + config.get('Source Database', 'source_host') + '/' + config.get('Source Database', 'source_sid')
print source_creds

dest_creds = config.get('Destination Database', 'dest_user') + '/' + config.get('Destination Database', 'dest_pass') \
               + '@' + config.get('Destination Database', 'dest_host') + '/' + config.get('Destination Database', 'dest_sid')
print dest_creds


#f = open('db_connect.conf','r')
