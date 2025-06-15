from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
from database import create_connection

class ProductMasterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Master List")
        self.init_ui()

    def init_ui(self):
        self.barcode_input = QLineEdit()
        self.sku_id_input = QLineEdit()
        self.category_input = QLineEdit()
        self.subcategory_input = QLineEdit()
        self.product_name_input = QLineEdit()
        self.description_input = QTextEdit()
        self.tax_input = QLineEdit()
        self.price_input = QLineEdit()
        self.unit_input = QLineEdit()
        self.image_path_input = QLineEdit()

        browse_button = QPushButton("Browse Image")
        browse_button.clicked.connect(self.browse_image)
        save_button = QPushButton("Save Product")
        save_button.clicked.connect(self.save_product)

        layout = QVBoxLayout()
        for label, widget in [
            ("Barcode", self.barcode_input),
            ("SKU ID", self.sku_id_input),
            ("Category", self.category_input),
            ("Subcategory", self.subcategory_input),
            ("Product Name", self.product_name_input),
            ("Description", self.description_input),
            ("Tax", self.tax_input),
            ("Price", self.price_input),
            ("Unit", self.unit_input),
            ("Image Path", self.image_path_input)
        ]:
            layout.addWidget(QLabel(label))
            layout.addWidget(widget)
        layout.addWidget(browse_button)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def browse_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg)")
        if path:
            self.image_path_input.setText(path)

    def save_product(self):
        try:
            data = (
                self.barcode_input.text(),
                self.sku_id_input.text(),
                self.category_input.text(),
                self.subcategory_input.text(),
                self.image_path_input.text(),
                self.product_name_input.text(),
                self.description_input.toPlainText(),
                float(self.tax_input.text()),
                float(self.price_input.text()),
                self.unit_input.text()
            )
            conn = create_connection()
            conn.execute('''INSERT INTO product_master (barcode, sku_id, category, subcategory,
                image_path, name, description, tax, price, unit)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
            conn.commit()
            conn.close()
            QMessageBox.information(self, "Success", "Product saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
