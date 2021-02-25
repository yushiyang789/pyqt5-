from PyQt5.Qt import *
import sys



        
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("社会我顺哥,人狠话不多")
window.resize(500, 500)
window.move(400, 200)

le_b=QLineEdit(window)
le_b.setEchoMode(3)


window.show()

sys.exit(app.exec_())
