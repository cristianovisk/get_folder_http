#!/usr/bin/env python
import requests, sys
from subprocess import PIPE, Popen
folder=""
plus=('\x1b[6;30;42m' + '[+]' + '\x1b[0m')
#HELP------------------------------------------------
if (sys.argv[1] == "--help"):
    print ("Sintax: get_http.py http://exemplo.com/ wordlist.txt")
    exit()
elif (sys.argv[1] == ""):
   print ("Sintax: get_http.py http://exemplo.com/ wordlist.txt")
   exit()
#CMD SYSTEM------------------------------------------
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

#GET_HTTP--------------------------------------------
def get_http(url):
    resp = requests.head("%s" %(url))
#   print resp.status_code, resp.text, resp.headers
    return resp.status_code

#-----------------------------------------------------
def read_file(file):
    folders=cmdline("cat %s" %file)
    folders=folders.split("\n")[::]
#   print folders
    return folders

def check_folder():
    site = sys.argv[1]
    folder = sys.argv[2]
    folders=read_file(folder)
    for fold in range(0, len(folders)):
        code = get_http("%s%s" %(site, folders[fold]))
        if (folders[fold] == ""):
            print "[-]"
        elif (code != 404):
            print ("%s Pasta: %s%s foi encontrada..." %(plus, site, folders[fold]))
site=sys.argv[1]
print ("%s Checando site %s" %(plus,site))
print ("%s Carregando wordlist..." %plus)
check_folder()
print('\x1b[6;30;42m' + 'Wordlist finalizada!' + '\x1b[0m')
