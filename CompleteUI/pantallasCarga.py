import os

from InterfacesRaw.Carga import Ui_Dialog
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from PyQt5.QtGui import QMovie

class PantallaCargaPorcentaje(QDialog, Ui_Dialog):
    def __init__(self, titulo: str, porcentajeAct: bool, porcentaje: str = ""):
        super().__init__()
        super().setupUi(self)
        ruta_gif = "./img/loading2.gif"

        rutaActual = os.getcwd()
        rutaFinal = os.path.join(rutaActual, "_internal")

        if os.path.exists(rutaFinal):
            ruta_gif = "./_internal/img/loading2.gif"

        self.gif = QMovie(ruta_gif)
        self.imagen.setMovie(self.gif)

        self.Texto.setText(titulo)
        self.setWindowTitle("Cargando...")
        if porcentajeAct:
            self.Porcentaje.setText(porcentaje)
        else:
            self.Porcentaje.hide()

        self.gif.start()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = PantallaCargaPorcentaje("aaaa", False)
    MainWindow.show()
    sys.exit(app.exec_())


