from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib


#input()は実行が面倒だからつけてない
#gmailのログイン保持はムリっぽい
#send(送る内容)で'resever04@gmail.com'に送信
# https://mail.google.com/mail/u/2/#inbox/FMfcgxwKjBSPFLlfJhbrDsfGJbjxvjvb で送った内容が見える　passwordは　xixqiZ-9faqne-kamsav
#例外処理まで書く気しない、動くから良いでしょう

def send(contents,sendTo='resever04@gmail.com',password='dorca6-gyqpoJ-medweb'):
    try:
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.login('locon4765', password)
        password = ''

        msg = MIMEText(contents)
        msg['Subject'] = '直近の不具合情報について'
        msg['From'] = 'locon4765@gmail.com'
        msg['To'] = sendTo
        msg['Date'] = formatdate()

        smtpobj.sendmail('locon4765@gmail.com', sendTo, msg.as_string())
        smtpobj.close()
        return True
    except:
        return False


    