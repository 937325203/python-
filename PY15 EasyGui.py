import easygui as ui
import os
import sys
#ui.msgbox("是,冰与火之歌")

ui.msgbox(title="白同学的问题",msg='来,坐好.问你个问题',ok_button='继续',image="/Users/BigBai/Downloads/sg.gif")

fildnames=['账号','密码']#输入框前的信息
fildvalues=['输入账号','输入密码']#输入框的默认内容

#mult:多元的
fildvalues=ui.multenterbox(msg="m",title="账号中心",fields=fildnames,values=fildvalues)
#fildvalues=ui.multpasswordbox(msg='欢迎',title='账号中心',fields=fildnames,values=fildvalues)
passwd=open('/Users/BigBai/Desktop/passwd','a')

for need in fildvalues:
    passwd.writelines(need+"\n")

passwd.close()

msg='眼镜好看吗?'
bt='关于眼镜的一个调查'
xz=['丑爆炸','人好看','贼帅','有点酷']

#先定义说话函数
def sh():
    """先输入想说的话"""
    neirong = ui.enterbox(msg='输入一句你想说的话', default='好饿...')
    """选择存储位置"""
    #path = ui.diropenbox(msg='选择存储位置:', title='这是title', default='/Users/BigBai/Desktop')
    #path = os.path.join(path, '想说的话')
    #path=ui.fileopenbox(msg='打开文件以存储',title='这是title',default='/Users/BigBai/Desktop/想说的话.txt',filetypes=['*.py','*.txt'])
    path=ui.filesavebox(msg='打开文件以存储',title='这是title',default='/Users/BigBai/Desktop/想说的话新.txt',filetypes=['*.py','*.txt'])
    xsdh = open(path, 'a')
    xsdh.write(neirong)
    xsdh.close()

while 1:
    cc=ui.choicebox(msg,bt,xz)
    if cc=='丑爆炸':
        ui.msgbox(msg="回去重新选择")
        continue

    if cc=='人好看':

        if ui.ccbox(msg='好看就好!',choices=('继续玩','不玩了')):
            continue
        else:
            ui.msgbox('拜拜')
            #sys.exit()
            break

    if  cc=='贼帅':

        """indexbox返回数值,buttonbox返回str"""
        huidan=ui.indexbox(msg='谢谢你哈~',choices=('不用谢~','我也很帅'))
        huida= ui.buttonbox(msg='谢谢你哈~',choices=('不用谢~','我也很帅'))
        if huidan==1:
            ui.msgbox('你真的不要脸了?',ok_button="是的!")
            break

    if cc=='有点酷':

        """返回一个list存储着选择的选项"""
        fanhui=ui.multchoicebox(msg='嘿嘿...谢谢你',choices=('骗你的','蠢狗'))
        sh()
        break



