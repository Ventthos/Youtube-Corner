from InterfacesRaw.Carga import Ui_Dialog
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5.QtGui import QMovie

class PantallaCargaPorcentaje(QMainWindow):
    def __init__(self, titulo: str, porcentajeAct: bool, porcentaje: str = ""):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        ruta_gif = "../img/loading2.gif"
        gif = QMovie(ruta_gif)
        self.ui.imagen.setMovie(gif)
        self.ui.Texto.setText(titulo)
        self.setWindowTitle("Cargando...")
        if porcentajeAct:
            self.ui.Porcentaje.setText(porcentaje)
        else:
            self.ui.Porcentaje.hide()

        gif.start()

        self.show()


