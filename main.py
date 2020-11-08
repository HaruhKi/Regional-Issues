
import sys
import pandas as pd
import smtplib
from email.mime.text import MIMEText
import datetime
import http.server
import socketserver
import sendMail 




# 不具合一覧
# INOPERATION 点火
# WORN OUT
# SUPPLY
# DISCHARGER 放電
# LIGHTNING 落雷
# BIRD バードストライク
# RECLINING 取り替え

TROUBLE = ["INOPERATION","WORN","SUPPLY","DISCHARGER","LIGHTNING","BIRD","RECLINING","STATIC"]
# TROUBLE = input()
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
    trouble_data = ''
    for key in TROUBLE:
        inpe = file[file['不具合情報'].str.match('^.*' + key + '.*$')]
        inpe_count = len(inpe)
        if (inpe_count >= 3):
            inpe.to_csv('to_csv_out_' + number + '_' + key + '.csv')
            trouble_data = trouble_data + number + "の" + key + "の不具合は3回以上です。" + '\n'
    print(trouble_data)
    return inpe_count,trouble_data
    #return に trouble_data　を追加しました

mailContent = ''
for key in MACHINE_NUMBER:
    inpe = file[file['機番'].str.match('^.*' + key + '.*$')]
    # inpe.to_csv('to_csv_out_' + key + '_' + date + '.csv')
    inpe_count,trouble_data =  trouble_search(inpe,key)
    mailContent = mailContent + trouble_data
    
sendMail.send(mailContent)

# PORT = 8000
# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()

