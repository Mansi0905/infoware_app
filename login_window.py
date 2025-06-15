from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import create_connection
from main_window import MainWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operator Login")
        self.init_ui()

    def init_ui(self):
        self.username_input = QLineEdit()
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Username"))
        layout.addWidget(self.username_input)
        layout.addWidget(QLabel("Password"))
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)
        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"Trying to login with username: {username} and password: {password}")


        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM operator WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        print(f"Query result: {result}")

        conn.close()

        if result:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

if __name__ == "__main__":
    app = QApplication([])
    login = LoginWindow()
    login.show()
    app.exec()

