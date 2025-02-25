# main.py
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("My Python App")
    window.setGeometry(100, 100, 300, 200)
    label = QLabel("Hello, World!", window)
    label.move(100, 80)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
