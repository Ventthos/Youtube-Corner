from InterfacesRaw.MainApp import Ui_MainWindow
from CompleteUI.pantallasCarga import PantallaCargaPorcentaje
from Utilities.Cancion import Cancion

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal

from Utilities.YoutubeUtilities import YoutubeUtilities

from tkinter import messagebox, filedialog


from pytube.exceptions import RegexMatchError
from PIL import Image

class MainApplication(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.pantallaCarga = None
        self.linkActual = ""
        self.queue: [Cancion] = []

        self.songDetailsFieldDownload.hide()
        self.stackedWidget.setCurrentIndex(1)

        self.pushButtonBuscarLink.clicked.connect(self.findSong)
        self.botonCancelDownload.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.buttonOpenDetails.clicked.connect(lambda: self.songDetailsFieldDownload.show())
        self.lineEditTitulo.textChanged.connect(lambda: self.changeInPrevisualizer(self.titleDownloadSong,
                                                                                   self.lineEditTitulo.text()))
        self.lineEditArtista.textChanged.connect(lambda: self.changeInPrevisualizer(self.artistDownloadSong,
                                                                                   self.lineEditArtista.text()))
        self.lineEditAlbum.textChanged.connect(lambda: self.changeInPrevisualizer(self.albumDownloadSong,
                                                                                   self.lineEditAlbum.text()))
        self.botonDownloadSong.clicked.connect(self.startDownloadingSong)

    def findSong(self):
        self.pantallaCarga = PantallaCargaPorcentaje("Buscando su canción, espere por favor...", False)
        self.pantallaCarga.show()

        link = self.lineEditEntradaLink.text()
        self.linkActual = link
        self.thread = FindSongThread(link)
        self.thread.finished.connect(self.onFinishedFindingSong)
        self.thread.error.connect(self.onErrorFindingSong)
        self.thread.start()

    def onFinishedFindingSong(self, songInfo):
        self.pantallaCarga.close()
        self.pantallaCarga = None
        self.thread = None
        self.titleDownloadSong.setText(songInfo[0])
        self.artistDownloadSong.setText(songInfo[1])
        self.albumDownloadSong.setText(songInfo[0])
        self.lineEditTitulo.setText(songInfo[0])
        self.lineEditArtista.setText(songInfo[0])
        self.lineEditArtista.setText(songInfo[1])
        self.lineEditAlbum.setText(songInfo[0])
        self.imgMusicDownload.setPixmap(QPixmap("thumb.png"))
        self.stackedWidget.setCurrentIndex(0)

    def onErrorFindingSong(self, errorMessage):
        self.pantallaCarga.close()
        self.pantallaCarga = None
        self.thread = None
        messagebox.showerror("Error", errorMessage)

    def changeInPrevisualizer(self, widget: QLineEdit, text: str):
        widget.setText(text)

    def startDownloadingSong(self):
        direccion = filedialog.asksaveasfilename(filetypes=(("MP3 Files", "mp3"),), defaultextension=".mp3",
                                                 initialfile=self.titleDownloadSong.text())

        if direccion != "":
            self.pantallaCarga = PantallaCargaPorcentaje("Descargando su canción, espere por favor...",
                                                         True, "0%")
            self.pantallaCarga.show()
            self.thread = DownloadSongThread(self.linkActual, direccion, self.titleDownloadSong.text(),
                                             self.artistDownloadSong.text(), self.albumDownloadSong.text())

            self.thread.avance.connect(self.updatePercentaje)
            self.thread.finished.connect(self.finishDownload)
            self.thread.start()

    def finishDownload(self):
        self.pantallaCarga.close()
        self.pantallaCarga = None
        self.thread = None
        self.stackedWidget.setCurrentIndex(1)
        messagebox.showinfo("Completado", "Su canción se ha descargado exitosamente")

    def updatePercentaje(self, porcentaje):
        self.pantallaCarga.Porcentaje.setText(f"{porcentaje}%")

    def addToQueue(self):
        self.queue.append(Cancion(
            self.titleDownloadSong.text(),
            self.artistDownloadSong.text(),
            self.albumDownloadSong.text(),
            self.linkActual,
            self.imgMusicDownload.pixmap()
        ))
        messagebox.showinfo("Listo", "La canción se ha aregado a la cola, descarguela en la interfaz de cola")


class FindSongThread(QThread):
    finished = pyqtSignal(tuple)
    error = pyqtSignal(str)

    def __init__(self, link):
        super().__init__()
        self.link = link

    def run(self):
        songInfo = []
        try:
            songInfo = YoutubeUtilities.getVideoInfo(self.link)
        except RegexMatchError:
            self.error.emit("La canción no pudo ser encontrada")
            return
        except Exception as e:
            self.error.emit("Hubo un error tratando de encontrar la canción")
            return
        try:
            YoutubeUtilities.download_thumb(self.link, "thumb.png")
        except Exception as e:
            self.error.emit("Hubo un error tratando de conseguir la portada de la canción")
            return
        self.finished.emit(songInfo)



class DownloadSongThread(QThread):
    finished = pyqtSignal()
    avance = pyqtSignal(int)
    error = pyqtSignal(str)

    def __init__(self, link, direccion, titulo_cancion, artista_cancion, album_cancion):
        super().__init__()
        self.link = link
        self.direccion = direccion
        self.titulo_cancion = titulo_cancion
        self.artista_cancion = artista_cancion
        self.album_cancion = album_cancion

    def run(self):
        self.avance.emit(10)
        direccion_mp4 = YoutubeUtilities.downloadMP4File(self.link, "./img/videos", True)
        self.avance.emit(45)
        YoutubeUtilities.MP4ToMP3(direccion_mp4, self.direccion)
        self.avance.emit(80)
        thumbnailraw = Image.open("thumb.png")
        thumbnailraw = thumbnailraw.resize((350, 350))
        thumbnailraw.save("thumb.png")
        self.avance.emit(90)
        YoutubeUtilities.changeAtributesToMP3(self.direccion, self.titulo_cancion, self.artista_cancion,
                                              self.album_cancion,"thumb.png")
        self.avance.emit(100)
        self.finished.emit()



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
