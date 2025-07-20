import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLineEdit # Import QLineEdit
from ui.caesar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Nút Encrypt
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        # Nút Decrypt
        self.ui.pushButton_2.clicked.connect(self.call_api_decrypt)

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/encrypt"
        payload = {
            # Sử dụng self.ui.lineEdit để lấy Plain Text (QLineEdit dùng .text())
            "plain_text": self.ui.lineEdit.text(),
            # Sử dụng self.ui.lineEdit_2 để lấy Key (QLineEdit dùng .text())
            "key": self.ui.lineEdit_2.text()
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                # Hiển thị kết quả mã hóa vào self.ui.lineEdit_3 (Cipher Text) (QLineEdit dùng .setText())
                self.ui.lineEdit_3.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API (Encrypt)")
                QMessageBox.critical(self, "Lỗi Mã Hóa", f"Có lỗi khi gọi API: {response.status_code}\n{response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Không thể kết nối đến API: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/caesar/decrypt"
        payload = {
            # Lấy Cipher Text từ self.ui.lineEdit_3 (QLineEdit dùng .text())
            "cipher_text": self.ui.lineEdit_3.text(),
            # Lấy Key từ self.ui.lineEdit_2 (QLineEdit dùng .text())
            "key": self.ui.lineEdit_2.text()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Hiển thị kết quả giải mã vào self.ui.lineEdit (Plain Text) (QLineEdit dùng .setText())
                self.ui.lineEdit.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API (Decrypt)")
                QMessageBox.critical(self, "Lỗi Giải Mã", f"Có lỗi khi gọi API: {response.status_code}\n{response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            QMessageBox.critical(self, "Lỗi Kết Nối", f"Không thể kết nối đến API: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())