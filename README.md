# mail_shell

一個用Python寫的簡單發信程式。

方便自己改寫subject及output。

放於排程中執行


#### 一、拷貝出設定檔模組
<pre>
cp env.py.example env.py
</pre>

#### 二、依自己的環境，修改env.py
<pre>
# -*- coding: utf-8 -*-
#寄件者
me = "me@exampl.test"

#收件者需使用串列。
you = ['user1@exampl.test','user2@exampl.test']

#用來定義切換的工作目錄
path = "/dlaravel/sites/ccc"

#郵件主機發送設定
mail_host = "mail.example.test"
mail_port = 25
mail_username = "admin"
mail_password = "admin"
</pre>

#### 四、嚐試執行。
<pre>./main.py</pre>
或
<pre>python main.py</pre>
或python3
<pre>pyton3 main.py</pre>
發送的內容顯示於營幕上，不真的送出
<pre> ./main.py dry-run</pre>

#### 五、變更main.py的內容
改寫main.py中的
subject 及 output

#### 六、設定排程，加入crontab每日00:10分執行，例如:
<pre>
10 0 * * * /usr/local/scripts/git-yesterday-report/main.py
</pre>
