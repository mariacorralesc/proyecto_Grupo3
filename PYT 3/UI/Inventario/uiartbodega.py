# Form implementation generated from reading ui file 'UI_ArtBodega.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_UI_ArtBodega(object):
    def setupUi(self, UI_ArtBodega):
        UI_ArtBodega.setObjectName("UI_ArtBodega")
        UI_ArtBodega.resize(1010, 662)
        self.txtBodega = QtWidgets.QLineEdit(parent=UI_ArtBodega)
        self.txtBodega.setGeometry(QtCore.QRect(500, 190, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtBodega.setFont(font)
        self.txtBodega.setObjectName("txtBodega")
        self.btMenu = QtWidgets.QPushButton(parent=UI_ArtBodega)
        self.btMenu.setGeometry(QtCore.QRect(880, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btMenu.setFont(font)
        self.btMenu.setObjectName("btMenu")
        self.lblBodega = QtWidgets.QLabel(parent=UI_ArtBodega)
        self.lblBodega.setGeometry(QtCore.QRect(50, 140, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblBodega.setFont(font)
        self.lblBodega.setObjectName("lblBodega")
        self.lblArticulo = QtWidgets.QLabel(parent=UI_ArtBodega)
        self.lblArticulo.setGeometry(QtCore.QRect(60, 70, 441, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblArticulo.setFont(font)
        self.lblArticulo.setObjectName("lblArticulo")
        self.lblCantidad = QtWidgets.QLabel(parent=UI_ArtBodega)
        self.lblCantidad.setGeometry(QtCore.QRect(50, 260, 691, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.lblCantidad.setFont(font)
        self.lblCantidad.setObjectName("lblCantidad")
        self.txtArticulo = QtWidgets.QLineEdit(parent=UI_ArtBodega)
        self.txtArticulo.setGeometry(QtCore.QRect(500, 70, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtArticulo.setFont(font)
        self.txtArticulo.setObjectName("txtArticulo")
        self.tblproductos = QtWidgets.QTabWidget(parent=UI_ArtBodega)
        self.tblproductos.setGeometry(QtCore.QRect(60, 400, 901, 211))
        self.tblproductos.setObjectName("tblproductos")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tblproductos.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tblproductos.addTab(self.tab_2, "")
        self.txtCantidad = QtWidgets.QLineEdit(parent=UI_ArtBodega)
        self.txtCantidad.setGeometry(QtCore.QRect(500, 310, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.txtCantidad.setFont(font)
        self.txtCantidad.setObjectName("txtCantidad")
        self.btAnadir = QtWidgets.QPushButton(parent=UI_ArtBodega)
        self.btAnadir.setGeometry(QtCore.QRect(460, 370, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.btAnadir.setFont(font)
        self.btAnadir.setObjectName("btAnadir")

        self.retranslateUi(UI_ArtBodega)
        QtCore.QMetaObject.connectSlotsByName(UI_ArtBodega)

    def retranslateUi(self, UI_ArtBodega):
        _translate = QtCore.QCoreApplication.translate
        UI_ArtBodega.setWindowTitle(_translate("UI_ArtBodega", "Dialog"))
        self.btMenu.setText(_translate("UI_ArtBodega", "Menu"))
        self.lblBodega.setText(_translate("UI_ArtBodega", "Ingrese el nombre de la bodega a la que se asignará el artículo: "))
        self.lblArticulo.setText(_translate("UI_ArtBodega", "Ingrese el nombre del artículo a agregar: "))
        self.lblCantidad.setText(_translate("UI_ArtBodega", "Ingrese la cantidad disponible del artículo en la bodega:"))
        self.tblproductos.setTabText(self.tblproductos.indexOf(self.tab), _translate("UI_ArtBodega", "Tab 1"))
        self.tblproductos.setTabText(self.tblproductos.indexOf(self.tab_2), _translate("UI_ArtBodega", "Tab 2"))
        self.btAnadir.setText(_translate("UI_ArtBodega", "Añadir"))
