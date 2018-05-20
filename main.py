#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import chdir
from sys import version_info
#正規式re模組
import subprocess
import re
try:
    import env
except:
    print("請執行下方指令拷貝環境模組:\ncp env.py.example env.py\n並修改env.py中的環境設定")
    quit()
#郵件套件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
#日期
from datetime import date, timedelta

#取得昨天的日期
today = date.today()
yesterday = date.today() - timedelta(1)

#切換到工作目錄
path = env.path
try:
    chdir(path)
except FileNotFoundError as notfound:
    error="請確認env.py中路徑指定正確:\n{}".format(path)
    print(error)
    quit()

#=================================================================================================

#執行的報表的git指令
command = [ "pwd" ]
#透過Python執行命令
proc = subprocess.Popen(command ,shell=False, stdout=subprocess.PIPE)
#取得標準輸出，存入變數中。
output = proc.stdout.read()

subject = u"主題{}".format(today)

output = "郵件內容，工作目錄是在{}".format(output)

#=================================================================================================

#========環境設定============
#寄件者
me = env.me
#收件者需使用串列。
you = env.you
#郵件主機設定
mail_host = env.mail_host
mail_port = env.mail_port
mail_username = env.mail_username
mail_password = env.mail_password
#=======環境設定結束==========

#連接到郵件主機
try:
    smtpserver = smtplib.SMTP(mail_host, mail_port)
except:
    error="錯誤:無法正確連到郵件主機\nSMTP主機:{}，使用POST:{}".format(mail_host, mail_port)
    print(error)
    quit()
#啟動TLS加密
smtpserver.starttls()

#登入SMTP伺服器
try:
 smtpserver.login( mail_username, mail_password)
except:
    print("{}無法登入郵件主機".format(mail_username))
    quit()


#HTML訊息
# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('multipart')
msg['Subject'] = "{}".format(Header(subject,'utf-8'))
msg['From'] = me

#msg的收件者，使用逗號隔開即可。
if(len(you)==1):
  msg['To'] = you[0]
else:
  msg['To'] = ", ".join(you)


html = MIMEText(output, 'html','utf-8')
msg.attach(html)
#傳送Email
smtpserver.sendmail(me, you, msg.as_string())
#切斷SMTP伺服器連線
smtpserver.close()
print('寄出!')
