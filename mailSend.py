from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

def send(contents,sendTo='resever04@gmail.com'):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login('locon4765', 'dorca6-gyqpoJ-medweb')

    msg = MIMEText(contents)
    msg['Subject'] = 'subject'
    msg['From'] = 'locon4765@gmail.com'
    msg['To'] = sendTo
    msg['Date'] = formatdate()

    smtpobj.sendmail('locon4765@gmail.com', sendTo, msg.as_string())
    smtpobj.close()