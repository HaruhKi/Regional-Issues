from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib

def send(contents,sendTo='受信するメールアドレス',password='送信するメールアドレス（gmail）のパスワード'):
    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login('送信するメールアドレスのアカウント名（gmail）', password)
        password = ''

        msg = MIMEText(contents)
        msg['Subject'] = '直近の不具合情報について'
        msg['From'] = '送信するメールアドレス（gmail）'
        msg['To'] = sendTo
        msg['Date'] = formatdate()

        smtpobj.sendmail('送信するメールアドレス（gmail）', sendTo, msg.as_string())
        smtpobj.close()
        return True
    except:
        return False


    