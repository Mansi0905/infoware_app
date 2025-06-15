from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from goods_receiving_form import GoodsReceivingForm
from product_master import ProductMasterForm
from sales_form import SalesForm

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Infoware Inventory Management")
        self.setGeometry(200, 200, 300, 200)
        layout = QVBoxLayout()

        goods_btn = QPushButton("Goods Receiving")
        goods_btn.clicked.connect(self.open_goods_form)

        sales_btn = QPushButton("Sales Form")
        sales_btn.clicked.connect(self.open_sales_form)

        product_btn = QPushButton("Product Master List")
        product_btn.clicked.connect(self.open_product_form)

        layout.addWidget(goods_btn)
        layout.addWidget(sales_btn)
        layout.addWidget(product_btn)
        self.setLayout(layout)

    def open_goods_form(self):
        self.gform = GoodsReceivingForm()
        self.gform.show()

    def open_sales_form(self):
        self.sform = SalesForm()
        self.sform.show()

    def open_product_form(self):
        self.pform = ProductMasterForm()
        self.pform.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
