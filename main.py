# main.py
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton

def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("My Python App")
    window.setGeometry(100, 100, 300, 200)
    
    layout = QVBoxLayout()
    
    label = QLabel("Enter IP Address:")
    layout.addWidget(label)
    
    ip_input = QLineEdit()
    layout.addWidget(ip_input)
    
    def show_ip():
        ip_address = ip_input.text()
        label.setText(f"IP: {ip_address}")
    
    button = QPushButton("Submit")
    button.clicked.connect(show_ip)
    layout.addWidget(button)
    
    window.setLayout(layout)
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
