from email.message import EmailMessage
from EMAIL_SENDER import password #create a module  for the password 
"""go to your personal mail settings and left side of corner you could see a security option,click it and roll down 
two step verification  is there,if it is off enable and inside an had app ,create app name and it generate some own password and copies it

"""

import ssl
import smtplib
email_sender='sender mail id'
receive_r='receiver mail id'
subject="HELLO WORLD!"
body="""
IT IS WHAT IT IS!

"""
em=EmailMessage()
em['From']=email_sender
em['to']=receive_r
em['subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,password)
    smtp.sendmail(email_sender,receive_r,em.as_string())
