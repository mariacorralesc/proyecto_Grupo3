import sys
from  PyQt6 import QtCore,QtGui,QtWidgets
from Application.Core.ModuloCore import FrmMain


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FrmMain()
    window.show()
    sys.exit(app.exec())
