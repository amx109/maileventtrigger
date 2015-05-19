a simple python script that:

* gets list of emails from inbox IMAP folder (via TLS)
* plays sound for each email greater than last mail UID
* stores highest email UID

**On first run** it will play a sound for every mail in the inbox since initial mail UID is set to 1

**Bypass email count** by writing a higher email id to the email_uid file

the sound file was obtained from http://www.freesound.org/people/Benboncan/sounds/91924/
