import itchat
import time
import sys

itchat.auto_login(enableCmdQR=2,hotReload=True)

msg_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()));
msg_content = sys.argv[1]
msg = msg_time + ' [itchat]:\n' + msg_content
#itchat.send(msg)
author = itchat.search_friends(name='haozi')[0]
author.send(msg)
