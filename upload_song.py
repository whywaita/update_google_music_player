#!/usr/bin/env python
# coding: utf-8 
import gmusicapi
from gmusicapi.appdirs import my_appdirs
import os.path
import sys

OAUTH_FILEPATH = os.path.join(my_appdirs.user_data_dir, 'oauth.cred')
api = gmusicapi.Musicmanager()

argvs = []
argvs = sys.argv[1:]

overlap_song = []
updated_song = []
filtering_song = []

# check oauth credential
if not os.path.isfile(OAUTH_FILEPATH):
    api.perform_oauth()

# login gmp
try:
    api.login(OAUTH_FILEPATH)
    print "login Success!"
except:
    print "login fail..."

print argvs

# upload argvs file
for i in range(len(argvs)):
    try:
        print "upload start " + argvs[i]
        api.upload(argvs[i])
        print "upload done!"
    except:
        print "Error!", sys.exc_info()[0]
