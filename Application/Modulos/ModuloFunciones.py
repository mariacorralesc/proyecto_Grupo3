import traceback
from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Inventario.uilistaproductos import Ui_UI_Productos
from UI.Inventario.uilistabodegas import Ui_UI_Bodegas
from UI.Inventario.uilistadistribuidores import Ui_UI_Distribuidores
from UI.Inventario.uiartbodega import Ui_UI_ArtBodega
from UI.Inventario.uientproducto import Ui_UI_EntProducto
from Dominio.Inventario.Entities import Productos, Bodega, Distribuidores
from Application.Core.CoreApp import *
import sqlite3
import sys


class FrmProductos(QtWidgets.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UI_Productos()
        self.ui.setupUi(self)
        # self.oProducto = None
        # self.modelolista = QtGui.QStandardItemModel()
        # self.ui.lstProducto.setModel(self.modelolista)

        # self.ui.btGuardar.clicked.connect(
        #     self.btGuardar_clicked_GuardarProducto)

        # def btGuardar_clicked_GuardarProducto(self):
        #     self.oProducto = Productos()
        #     self.oProducto.codigo = self.ui.txtCodigo.text()
        #     self.oProducto.cantidad = self.ui.txtCantidad.text()
        #     self.oProducto.producto = self.ui.txtProducto.text()
        #     self.oProducto.precio = float(self.ui.txtPrecio.text())
        #     itemView = (self.oProducto.codigo + " " +
        #                 self.oProducto.producto + " " +
        #                 self.oProducto.cantidad + " " +
        #                 str(self.oProducto.precio))
        #     item = QtGui.QStandardItem(itemView)
        #     self.modelolista.appendRow(item)
        #     Persistencia.agregarProducto(self.oProducto)


class FrmBodegas(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UI_Bodegas()
        self.ui.setupUi(self)


class FrmDistribuidores(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UI_Distribuidores()
        self.ui.setupUi(self)


class FrmArtBodega(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UI_ArtBodega()
        self.ui.setupUi(self)

    #     self.ui.btGuardar.clicked.connect(self.guardar_click)
    #     self.ui.btActualizar.clicked.connect(self.actualizar_click)
    #     self.iniciar_basede_datos()

    # # Iniciamos la base de datos y creamos la tabla si no existe
    # def iniciar_basede_datos(self):
    #     self.conn = sqlite3.connect("dbproductos.bd")
    #     cursor = self.conn.cursor()
    #     cursor.execute("""CREATE TABLE IF NOT EXISTS productos (
    #         codigo TEXT NOT NULL,
    #         producto TEXT NOT NULL,
    #         cantidad TEXT NOT NULL,
    #         precio TEXT NOT NULL)""")
    #     self.conn.commit()

    # def guardar_click(self):
    #     conn = sqlite3.connect("dbproductos.bd")
    #     cursor = conn.cursor()
    #     self.codigo = str(self.ui.txtCodigo.text())
    #     self.producto = str(self.ui.txtProducto.text())
    #     self.cantidad = str(self.ui.txtCantidad.text())
    #     self.precio = str(self.ui.txtPrecio.text())

    #     self.registro = (self.codigo, self.producto,
    #                      self.cantidad, self.precio)

    #     cursor.execute(
    #         "INSERT INTO productos (codigo,producto,cantidad,precio) VALUES (?,?,?,?)", self.registro)

    #     conn.commit()
    #     self.ui.lineEdit.setText("")
    #     conn.commit()
    #     QMessageBox.about(self, "Registro guardado", "Aviso")

    # def actualizar_click(self):
    #     conn = sqlite3.connect("dbproductos.bd")
    #     cursor = conn.cursor()

    #     # Se cargan los datos indicados de la tabla
    #     cursor.execute(
    #         "SELECT codigo, producto, cantidad, precio FROM productos")
    #     table_info = cursor.fetchall()
    #     string_list = QStringListModel()
    #     database_table_column_count = 4
    #     database_table_columns = {}
    #     database_table_items = []
    #     self.ui.tableWidget.setColumnCount(database_table_column_count)

    #     self.numerodefilas = len(table_info)
    #     self.ui.tableWidget.setRowCount(self.numerodefilas)
    #     for j in range(self.numerodefilas):
    #         fila = table_info[j]

    #         for i in range(0, len(fila)):
    #             elemento = fila[i]
    #             elemento = str(elemento)

    #             newitem = QTableWidgetItem(elemento)
    #             self.ui.tableWidget.setItem(j, i, newitem)


class FrmEntProducto(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_UI_EntProducto()
        self.ui.setupUi(self)
