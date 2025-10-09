import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QVBoxLayout,QHBoxLayout, QPushButton
from PyQt5.QtCore import QTimer,QTime,Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0,0)
        self.time_label = QLabel("00:00:00:00",self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop-Watch")
        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)
        vbox.addWidget(self.reset_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.start_button)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()

        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.start_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
        
        QPushButton{
        font-size: 20px;
        
        }
        QLabel{
        font-size: 50px;
        
        }
        """)
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)



    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.time = QTime(0,0,0,0)
        self.time_label.setText(self.format_time(self.time))



    def format_time(self, time):
        hour = time.hour()
        minute = time.minute()
        seconds = time.second()
        millisec = time.msec()//10

        return f"{hour:02}:{minute:02}:{seconds:02}:{millisec:02}"


    def update_display(self):

        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))





if __name__ == "__main__":
    app = QApplication(sys.argv)
    watch = StopWatch()
    watch.show()
    sys.exit(app.exec_())