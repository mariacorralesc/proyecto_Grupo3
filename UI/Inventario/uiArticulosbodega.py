# Form implementation generated from reading ui file 'UI_Articulosbodega.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Articulosbodega(object):
    def setupUi(self, Articulosbodega):
        Articulosbodega.setObjectName("Articulosbodega")
        Articulosbodega.resize(956, 632)
        Articulosbodega.setStyleSheet("background-color: rgb(0, 0, 255);\n"
"background-color: rgb(76, 154, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=Articulosbodega)
        self.centralwidget.setObjectName("centralwidget")
        self.txtArticulo = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtArticulo.setGeometry(QtCore.QRect(470, 60, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtArticulo.setFont(font)
        self.txtArticulo.setObjectName("txtArticulo")
        self.btAnadir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btAnadir.setGeometry(QtCore.QRect(430, 360, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btAnadir.setFont(font)
        self.btAnadir.setObjectName("btAnadir")
        self.txtBodega = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtBodega.setGeometry(QtCore.QRect(470, 180, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtBodega.setFont(font)
        self.txtBodega.setObjectName("txtBodega")
        self.btMenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btMenu.setGeometry(QtCore.QRect(850, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btMenu.setFont(font)
        self.btMenu.setObjectName("btMenu")
        self.lblArticulo = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblArticulo.setGeometry(QtCore.QRect(30, 60, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblArticulo.setFont(font)
        self.lblArticulo.setObjectName("lblArticulo")
        self.lblBodega = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblBodega.setGeometry(QtCore.QRect(20, 130, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblBodega.setFont(font)
        self.lblBodega.setObjectName("lblBodega")
        self.lblCantidad = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblCantidad.setGeometry(QtCore.QRect(20, 250, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblCantidad.setFont(font)
        self.lblCantidad.setObjectName("lblCantidad")
        self.txtCantidad = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtCantidad.setGeometry(QtCore.QRect(470, 300, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtCantidad.setFont(font)
        self.txtCantidad.setObjectName("txtCantidad")
        self.tblproductos = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tblproductos.setGeometry(QtCore.QRect(30, 390, 901, 211))
        self.tblproductos.setObjectName("tblproductos")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tblproductos.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tblproductos.addTab(self.tab_2, "")
        Articulosbodega.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=Articulosbodega)
        self.statusbar.setObjectName("statusbar")
        Articulosbodega.setStatusBar(self.statusbar)

        self.retranslateUi(Articulosbodega)
        QtCore.QMetaObject.connectSlotsByName(Articulosbodega)

    def retranslateUi(self, Articulosbodega):
        _translate = QtCore.QCoreApplication.translate
        Articulosbodega.setWindowTitle(_translate("Articulosbodega", "Articulos de Bodega"))
        self.btAnadir.setText(_translate("Articulosbodega", "Añadir"))
        self.btMenu.setText(_translate("Articulosbodega", "Menu"))
        self.lblArticulo.setText(_translate("Articulosbodega", "Ingrese el nombre del artículo a agregar: "))
        self.lblBodega.setText(_translate("Articulosbodega", "Ingrese el nombre de la bodega a la que se asignará el artículo: "))
        self.lblCantidad.setText(_translate("Articulosbodega", "Ingrese la cantidad disponible del artículo en la bodega:"))
        self.tblproductos.setTabText(self.tblproductos.indexOf(self.tab), _translate("Articulosbodega", "Tab 1"))
        self.tblproductos.setTabText(self.tblproductos.indexOf(self.tab_2), _translate("Articulosbodega", "Tab 2"))
