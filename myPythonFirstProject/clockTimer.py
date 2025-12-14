#name = Suminda lakshan

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase,QPainter, QBrush, QColor, QPen


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setFixedSize(400, 400)


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.setWindowFlags(Qt.FramelessWindowHint) # i used this for remove window borders
        self.setAttribute(Qt.WA_TranslucentBackground) # from this i could be able to make background transparent

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("""
                   font-size: 60px; 
                   color: hsl(111, 100%, 50%);
                   background: transparent;
               """)

        font_id = QFontDatabase.addApplicationFont("I:/myPythonFirstProject/DS-DIGIB.TTF")
        if font_id != -1:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family,42)
            self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setBrush(QBrush(QColor(0, 0, 0, 150)))   #we can change transparency as we want
        painter.setPen(QPen(QColor(111, 255, 0, 180), 3))  # Green border
        painter.drawEllipse(2, 2, self.width() - 4, self.height() - 4)

        painter.setPen(QPen(QColor(111, 255, 0, 80), 1))
        painter.drawEllipse(10, 10, self.width() - 20, self.height() - 20)

    def update_time(self):
            current_time = QTime.currentTime().toString("hh:mm:ss AP")
            self.time_label.setText(current_time)

    def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                self.drag_position = event.globalPos() - self.frameGeometry().topLeft()# using this drag position i could dragg the window
                event.accept()
#below mentioned  (mousePressEvent, mouseMoveEvent, mouseReleaseEvent) make window draggable
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drag_position:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.drag_position = None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())