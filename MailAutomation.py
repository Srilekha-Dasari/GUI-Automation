
"""The smtplib module defines an SMTP client session object that can be used to 
send mail to any Internet machine with an SMTP or ESMTP listener daemon. """
#pip install smtplib 
import smtplib
connectionobj= smtplib.SMTP("smtp.gmail.com",587) #port num for gmail domain
connectionobj.ehlo() #it is hello to servers which support SMTP services
connectionobj.starttls() #StartTLS is a protocol command used to (encrypt) inform the email server 
#that the email client wants to upgrade from an insecure connection to a secure one using TLS or SSL.
#connectionobj.login("From (your) gmail address", "password")
connectionobj.login("from@gmail.com","EnterPassword")
#connectiononj.sendmail("from address","to address","message")
connectionobj.sendmail("from@gmail.com","to@gmail.com", 
                       "Subject: Trial Mail \n\n  Hello are you enjoying automation? Now you removed error fantastic \n\n")

"""If any error occurs: Go to your (Google Account).
On the left navigation panel, click Security.
On the bottom of the page, in the Less secure app access panel, click Turn on access.
If you don't see this setting, 
your administrator might have turned off 
less secure app account access (check the instruction above).
Click the Save button."""