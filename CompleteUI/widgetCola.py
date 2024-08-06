from InterfacesRaw.WidgetCola import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QIcon
from Utilities.Cancion import Cancion
import os


class WidgetCola(Ui_Form, QWidget):
    def __init__(self, cancion: Cancion, window):
        super().__init__()
        super().setupUi(self)
        self.cancion = cancion
        self.widgetDisplay = window
        self.titleDownloadSong.setText(cancion.titulo)
        self.artistDownloadSong.setText(cancion.artista)
        self.albumDownloadSong.setText(cancion.album)
        self.imgMusicDownload.setPixmap(QPixmap(cancion.portada))
        self.buttonPlayDownload.clicked.connect(self.eliminarWidget)

        rutaActual = os.getcwd()
        rutaFinal = os.path.join(rutaActual, "_internal")

        if os.path.exists(rutaFinal):
            self.buttonPlayDownload.setIcon(QIcon("./_internal/img/basura.png"))

    def eliminarWidget(self):
        self.widgetDisplay.deleteFromQueue(self.cancion)