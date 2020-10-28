
import sys
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import datetime

# 不具合一覧
# INOPERATION 点火
# WORN OUT
# SUPPLY
# DISCHARGER 放電
# LIGHTNING 落雷
# BIRD バードストライク
# RECLINING 取り替え

TROUBLE = ["INOPERATION","WORN","SUPPLY","DISCHARGER","LIGHTNING","BIRD","RECLINING"]
MACHINE_NUMBER = ["01RK","02RK","03RK","04RK","05RK","06RK"]

file = pd.read_csv('data.csv')
file = file.dropna(how = "all",axis=1)
file = file.dropna(how = "all")
# print("不具合情報:")
# value = input()
# value = value.upper()
d = datetime.datetime.today()
date = d.strftime("%Y-%m-%d")


def trouble_search (file, number):
    for key in TROUBLE:
        inpe = file[file['不具合情報'].str.match('^.*' + key + '.*$')]
        inpe_count = len(inpe)
        inpe.to_csv('to_csv_out_' + number + '_' + key + '.csv')
        if (inpe_count >= 3):
            print(number + "の" + key + "の不具合は3回以上です。")

    return inpe_count

for key in MACHINE_NUMBER:
    inpe = file[file['機番'].str.match('^.*' + key + '.*$')]
    # inpe.to_csv('to_csv_out_' + key + '_' + date + '.csv')
    inpe_count =  trouble_search(inpe,key)
    if (inpe_count > 3):
        inpe.to_csv('to_csv_out_' + key + '_' + '.csv')




# def send_mail():
#     try:
#         print("メールアドレス:")
#         toaddr = input()
#         raw_msg = "「" + value + "」の不具合は" + inpe_count + "件です。"
#         msg = MIMEText(raw_msg.encode(jp), 'plain', jp, )
#         fromaddr = ""
#         password = ""
#
#         msg['Subject'] = "不具合情報" + date
#         msg['From'] = fromaddr
#         msg['To'] = toaddr
#
#         smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
#         smtpobj.ehlo()
#         smtpobj.starttls()
#         smtpobj.ehlo()
#         smtpobj.login(fromaddr, password)
#         smtpobj.sendmail(fromaddr, toaddr, msg)
#         smtpobj.close()
#         return True
#     except:
#         return False

# print(inpe,"\n",inpe_count,"\n",value)
#
# if (inpe_count >= 3):
#     inpe.to_csv('to_csv_out'+date+'.csv')
#     print("3回以上です")
    # try:
    #     if (send_mail()):
    #         print("Successfully sent email")
    # except Exception:
    #     print("Error: unable to send email")


# file['不具合情報'].str.match('^.*INOPERATION.*$')

# file[file['8'].isna() == False]

# inpe = file[file['不具合情報'].str.match('^.*INOPERATION.*$')]
# print(inpe)

