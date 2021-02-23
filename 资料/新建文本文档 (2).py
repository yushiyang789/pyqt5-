from PyQt5.Qt import *
import sys



        
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥,人狠话不多")
window.resize(500, 500)
window.move(400, 200)

push_btn=QPushButton(window)
push_btn.setText('这是QPushBuon')
push_btn.move(100,100)

menu=QMenu()




new_action=QAction(QIcon('1.jpg'),'新建',menu)
new_action.triggered.connect(lambda :print('新建'))

open_action=QAction('打开',menu)
open_action.triggered.connect(lambda :print('打开'))

exit_action=QAction('退出',menu)
exit_action.triggered.connect(lambda :print('退出'))

child_menu=QMenu(menu)
child_menu.setTitle('最近打开')
file_action=QAction('打开你大爷')
child_menu.addAction(file_action)

menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(child_menu)
menu.addSeparator()
menu.addAction(exit_action)


push_btn.setMenu(menu)

window.show()

sys.exit(app.exec_())
