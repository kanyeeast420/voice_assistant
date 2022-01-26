from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


def window():
    # window
    app = QApplication(sys.argv)
    win = QMainWindow()

    # win props
    win.setGeometry(0, 0, 300, 150)
    win.setWindowTitle("voice assistant")

    button = QPushButton(win)
    button.setText("Run assistant")
  

    # create window
    win.show()
    sys.exit(app.exec_())


window()
