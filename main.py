# main.py
import sys
import requests
import threading
import time
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QLineEdit, QPushButton

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.running = False  # 데이터를 가져오는 스레드 상태

    def initUI(self):
        self.setWindowTitle("xDrip+ Blood Sugar Viewer")
        self.setGeometry(100, 100, 400, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Enter xDrip+ IP Address:")
        layout.addWidget(self.label)

        self.ip_input = QLineEdit()
        layout.addWidget(self.ip_input)

        self.submit_button = QPushButton("Start Monitoring")
        self.submit_button.clicked.connect(self.start_monitoring)
        layout.addWidget(self.submit_button)

        self.data_label = QLabel("Blood Sugar: N/A")
        layout.addWidget(self.data_label)

        self.setLayout(layout)

    def start_monitoring(self):
        ip_address = self.ip_input.text().strip()
        if not ip_address:
            self.label.setText("Please enter a valid IP address")
            return

        self.label.setText(f"Monitoring xDrip+ at {ip_address}")
        self.running = True
        thread = threading.Thread(target=self.fetch_data, args=(ip_address,), daemon=True)
        thread.start()

    def fetch_data(self, ip):
        url = f"http://{ip}:17580/rest/v1/latestbloodsugar"
        while self.running:
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    blood_sugar = data.get("sgv", "N/A")  # xDrip+의 혈당값 가져오기
                    self.data_label.setText(f"Blood Sugar: {blood_sugar} mg/dL")
                else:
                    self.data_label.setText("Error fetching data")
            except requests.exceptions.RequestException:
                self.data_label.setText("Connection Error")

            time.sleep(10)  # 10초마다 데이터 업데이트

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
