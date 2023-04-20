from PyQt6 import QtCore, QtGui, QtWidgets
from UI.Core.uiPrincipal import Ui_Principal
from Application.Modulos.ModuloFunciones import *


class FrmMain(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Principal()
        self.ui.setupUi(self)
        self.ui.menubar.triggered.connect(self.onClickMnuProductos)
        self.ui.menubar.triggered.connect(self.onClickMnuBodegas)
        self.ui.menubar.triggered.connect(self.onClickMnuDistribuidores)
        self.ui.menubar.triggered.connect(self.onClickMnuArtBodega)
        self.ui.menubar.triggered.connect(self.onClickMnuEntProducto)
        self.pantalla1 = None
        self.pantalla2 = None
        self.pantalla3 = None
        self.pantalla4 = None
        self.pantalla5 = None
        
    def onClickMnuProductos(self):
        self.pantalla1 = FrmProductos()
        self.pantalla1.show()
        
    def onClickMnuBodegas(self):
        self.pantalla2 = FrmBodegas()
        self.pantalla2.show()
        
    def onClickMnuDistribuidores(self):
        self.pantalla3 = FrmDistribuidores()
        self.pantalla3.show()    
    
    def onClickMnuArtBodega(self):
        self.pantalla4 = FrmArtBodega()
        self.pantalla4.show()    
        
    def onClickMnuEntProducto(self):
        self.pantalla5 = FrmEntProducto()
        self.pantalla5.show()    