from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import create_connection

class SalesForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sales Form")
        self.init_ui()

    def init_ui(self):
        self.product_id_input = QLineEdit()
        self.customer_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.rate_per_unit_input = QLineEdit()
        self.tax_input = QLineEdit()

        save_button = QPushButton("Save Sale")
        save_button.clicked.connect(self.save_data)

        layout = QVBoxLayout()
        for label, widget in [
            ("Product ID", self.product_id_input),
            ("Customer", self.customer_input),
            ("Quantity", self.quantity_input),
            ("Unit", self.unit_input),
            ("Rate per Unit", self.rate_per_unit_input),
            ("Tax", self.tax_input)
        ]:
            layout.addWidget(QLabel(label))
            layout.addWidget(widget)
        layout.addWidget(save_button)
        self.setLayout(layout)

    def save_data(self):
        try:
            product_id = int(self.product_id_input.text())
            customer = self.customer_input.text()
            quantity = int(self.quantity_input.text())
            unit = self.unit_input.text()
            rate_per_unit = float(self.rate_per_unit_input.text())
            tax = float(self.tax_input.text())
            total = quantity * rate_per_unit + tax

            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO sales 
                (product_id, customer, quantity, unit, rate_per_unit, total, tax) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (product_id, customer, quantity, unit, rate_per_unit, total, tax))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Sale entry saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
