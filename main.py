import os
import random

from InterfacesRaw.MainApp import Ui_MainWindow
from CompleteUI.pantallasCarga import PantallaCargaPorcentaje
from Utilities.Cancion import Cancion
from CompleteUI.widgetCola import WidgetCola

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5 import QtCore

from Utilities.YoutubeUtilities import YoutubeUtilities

from tkinter import messagebox, filedialog
import re

from pytube.exceptions import RegexMatchError
import random

from PIL import Image

class MainApplication(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.pantallaCarga = None
        self.linkActual = ""
        self.queue: [Cancion] = []
        #self.barraSpaceadora = QSpacerItem(20, 200, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_17.setAlignment(QtCore.Qt.AlignTop)

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
        self.downloadToolButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.queueToolButton.clicked.connect(self.showQueue)
        self.botonAgregarCola.clicked.connect(self.addToQueue)
        self.buttonDescargarCola.clicked.connect(self.downloadQueue)

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
        randomNumber = random.randint(0, 10000)
        ruta = f"img/videos/thumb_{randomNumber}.png"

        while os.path.exists(ruta):
            ruta = f"img/videos/thumb_{random.randint(0, 10000)}.png"
            print(ruta)

        os.replace("thumb.png", ruta)
        self.queue.append(Cancion(
            self.titleDownloadSong.text(),
            self.artistDownloadSong.text(),
            self.albumDownloadSong.text(),
            self.linkActual,
            ruta
            # pytube.YouTube(self.linkActual).streams.get_audio_only().filesize_mb
        ))
        self.stackedWidget.setCurrentIndex(1)
        messagebox.showinfo("Listo", "La canción se ha aregado a la cola, descarguela en la interfaz de cola")

    def showQueue(self):
        self.stackedWidget.setCurrentIndex(2)
        for i in range(self.verticalLayout_17.count()-1, -1, -1):
            self.verticalLayout_17.itemAt(i).widget().hide()
            self.verticalLayout_17.removeWidget(self.verticalLayout_17.itemAt(i).widget())
        for cancion in self.queue:
            widget = WidgetCola(cancion)
            self.verticalLayout_17.addWidget(widget)

    def downloadQueue(self):
        direccion = filedialog.askdirectory()

        if direccion != "":
            self.pantallaCarga = PantallaCargaPorcentaje("Descargando cola, espere por favor...",
                                                         True, "0%")
            self.pantallaCarga.show()
            self.thread = DownloadQueueThread(self.queue, direccion)

        self.thread.avance.connect(self.updatePercentaje)
        self.thread.finished.connect(self.finishDownload)
        self.thread.start()


    def closeEvent(self, event):
        super().closeEvent(event)
        for imagen in os.listdir("img/videos"):
            f = os.path.join("img/videos", imagen)
            os.remove(f)




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

    def __init__(self, link, direccion, titulo_cancion, artista_cancion, album_cancion, imagenRoute = "thumb.png"):
        super().__init__()
        self.link = link
        self.direccion = direccion
        self.titulo_cancion = titulo_cancion
        self.artista_cancion = artista_cancion
        self.album_cancion = album_cancion
        self.imagen = imagenRoute

    def run(self):
        self.avance.emit(10)
        direccion_mp4 = YoutubeUtilities.downloadMP4File(self.link, "./img/videos", True)
        self.avance.emit(45)
        YoutubeUtilities.MP4ToMP3(direccion_mp4, self.direccion)
        self.avance.emit(80)
        thumbnailraw = Image.open(self.imagen)
        thumbnailraw = thumbnailraw.resize((350, 350))
        thumbnailraw.save(self.imagen)
        self.avance.emit(90)
        YoutubeUtilities.changeAtributesToMP3(self.direccion, self.titulo_cancion, self.artista_cancion,
                                              self.album_cancion,self.imagen)
        self.avance.emit(100)
        self.finished.emit()


class DownloadQueueThread(QThread):
    finished = pyqtSignal()
    avance = pyqtSignal(float)
    error = pyqtSignal(str)

    def __init__(self, queue: [Cancion], direccion):
        self.cancionesDescargadas = 0
        self.queue: [Cancion] = queue
        self.direccion = direccion
        super().__init__()

    def run(self):
        for cancion in self.queue:
            tituloLimpio = self.eliminar_signos_raros(cancion.titulo)
            direccionCancion = os.path.join(self.direccion, tituloLimpio)
            direccionCancion = direccionCancion + ".mp3"
            direccion_mp4 = YoutubeUtilities.downloadMP4File(cancion.link, "./img/videos", True)
            YoutubeUtilities.MP4ToMP3(direccion_mp4, direccionCancion)
            thumbnailraw = Image.open(cancion.portada)
            thumbnailraw = thumbnailraw.resize((350, 350))
            thumbnailraw.save(cancion.portada)
            YoutubeUtilities.changeAtributesToMP3(direccionCancion, cancion.titulo, cancion.artista,
                                                  cancion.album, cancion.portada)
            self.cancionesDescargadas += 1
            self.avance.emit(self.cancionesDescargadas/len(self.queue) * 100)
        self.finished.emit()

    def eliminar_signos_raros(self, texto):
        # Usar una expresión regular para conservar solo caracteres alfanuméricos y espacios
        texto_limpio = re.sub(r'[^a-zA-Z0-9\s]', '', texto)
        return texto_limpio

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainApplication()
    MainWindow.show()
    sys.exit(app.exec_())
