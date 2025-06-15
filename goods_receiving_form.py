from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import create_connection

class GoodsReceivingForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Goods Receiving Form")
        self.init_ui()

    def init_ui(self):
        self.product_id_input = QLineEdit()
        self.supplier_input = QLineEdit()
        self.quantity_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.rate_per_unit_input = QLineEdit()
        self.tax_input = QLineEdit()

        save_button = QPushButton("Save Entry")
        save_button.clicked.connect(self.save_data)

        layout = QVBoxLayout()
        for label, widget in [
            ("Product ID", self.product_id_input),
            ("Supplier", self.supplier_input),
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
            supplier = self.supplier_input.text()
            quantity = int(self.quantity_input.text())
            unit = self.unit_input.text()
            rate_per_unit = float(self.rate_per_unit_input.text())
            tax = float(self.tax_input.text())
            total = quantity * rate_per_unit + tax

            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO goods_receiving 
                (product_id, supplier, quantity, unit, rate_per_unit, total, tax) 
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                (product_id, supplier, quantity, unit, rate_per_unit, total, tax))
            conn.commit()
            conn.close()

            QMessageBox.information(self, "Success", "Goods receiving entry saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
