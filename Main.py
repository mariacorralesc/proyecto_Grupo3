import sys
from  PyQt6 import QtCore,QtGui,QtWidgets
from Application.Core.moduloCore import FrmMain


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FrmMain()
    window.show()
    sys.exit(app.exec())
