from PyQt5.Qt import *
import sys



        
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("QQ登录")
window.resize(500, 500)
window.move(400, 200)

lb=QLabel("帐号",window)
lb.move(180,80)
lb2=QLabel("密码",window)
lb2.move(180,110)
lb3=QLabel(window)
lb3.resize(70,20)
lb3.move(400,80)
lb4=QLabel(window)
lb4.resize(70,20)
lb4.move(400,110)

le1=QLineEdit(window)
le1.move(210,80)
le2=QLineEdit(window)
le2.move(210,110)


completer=QCompleter(['123','1234','123456'],le1)
le1.setCompleter(completer)




le2.setEchoMode(2)

def change():
    if le2.echoMode()==2:
        le2.setEchoMode(0)
        action.setIcon(QIcon('2.png'))
    else:
        le2.setEchoMode(2)
        action.setIcon(QIcon('1.png'))

action=QAction(le2)
action.setIcon(QIcon('1.png'))
le2.addAction(action,1)
action.triggered.connect(change)

pt=QPushButton("登录",window)
pt.move(220,140)



def cao():
    account=le1.text()
    password=le2.text()
    if account != 'sz':
        le1.setText('')
        le2.setText('')
        lb3.setText('帐号不存在')
        le1.setFocus()
    elif password != 'itlike':
        le2.setText('')
        lb4.setText('密码错误')
        le2.setFocus()
    else:
        print('登陆成功')
    
pt.pressed.connect(cao)

window.show()

sys.exit(app.exec_())
