#!/usr/bin/python
import imaplib
import pygame
import time
import os.path

imap_server   = "your_server"
imap_port     = "993"
imap_username = "username"
imap_pw       = "pw"
soundfile     = "91924__benboncan__till-with-bell.wav"

def new_mail_generator(last_uid, host, port, login, password):
    # connect
    mail_server = imaplib.IMAP4_SSL(host, port)
 
    # authenticate
    try:
        (retcode, capabilities) = mail_server.login(login, password)
    except:
        print sys.exc_info()[1]
        sys.exit(1)
    
    #select the inbox
    mail_server.select("INBOX")

    #get all the email uids
    result, data = mail_server.uid('search', None, "ALL")
    
    #write max uid to a file (persistent storage)
    uid_file = open("email_uid", "w")
    uid_file.write(max(data[0].split()))
    uid_file.close()
    
    for message_uid in data[0].split():
        if int(message_uid) > last_uid:
             yield data[0][1]
    
def main():
    
    uid = int(1)

    if os.path.isfile("email_uid"):
        f = open("email_uid")
        uid = int(f.readline())
        f.close()
    
    for mail in new_mail_generator(uid,
				host=imap_server,
				port=imap_port,
				login=imap_username,
				password=imap_pw):
        pygame.mixer.init()
        pygame.mixer.music.load(soundfile)
        pygame.mixer.music.play()
        time.sleep(2.5)

if __name__ == "__main__":
    main()

