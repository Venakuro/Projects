import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QGridLayout,QVBoxLayout,QLineEdit,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("hehe.png"))
        self.display = QLineEdit(self)
        self.one = QPushButton("1",self)
        self.two = QPushButton("2",self)
        self.three = QPushButton("3",self)
        self.four = QPushButton("4",self)
        self.five = QPushButton("5",self)
        self.six = QPushButton("6",self)
        self.seven = QPushButton("7",self)
        self.eight = QPushButton("8",self)
        self.nine = QPushButton("9",self)
        self.zero = QPushButton("0",self)
        self.add = QPushButton("+",self)
        self.sub = QPushButton("-",self)
        self.mul = QPushButton("x",self)
        self.div = QPushButton("/",self)
        self.eq = QPushButton("=",self)
        self.decimal = QPushButton(".",self)
        self.clear = QPushButton("C",self)
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.seven,0,0)
        grid.addWidget(self.eight,0,1)
        grid.addWidget(self.nine,0,2)
        grid.addWidget(self.add,0,3)
        grid.addWidget(self.four,1,0)
        grid.addWidget(self.five,1,1)
        grid.addWidget(self.six,1,2)
        grid.addWidget(self.sub,1,3)
        grid.addWidget(self.one,2,0)
        grid.addWidget(self.two,2,1)
        grid.addWidget(self.three,2,2)
        grid.addWidget(self.mul,2,3)
        grid.addWidget(self.zero,3,0)
        grid.addWidget(self.decimal,3,1)
        grid.addWidget(self.div,3,2)
        grid.addWidget(self.eq,3,3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.display)
        vbox.addWidget(self.clear)
        vbox.addLayout(grid)

        self.display.setFixedHeight(50)
        self.display.setReadOnly(True)

        self.setLayout(vbox)
        self.one.clicked.connect(self.onee)
        self.two.clicked.connect(self.twoo)
        self.three.clicked.connect(self.threee)
        self.four.clicked.connect(self.fourr)
        self.five.clicked.connect(self.fivee)
        self.six.clicked.connect(self.sixx)
        self.seven.clicked.connect(self.sevenn)
        self.eight.clicked.connect(self.eightt)
        self.nine.clicked.connect(self.ninee)
        self.zero.clicked.connect(self.zeroo)
        self.add.clicked.connect(self.pluss)
        self.sub.clicked.connect(self.minus)
        self.mul.clicked.connect(self.mull)
        self.div.clicked.connect(self.divv)
        self.eq.clicked.connect(self.equal)
        self.decimal.clicked.connect(self.decimall)
        self.clear.clicked.connect(self.dell)

        self.setStyleSheet("""
        QPushButton {
        font-size: 30px;
        }
        QLineEdit {
        font-size: 30px;
        }
        """)


    def onee(self):
        self.display.setText(self.display.text()+"1")
    def twoo(self):
        self.display.setText(self.display.text()+"2")
    def threee(self):
        self.display.setText(self.display.text()+"3")
    def fourr(self):
        self.display.setText(self.display.text()+"4")
    def fivee(self):
        self.display.setText(self.display.text()+"5")
    def sixx(self):
        self.display.setText(self.display.text()+"6")
    def sevenn(self):
        self.display.setText(self.display.text()+"7")
    def eightt(self):
        self.display.setText(self.display.text()+"8")
    def ninee(self):
        self.display.setText(self.display.text()+"9")
    def zeroo(self):
        self.display.setText(self.display.text()+"0")
    def pluss(self):
        self.display.setText(self.display.text()+"+")
    def mull(self):
        self.display.setText(self.display.text()+"*")
    def divv(self):
        self.display.setText(self.display.text()+"/")
    def minus(self):
        self.display.setText(self.display.text()+"-")
    def decimall(self):
        self.display.setText(self.display.text()+".")
    def dell(self):
        self.display.setText("")
    def equal(self):
        try:
            result = eval(self.display.text())
            self.display.setText(str(result))
        except ZeroDivisionError:
            self.display.setText("MATHS ERROR")






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())