from InterfacesRaw.WidgetCola import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

class WidgetCola(Ui_Form, QWidget):
    def __init__(self, titulo, artista, album, img):
        super().__init__()
        super().setupUi(self)
        self.titleDownloadSong.setText(titulo)
        self.artistDownloadSong.setText(artista)
        self.albumDownloadSong.setText(album)
        self.imgMusicDownload.setPixmap(QPixmap(img))
