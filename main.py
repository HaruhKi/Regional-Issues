import sys
import pandas as pd
import smtplib
import datetime
import http.server
import socketserver
import sendMail 
import re
from email.mime.text import MIMEText
from collections import Counter

# 機体番号一覧
MACHINE_NUMBER = ["01RK","02RK","03RK","04RK","05RK","06RK"]
# REMOVE_WORDは検索から外したい単語一覧です。右に単語を追加していくことが出来ます。
REMOVE_WORD = ["-","OUT","OUT.","ON","IN","AT","OF","NG","RH","LH","MAIN","FOUND"]

# ここにExcelファイルからexportしたcsvファイルの名前を記載します。
# csvファイルはこのファイル（main.py）と同じ場所に置きます。
file = pd.read_csv('data.csv')

file = file.dropna(how = "all",axis=1)
file = file.dropna(how = "all")

inpe = file['不具合情報']
inpe_count = len(inpe)

all_list = []
for i in range(inpe_count):
    ilist = inpe[i].split()
    alist  = [ilist[i] for i in range(len(ilist))]
    all_list += alist
c = Counter(all_list)


re_comp = re.compile("^NO.[0-9].*$")
count_over = [i[0] for i in c.items() if i[1] >= 3]
remove_no  = [count_over[i] for i in range(len(count_over)) if not re_comp.match(count_over[i])]
TROUBLE = [remove_no[i] for i in range(len(remove_no)) if remove_no[i] not in REMOVE_WORD]

# 下二行のコメントを外すと検索がかかっている不具合一覧が見れます。
# 検索に単語を追加したい場合は「TROUBLE.append("ここに検索したい単語を入れる")」のコメントアウトを削除してください。

# print("↓不具合一覧↓\n")
# print(TROUBLE)

# TROUBLE.append("ここに検索したい単語を入れる")


def trouble_search (file, number):
    trouble_data = ''
    for key in TROUBLE:
        inpe = file[file['不具合情報'].str.match('^.*' + key + '.*$')]
        inpe_count = len(inpe)
        if (inpe_count >= 3):
            inpe.to_csv('to_csv_out_' + number + '_' + key + '.csv')
            trouble_data = trouble_data + key + "の不具合は" + str(inpe_count) + "回です。\n"
    print("【機体番号　" + number + "　】\n")
    print(trouble_data)
    return inpe_count,trouble_data


mailContent = ''
for key in MACHINE_NUMBER:
    inpe = file[file['機番'].str.match('^.*' + key + '.*$')]
    inpe_count,trouble_data =  trouble_search(inpe,key)
    mailContent = mailContent + "【機体番号　" + key + "　】\n" + trouble_data + "\n"
    
sendMail.send(mailContent)


