from InterfacesRaw.MainApp import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QPixmap
from Utilities.YoutubeUtilities import YoutubeUtilities
from tkinter import messagebox
from pytube.exceptions import RegexMatchError

class MainApplication(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.songDetailsFieldDownload.hide()
        self.stackedWidget.setCurrentIndex(1)

        self.pushButtonBuscarLink.clicked.connect(self.findSong)
        self.botonCancelDownload.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.buttonOpenDetails.clicked.connect(lambda: self.songDetailsFieldDownload.show())
        self.lineEditTitulo.textChanged.connect(lambda: self.changeInPrevisualizer(self.titleDownloadSong,
                                                                                   self.lineEditTitulo.text()))

    def findSong(self):
        songInfo = []
        link = self.lineEditEntradaLink.text()
        try:
            songInfo = YoutubeUtilities.getVideoInfo(link)
        except RegexMatchError:
            messagebox.showerror("Error", "La canción no pudo ser encontrada")
            return
        except:
            messagebox.showerror("Error", "No se pudo encontrar la canción")
            return
        self.titleDownloadSong.setText(songInfo[0])
        self.artistDownloadSong.setText(songInfo[1])
        self.albumDownloadSong.setText(songInfo[0])
        self.lineEditTitulo.setText(songInfo[0])
        self.lineEditArtista.setText(songInfo[0])
        self.lineEditArtista.setText(songInfo[1])
        self.lineEditAlbum.setText(songInfo[0])

        try:
            YoutubeUtilities.download_thumb(link, "thumb.png")
        except:
            messagebox.showerror("Error", "Hubo un error tratando de conseguir la portada"
                                          "de la canción")
            return
        self.imgMusicDownload.setPixmap(QPixmap("thumb.png"))
        self.stackedWidget.setCurrentIndex(0)

    def changeInPrevisualizer(self, widget: QLineEdit, text: str):
        widget.setText(text)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
