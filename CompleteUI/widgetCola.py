from InterfacesRaw.WidgetCola import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from Utilities.Cancion import Cancion


class WidgetCola(Ui_Form, QWidget):
    def __init__(self, cancion: Cancion):
        super().__init__()
        super().setupUi(self)
        self.cancion = cancion
        self.titleDownloadSong.setText(cancion.titulo)
        self.artistDownloadSong.setText(cancion.artista)
        self.albumDownloadSong.setText(cancion.album)
        self.imgMusicDownload.setPixmap(QPixmap(cancion.portada))
