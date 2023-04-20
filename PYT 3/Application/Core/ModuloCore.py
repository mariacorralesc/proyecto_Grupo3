from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Core.uiPrincipal import Ui_Principal
from Application.Modulos.moduloProductos import *

class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        
        self.ui.mnuProductos.triggered.connect(self.onClickMnuProductos)
        self.ui.mnuBodegas.triggered.connect(self.onClickMnuBodegas)
        self.ui.mnuDistribuidores.triggered.connect(self.onClickMnuDistribuidores)
        self.ui.mnuArtBodega.triggered.connect(self.onClickMnuArtBodega)
        self.ui.mnuEntProducto.triggered.connect(self.onClickMnuEntProducto)
        self.pantalla1 = None
        self.pantalla2 = None
        self.pantalla3 = None
        self.pantalla4 = None
        self.pantalla5 = None
        
    def onClickMnuProductos(self):
        self.pantalla1 = FrmProductos()
        self.pantalla1.show()
        
    def onClickMnuBodegas(self):
        self.pantalla1 = Frm()
        self.pantalla1.show()
        
    def onClickMnuDistribuidores(self):
        self.pantalla2 = FrmImprimir()
        self.pantalla2.show()    