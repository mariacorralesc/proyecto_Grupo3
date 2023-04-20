from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from listaproductos import Ui_FrmProductos
import sqlite3
import sys


class FrmProductos(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FrmProductos()
        self.ui.setupUi(self)
        self.ui.btGuardar.clicked.connect(self.guardar_click)
        self.ui.btActualizar.clicked.connect(self.actualizar_click)
        self.iniciar_basede_datos()

    # Iniciamos la base de datos y creamos la tabla si no existe
    def iniciar_basede_datos(self):
        self.conn = sqlite3.connect("dbproductos.bd")
        cursor = self.conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
            codigo TEXT NOT NULL,
            producto TEXT NOT NULL,
            cantidad TEXT NOT NULL,
            precio TEXT NOT NULL)""")
        self.conn.commit()

    def guardar_click(self):
        conn = sqlite3.connect("dbproductos.bd")
        cursor = conn.cursor()
        self.codigo = str(self.ui.txtCodigo.text())
        self.producto = str(self.ui.txtProducto.text())
        self.cantidad = str(self.ui.txtCantidad.text())
        self.precio = str(self.ui.txtPrecio.text())

        self.registro = (self.codigo, self.producto, self.cantidad, self.precio)

        cursor.execute("INSERT INTO productos (codigo,producto,cantidad,precio) VALUES (?,?,?,?)", self.registro)

        conn.commit()
        self.ui.lineEdit.setText("")
        conn.commit()
        QMessageBox.about(self, "Registro guardado", "Aviso")

    def actualizar_click(self):
        conn = sqlite3.connect("dbproductos.bd")
        cursor = conn.cursor()

        # Se cargan los datos indicados de la tabla
        cursor.execute("SELECT codigo, producto, cantidad, precio FROM productos")
        table_info = cursor.fetchall()
        string_list = QStringList()
        database_table_column_count = 4
        database_table_columns = {}
        database_table_items = []
        self.ui.tableWidget.setColumnCount(database_table_column_count)

        self.numerodefilas = len(table_info)
        self.ui.tableWidget.setRowCount(self.numerodefilas)
        for j in range(self.numerodefilas):
            fila = table_info[j]

            for i in range(0, len(fila)):
                elemento = fila[i]
                elemento = str(elemento)

                newitem = QTableWidgetItem(elemento)
                self.ui.tableWidget.setItem(j, i, newitem)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = FrmProductos()
    myapp.show()
    sys.exit(app.exec())
