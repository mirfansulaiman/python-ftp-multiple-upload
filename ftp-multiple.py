#!/usr/bin/python
# FTP Multiple Upload.
# 16/06/2017
# author : @mirfansulaiman
# Modified from https://gist.github.com/slok/1447559
# Use :
# python ./ftp-multiple.py filename.xx
# python ./ftp-multiple.py foldername/filename.xx
# python ./ftp-multiple.py filename.xx foldername/filename.xx foldername/folder/filename.xx
# Upload all file in folder : python ./ftp-multiple.py *
###########################################

from ftplib import FTP
import hashlib, sys

USER = '********'
PASS = '********'
SERVER = 'website.xyz'
PORT = 21
BINARY_STORE = True 
###########################################

def connect_ftp():
    #Connect to the server
    ftp = FTP()
    ftp.connect(SERVER, PORT)
    ftp.login(USER, PASS)
    print (ftp.getwelcome())
    return ftp

def upload_file(ftp_connetion, upload_file_path):

    #Open the file
    try:
        upload_file = open(upload_file_path, 'r')
        #get the name
        path_split = upload_file_path.split('/')
        final_file_name = path_split[len(path_split)-1]
        print('md5sum : ' + hashlib.md5(final_file_name).hexdigest())
        #transfer the file
        print('Uploading ' + final_file_name + '...')
        
        if BINARY_STORE:
            ftp_connetion.storbinary('STOR '+ final_file_name, upload_file)
        else:
            ftp_connetion.storlines('STOR '+ final_file_name, upload_file)
            
        print('Upload finished.\n----------')
        
    except IOError:
        print("No such file or directory... passing to next file")
 
#Run Script
ftp_conn = connect_ftp()
for arg in sys.argv:
    if arg not in sys.argv[0]:
        print('Filename : ' + arg)
        upload_file(ftp_conn, arg)
