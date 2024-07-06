from InterfacesRaw.MainApp import Ui_MainWindow
from CompleteUI.pantallasCarga import PantallaCargaPorcentaje
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from threading import Thread
from Utilities.YoutubeUtilities import YoutubeUtilities
from tkinter import messagebox
from pytube.exceptions import RegexMatchError

class MainApplication(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.pantallaCarga = None
        self.songDetailsFieldDownload.hide()
        self.stackedWidget.setCurrentIndex(1)

        self.pushButtonBuscarLink.clicked.connect(self.findSongWithLoadingScreen)
        self.botonCancelDownload.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.buttonOpenDetails.clicked.connect(lambda: self.songDetailsFieldDownload.show())
        self.lineEditTitulo.textChanged.connect(lambda: self.changeInPrevisualizer(self.titleDownloadSong,
                                                                                   self.lineEditTitulo.text()))

    def findSong(self):
        self.pantallaCarga = PantallaCargaPorcentaje("Buscando su canción, espere por favor...", False)
        self.pantallaCarga.show()
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
        print("llegue")
        self.stackedWidget.setCurrentIndex(0)

        self.pantallaCarga.hide()

    def findSongWithLoadingScreen(self):
        self.pantallaCarga = PantallaCargaPorcentaje("Buscando su canción, espere por favor...", False)


    def changeInPrevisualizer(self, widget: QLineEdit, text: str):
        widget.setText(text)


class launchAnyFunction(QThread):
    anySignal = pyqtSignal(int)

    def __init__(self, function, parent = None, index = 0):
        super(launchAnyFunction, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.function = function

    def run(self):
        self.function()
        self.stop()

    def stop(self):
        self.is_running = False
        self.terminate()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
