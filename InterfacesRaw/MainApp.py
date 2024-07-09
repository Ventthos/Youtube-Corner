# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InterfacesRaw\frontend.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1025, 785)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setStyleSheet("#header{\n"
"    background-color: #111823;\n"
"    border-bottom: 4px solid #37475c;\n"
"}\n"
"\n"
"#header QLabel, QPushButton{\n"
"    color: white;\n"
"}\n"
"\n"
"#headerMenu QPushButton{\n"
"    background-color:  #111823;\n"
"    border: none;\n"
"    padding: 10px 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#headerMenu QPushButton:hover{\n"
"    background-color: #21324a;\n"
"    \n"
"}")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.headerLogo = QtWidgets.QFrame(self.header)
        self.headerLogo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerLogo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerLogo.setObjectName("headerLogo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.headerLogo)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imgLogo = QtWidgets.QLabel(self.headerLogo)
        self.imgLogo.setMaximumSize(QtCore.QSize(40, 40))
        self.imgLogo.setText("")
        self.imgLogo.setPixmap(QtGui.QPixmap(".\\InterfacesRaw\\../img/youtube-app--icon.webp"))
        self.imgLogo.setScaledContents(True)
        self.imgLogo.setObjectName("imgLogo")
        self.horizontalLayout_2.addWidget(self.imgLogo)
        self.stringLogo = QtWidgets.QLabel(self.headerLogo)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stringLogo.setFont(font)
        self.stringLogo.setObjectName("stringLogo")
        self.horizontalLayout_2.addWidget(self.stringLogo)
        self.horizontalLayout.addWidget(self.headerLogo, 0, QtCore.Qt.AlignLeft)
        self.headerMenu = QtWidgets.QFrame(self.header)
        self.headerMenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.headerMenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.headerMenu.setObjectName("headerMenu")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.headerMenu)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.downloadToolButton = QtWidgets.QPushButton(self.headerMenu)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.downloadToolButton.setFont(font)
        self.downloadToolButton.setObjectName("downloadToolButton")
        self.horizontalLayout_3.addWidget(self.downloadToolButton)
        self.queueToolButton = QtWidgets.QPushButton(self.headerMenu)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.queueToolButton.setFont(font)
        self.queueToolButton.setObjectName("queueToolButton")
        self.horizontalLayout_3.addWidget(self.queueToolButton)
        self.editorToolButton = QtWidgets.QPushButton(self.headerMenu)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.editorToolButton.setFont(font)
        self.editorToolButton.setObjectName("editorToolButton")
        self.horizontalLayout_3.addWidget(self.editorToolButton)
        self.horizontalLayout.addWidget(self.headerMenu, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.header)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget.setStyleSheet("#songDownloaderWidget, #findSongWidget, #queueWidget{\n"
"    background-color: #111823;\n"
"}\n"
"\n"
"\n"
"#songDownloaderWidget QLabel, QPushButton, #frameDatosQueue QLabel{\n"
"    color: white;\n"
"}\n"
"\n"
"#buttonOpenDetails{\n"
"    background-color: #21324a;\n"
"    border-radius: 6px;\n"
"    padding: 8px 10px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"#buttonOpenDetails:hover, #detailsSongDownloadScrollContents QPushButton:hover,  #botonCancelDownload:hover, #botonAgregarCola:hover, #buttonReiniciarCola:hover{\n"
"    background-color: #37475c;\n"
"}\n"
"\n"
"#songDetailsFieldDownload{\n"
"    background-color: #4d5b6e;\n"
"}\n"
"\n"
"detailsSongDownloadScroll{\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"#detailsSongDownloadScrollContents{\n"
"    background-color: #4d5b6e;\n"
"    border:none;\n"
"}\n"
"\n"
"#scrollAreaWidgetContentsQueue{\n"
"    background-color: #182334;\n"
"    border:none;\n"
"}\n"
"\n"
"#detailsSongDownloadScrollContents QFrame QLineEdit, #lineEditEntradaLink{\n"
"    background-color: #182334;\n"
"    border: 2px solid #2b3e59;\n"
"    color: white;\n"
"    padding: 4px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"#detailsSongDownloadScrollContents QPushButton, #botonCancelDownload, #botonAgregarCola, #buttonReiniciarCola{\n"
"    background-color: #21324a;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"#botonDownloadSong, #pushButtonBuscarLink, #buttonDescargarCola{\n"
"    background-color: #0d69ef;\n"
"    border:  none;\n"
"    padding: 8px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#botonDownloadSong:hover, #pushButtonBuscarLink:hover, #buttonDescargarCola:hover{\n"
"    background-color:#0c5fd7;\n"
"}\n"
"\n"
"#findSongContainer{\n"
"    background-color: #21324a;\n"
"    border-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#findSongContainer QLabel{\n"
"    color: white;\n"
"}\n"
"\n"
"#lineEditEntradaLink{\n"
"    border: 2px solid #0d69f0 ;\n"
"     border-top-right-radius:0px;\n"
"    border-bottom-right-radius:0px;\n"
"    border-right: none;\n"
"\n"
"}\n"
"\n"
"#pushButtonBuscarLink{\n"
"    border-top-left-radius:0px;\n"
"    border-bottom-left-radius:0px;\n"
"    border: 2px solid #0d69f0 ;\n"
"    border-left: none;\n"
"}\n"
"\n"
" #labelTituloPeso, #labelTituloNCanciones, #buttonReiniciarCola{\n"
"    margin-top: 20px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.songDownloaderWidget = QtWidgets.QWidget()
        self.songDownloaderWidget.setObjectName("songDownloaderWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.songDownloaderWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.songInfoContainer = QtWidgets.QFrame(self.songDownloaderWidget)
        self.songInfoContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songInfoContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songInfoContainer.setObjectName("songInfoContainer")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.songInfoContainer)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frameDownloadMusicDetails = QtWidgets.QFrame(self.songInfoContainer)
        self.frameDownloadMusicDetails.setStyleSheet("#frameDownloadMusicDetails{\n"
"    background-color: #21324a;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#tiempoReproduccionSlider::groove:horizontal{\n"
"    border: 1px solid #16488b;\n"
"    height: 4px;\n"
"}\n"
"\n"
"#tiempoReproduccionSlider::handle:horizontal{\n"
"    background: #0f6af2;\n"
"    width: 13px;\n"
"    margin: -5px -1px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #0f6af2;\n"
"}\n"
"\n"
"#tiempoReproduccionSlider::add-page::horizontal{\n"
"    background-color: #16488b;\n"
"}\n"
"\n"
"\n"
"#tiempoReproduccionSlider::sub-page::horizontal{\n"
"    background-color: #0f6af2;\n"
"}\n"
"\n"
"#buttonPlayDownload{\n"
"    background-color: #0d69ef;\n"
"    border:  none;\n"
"    padding: 8px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#buttonPlayDownload:hover{\n"
"    background-color:#0c5fd7;\n"
"}")
        self.frameDownloadMusicDetails.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDownloadMusicDetails.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDownloadMusicDetails.setObjectName("frameDownloadMusicDetails")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frameDownloadMusicDetails)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.musicPreviewWidget = QtWidgets.QFrame(self.frameDownloadMusicDetails)
        self.musicPreviewWidget.setStyleSheet("")
        self.musicPreviewWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.musicPreviewWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.musicPreviewWidget.setObjectName("musicPreviewWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.musicPreviewWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imgMusicDownload = QtWidgets.QLabel(self.musicPreviewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgMusicDownload.sizePolicy().hasHeightForWidth())
        self.imgMusicDownload.setSizePolicy(sizePolicy)
        self.imgMusicDownload.setMinimumSize(QtCore.QSize(75, 75))
        self.imgMusicDownload.setMaximumSize(QtCore.QSize(80, 80))
        self.imgMusicDownload.setScaledContents(True)
        self.imgMusicDownload.setWordWrap(True)
        self.imgMusicDownload.setObjectName("imgMusicDownload")
        self.horizontalLayout_4.addWidget(self.imgMusicDownload)
        self.stringInfoSongDownload = QtWidgets.QFrame(self.musicPreviewWidget)
        self.stringInfoSongDownload.setStyleSheet("")
        self.stringInfoSongDownload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stringInfoSongDownload.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stringInfoSongDownload.setObjectName("stringInfoSongDownload")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.stringInfoSongDownload)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.titleDownloadSong = QtWidgets.QLabel(self.stringInfoSongDownload)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.titleDownloadSong.setFont(font)
        self.titleDownloadSong.setObjectName("titleDownloadSong")
        self.verticalLayout_3.addWidget(self.titleDownloadSong)
        self.artistDownloadSong = QtWidgets.QLabel(self.stringInfoSongDownload)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.artistDownloadSong.setFont(font)
        self.artistDownloadSong.setObjectName("artistDownloadSong")
        self.verticalLayout_3.addWidget(self.artistDownloadSong)
        self.albumDownloadSong = QtWidgets.QLabel(self.stringInfoSongDownload)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setItalic(True)
        self.albumDownloadSong.setFont(font)
        self.albumDownloadSong.setObjectName("albumDownloadSong")
        self.verticalLayout_3.addWidget(self.albumDownloadSong)
        self.horizontalLayout_4.addWidget(self.stringInfoSongDownload)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.buttonPlayDownload = QtWidgets.QPushButton(self.musicPreviewWidget)
        self.buttonPlayDownload.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\InterfacesRaw\\../img/white-play-icon-png-6.webp"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlayDownload.setIcon(icon)
        self.buttonPlayDownload.setObjectName("buttonPlayDownload")
        self.horizontalLayout_4.addWidget(self.buttonPlayDownload, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.musicPreviewWidget)
        self.reproduccionContainer = QtWidgets.QFrame(self.frameDownloadMusicDetails)
        self.reproduccionContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reproduccionContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reproduccionContainer.setObjectName("reproduccionContainer")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.reproduccionContainer)
        self.verticalLayout_4.setContentsMargins(9, 0, -1, -1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tiempoReproduccionSlider = QtWidgets.QSlider(self.reproduccionContainer)
        self.tiempoReproduccionSlider.setPageStep(1)
        self.tiempoReproduccionSlider.setOrientation(QtCore.Qt.Horizontal)
        self.tiempoReproduccionSlider.setObjectName("tiempoReproduccionSlider")
        self.verticalLayout_4.addWidget(self.tiempoReproduccionSlider)
        self.timeeproductionContainer = QtWidgets.QFrame(self.reproduccionContainer)
        self.timeeproductionContainer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.timeeproductionContainer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeeproductionContainer.setObjectName("timeeproductionContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.timeeproductionContainer)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pastTimeReproduction = QtWidgets.QLabel(self.timeeproductionContainer)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pastTimeReproduction.setFont(font)
        self.pastTimeReproduction.setObjectName("pastTimeReproduction")
        self.horizontalLayout_5.addWidget(self.pastTimeReproduction)
        self.restingTimeReproduction = QtWidgets.QLabel(self.timeeproductionContainer)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.restingTimeReproduction.setFont(font)
        self.restingTimeReproduction.setObjectName("restingTimeReproduction")
        self.horizontalLayout_5.addWidget(self.restingTimeReproduction, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_4.addWidget(self.timeeproductionContainer)
        self.verticalLayout_5.addWidget(self.reproduccionContainer)
        self.verticalLayout_8.addWidget(self.frameDownloadMusicDetails)
        self.detailSongsDownload = QtWidgets.QFrame(self.songInfoContainer)
        self.detailSongsDownload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.detailSongsDownload.setFrameShadow(QtWidgets.QFrame.Raised)
        self.detailSongsDownload.setObjectName("detailSongsDownload")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.detailSongsDownload)
        self.verticalLayout_7.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.buttonOpenDetails = QtWidgets.QPushButton(self.detailSongsDownload)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.buttonOpenDetails.setFont(font)
        self.buttonOpenDetails.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOpenDetails.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonOpenDetails.setStyleSheet("")
        self.buttonOpenDetails.setIcon(icon)
        self.buttonOpenDetails.setObjectName("buttonOpenDetails")
        self.verticalLayout_7.addWidget(self.buttonOpenDetails)
        self.songDetailsFieldDownload = QtWidgets.QFrame(self.detailSongsDownload)
        self.songDetailsFieldDownload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.songDetailsFieldDownload.setFrameShadow(QtWidgets.QFrame.Raised)
        self.songDetailsFieldDownload.setObjectName("songDetailsFieldDownload")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.songDetailsFieldDownload)
        self.verticalLayout_6.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.detailsSongDownloadScroll = QtWidgets.QScrollArea(self.songDetailsFieldDownload)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.detailsSongDownloadScroll.sizePolicy().hasHeightForWidth())
        self.detailsSongDownloadScroll.setSizePolicy(sizePolicy)
        self.detailsSongDownloadScroll.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.detailsSongDownloadScroll.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.detailsSongDownloadScroll.setWidgetResizable(True)
        self.detailsSongDownloadScroll.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.detailsSongDownloadScroll.setObjectName("detailsSongDownloadScroll")
        self.detailsSongDownloadScrollContents = QtWidgets.QWidget()
        self.detailsSongDownloadScrollContents.setGeometry(QtCore.QRect(0, 0, 478, 313))
        self.detailsSongDownloadScrollContents.setObjectName("detailsSongDownloadScrollContents")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.detailsSongDownloadScrollContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frameInfoSong = QtWidgets.QFrame(self.detailsSongDownloadScrollContents)
        self.frameInfoSong.setStyleSheet("")
        self.frameInfoSong.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInfoSong.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfoSong.setObjectName("frameInfoSong")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frameInfoSong)
        self.verticalLayout_9.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelTitulo = QtWidgets.QLabel(self.frameInfoSong)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelTitulo.setFont(font)
        self.labelTitulo.setObjectName("labelTitulo")
        self.verticalLayout_9.addWidget(self.labelTitulo)
        self.lineEditTitulo = QtWidgets.QLineEdit(self.frameInfoSong)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditTitulo.sizePolicy().hasHeightForWidth())
        self.lineEditTitulo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditTitulo.setFont(font)
        self.lineEditTitulo.setAcceptDrops(False)
        self.lineEditTitulo.setFrame(True)
        self.lineEditTitulo.setReadOnly(False)
        self.lineEditTitulo.setObjectName("lineEditTitulo")
        self.verticalLayout_9.addWidget(self.lineEditTitulo)
        self.verticalLayout_10.addWidget(self.frameInfoSong)
        self.frameInfoSong_2 = QtWidgets.QFrame(self.detailsSongDownloadScrollContents)
        self.frameInfoSong_2.setStyleSheet("")
        self.frameInfoSong_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInfoSong_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfoSong_2.setObjectName("frameInfoSong_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frameInfoSong_2)
        self.verticalLayout_11.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.labelArtista = QtWidgets.QLabel(self.frameInfoSong_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelArtista.setFont(font)
        self.labelArtista.setObjectName("labelArtista")
        self.verticalLayout_11.addWidget(self.labelArtista)
        self.lineEditArtista = QtWidgets.QLineEdit(self.frameInfoSong_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditArtista.sizePolicy().hasHeightForWidth())
        self.lineEditArtista.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditArtista.setFont(font)
        self.lineEditArtista.setAcceptDrops(False)
        self.lineEditArtista.setFrame(True)
        self.lineEditArtista.setReadOnly(False)
        self.lineEditArtista.setObjectName("lineEditArtista")
        self.verticalLayout_11.addWidget(self.lineEditArtista)
        self.verticalLayout_10.addWidget(self.frameInfoSong_2)
        self.frameInfoSong_3 = QtWidgets.QFrame(self.detailsSongDownloadScrollContents)
        self.frameInfoSong_3.setStyleSheet("")
        self.frameInfoSong_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInfoSong_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInfoSong_3.setObjectName("frameInfoSong_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frameInfoSong_3)
        self.verticalLayout_12.setContentsMargins(-1, 6, -1, 6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.labelTituloAlbum = QtWidgets.QLabel(self.frameInfoSong_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelTituloAlbum.setFont(font)
        self.labelTituloAlbum.setObjectName("labelTituloAlbum")
        self.verticalLayout_12.addWidget(self.labelTituloAlbum)
        self.lineEditAlbum = QtWidgets.QLineEdit(self.frameInfoSong_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditAlbum.sizePolicy().hasHeightForWidth())
        self.lineEditAlbum.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEditAlbum.setFont(font)
        self.lineEditAlbum.setAcceptDrops(False)
        self.lineEditAlbum.setFrame(True)
        self.lineEditAlbum.setReadOnly(False)
        self.lineEditAlbum.setObjectName("lineEditAlbum")
        self.verticalLayout_12.addWidget(self.lineEditAlbum)
        self.verticalLayout_10.addWidget(self.frameInfoSong_3)
        self.frameBotonesDetailDownload = QtWidgets.QFrame(self.detailsSongDownloadScrollContents)
        self.frameBotonesDetailDownload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBotonesDetailDownload.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBotonesDetailDownload.setObjectName("frameBotonesDetailDownload")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frameBotonesDetailDownload)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.editarPortadaDownloadButton = QtWidgets.QPushButton(self.frameBotonesDetailDownload)
        self.editarPortadaDownloadButton.setObjectName("editarPortadaDownloadButton")
        self.horizontalLayout_7.addWidget(self.editarPortadaDownloadButton)
        self.editarAudioDownloadButton = QtWidgets.QPushButton(self.frameBotonesDetailDownload)
        self.editarAudioDownloadButton.setObjectName("editarAudioDownloadButton")
        self.horizontalLayout_7.addWidget(self.editarAudioDownloadButton)
        self.verticalLayout_10.addWidget(self.frameBotonesDetailDownload)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem1)
        self.detailsSongDownloadScroll.setWidget(self.detailsSongDownloadScrollContents)
        self.verticalLayout_6.addWidget(self.detailsSongDownloadScroll)
        self.verticalLayout_7.addWidget(self.songDetailsFieldDownload)
        self.verticalLayout_8.addWidget(self.detailSongsDownload)
        self.frameBotonesFinales = QtWidgets.QFrame(self.songInfoContainer)
        self.frameBotonesFinales.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBotonesFinales.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBotonesFinales.setObjectName("frameBotonesFinales")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frameBotonesFinales)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.botonCancelDownload = QtWidgets.QPushButton(self.frameBotonesFinales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botonCancelDownload.setFont(font)
        self.botonCancelDownload.setObjectName("botonCancelDownload")
        self.horizontalLayout_6.addWidget(self.botonCancelDownload)
        self.botonAgregarCola = QtWidgets.QPushButton(self.frameBotonesFinales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botonAgregarCola.setFont(font)
        self.botonAgregarCola.setObjectName("botonAgregarCola")
        self.horizontalLayout_6.addWidget(self.botonAgregarCola)
        self.botonDownloadSong = QtWidgets.QPushButton(self.frameBotonesFinales)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botonDownloadSong.setFont(font)
        self.botonDownloadSong.setObjectName("botonDownloadSong")
        self.horizontalLayout_6.addWidget(self.botonDownloadSong)
        self.verticalLayout_8.addWidget(self.frameBotonesFinales, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_2.addWidget(self.songInfoContainer, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.songDownloaderWidget)
        self.findSongWidget = QtWidgets.QWidget()
        self.findSongWidget.setObjectName("findSongWidget")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.findSongWidget)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.findSongContainer = QtWidgets.QWidget(self.findSongWidget)
        self.findSongContainer.setObjectName("findSongContainer")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.findSongContainer)
        self.verticalLayout_14.setContentsMargins(30, 40, 30, 40)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label = QtWidgets.QLabel(self.findSongContainer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_14.addWidget(self.label)
        self.line = QtWidgets.QFrame(self.findSongContainer)
        self.line.setMinimumSize(QtCore.QSize(500, 0))
        self.line.setMaximumSize(QtCore.QSize(500, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_14.addWidget(self.line, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.findSongContainer)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_14.addWidget(self.label_2)
        self.frameEntradasLink = QtWidgets.QFrame(self.findSongContainer)
        self.frameEntradasLink.setStyleSheet("")
        self.frameEntradasLink.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEntradasLink.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEntradasLink.setObjectName("frameEntradasLink")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frameEntradasLink)
        self.horizontalLayout_8.setContentsMargins(0, 20, 0, -1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEditEntradaLink = QtWidgets.QLineEdit(self.frameEntradasLink)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditEntradaLink.setFont(font)
        self.lineEditEntradaLink.setObjectName("lineEditEntradaLink")
        self.horizontalLayout_8.addWidget(self.lineEditEntradaLink)
        self.pushButtonBuscarLink = QtWidgets.QPushButton(self.frameEntradasLink)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBuscarLink.sizePolicy().hasHeightForWidth())
        self.pushButtonBuscarLink.setSizePolicy(sizePolicy)
        self.pushButtonBuscarLink.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\InterfacesRaw\\../img/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonBuscarLink.setIcon(icon1)
        self.pushButtonBuscarLink.setIconSize(QtCore.QSize(13, 13))
        self.pushButtonBuscarLink.setObjectName("pushButtonBuscarLink")
        self.horizontalLayout_8.addWidget(self.pushButtonBuscarLink)
        self.verticalLayout_14.addWidget(self.frameEntradasLink)
        self.verticalLayout_13.addWidget(self.findSongContainer, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_2 = QtWidgets.QFrame(self.findSongWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_13.addWidget(self.frame_2)
        self.verticalLayout_13.setStretch(0, 5)
        self.verticalLayout_13.setStretch(1, 1)
        self.stackedWidget.addWidget(self.findSongWidget)
        self.queueWidget = QtWidgets.QWidget()
        self.queueWidget.setObjectName("queueWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.queueWidget)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.scrollAreaQueue = QtWidgets.QScrollArea(self.queueWidget)
        self.scrollAreaQueue.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaQueue.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollAreaQueue.setWidgetResizable(True)
        self.scrollAreaQueue.setObjectName("scrollAreaQueue")
        self.scrollAreaWidgetContentsQueue = QtWidgets.QWidget()
        self.scrollAreaWidgetContentsQueue.setGeometry(QtCore.QRect(0, 0, 664, 677))
        self.scrollAreaWidgetContentsQueue.setObjectName("scrollAreaWidgetContentsQueue")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContentsQueue)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.scrollAreaQueue.setWidget(self.scrollAreaWidgetContentsQueue)
        self.horizontalLayout_9.addWidget(self.scrollAreaQueue)
        self.frameDerechoQueue = QtWidgets.QFrame(self.queueWidget)
        self.frameDerechoQueue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDerechoQueue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDerechoQueue.setObjectName("frameDerechoQueue")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frameDerechoQueue)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frameDatosQueue = QtWidgets.QFrame(self.frameDerechoQueue)
        self.frameDatosQueue.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameDatosQueue.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameDatosQueue.setObjectName("frameDatosQueue")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frameDatosQueue)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.tituloQueue = QtWidgets.QLabel(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tituloQueue.setFont(font)
        self.tituloQueue.setAlignment(QtCore.Qt.AlignCenter)
        self.tituloQueue.setObjectName("tituloQueue")
        self.verticalLayout_15.addWidget(self.tituloQueue)
        self.line_2 = QtWidgets.QFrame(self.frameDatosQueue)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_15.addWidget(self.line_2)
        self.labelTituloNCanciones = QtWidgets.QLabel(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTituloNCanciones.setFont(font)
        self.labelTituloNCanciones.setObjectName("labelTituloNCanciones")
        self.verticalLayout_15.addWidget(self.labelTituloNCanciones)
        self.labelDisplayNCanciones = QtWidgets.QLabel(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelDisplayNCanciones.setFont(font)
        self.labelDisplayNCanciones.setObjectName("labelDisplayNCanciones")
        self.verticalLayout_15.addWidget(self.labelDisplayNCanciones)
        self.labelTituloPeso = QtWidgets.QLabel(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.labelTituloPeso.setFont(font)
        self.labelTituloPeso.setObjectName("labelTituloPeso")
        self.verticalLayout_15.addWidget(self.labelTituloPeso)
        self.labelDisplayPeso = QtWidgets.QLabel(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.labelDisplayPeso.setFont(font)
        self.labelDisplayPeso.setObjectName("labelDisplayPeso")
        self.verticalLayout_15.addWidget(self.labelDisplayPeso)
        self.buttonReiniciarCola = QtWidgets.QPushButton(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.buttonReiniciarCola.setFont(font)
        self.buttonReiniciarCola.setObjectName("buttonReiniciarCola")
        self.verticalLayout_15.addWidget(self.buttonReiniciarCola)
        self.buttonDescargarCola = QtWidgets.QPushButton(self.frameDatosQueue)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.buttonDescargarCola.setFont(font)
        self.buttonDescargarCola.setObjectName("buttonDescargarCola")
        self.verticalLayout_15.addWidget(self.buttonDescargarCola)
        self.verticalLayout_16.addWidget(self.frameDatosQueue)
        spacerItem2 = QtWidgets.QSpacerItem(20, 369, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem2)
        self.horizontalLayout_9.addWidget(self.frameDerechoQueue)
        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 1)
        self.stackedWidget.addWidget(self.queueWidget)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.stringLogo.setText(_translate("MainWindow", "Youtube Corner"))
        self.downloadToolButton.setText(_translate("MainWindow", "Descargar Música"))
        self.queueToolButton.setText(_translate("MainWindow", "Cola de Descarga"))
        self.editorToolButton.setText(_translate("MainWindow", "Editar MP3"))
        self.imgMusicDownload.setText(_translate("MainWindow", "TextLabel"))
        self.titleDownloadSong.setText(_translate("MainWindow", "TextLabel"))
        self.artistDownloadSong.setText(_translate("MainWindow", "TextLabel"))
        self.albumDownloadSong.setText(_translate("MainWindow", "TextLabel"))
        self.pastTimeReproduction.setText(_translate("MainWindow", "0:00"))
        self.restingTimeReproduction.setText(_translate("MainWindow", "3:49"))
        self.buttonOpenDetails.setText(_translate("MainWindow", "Song Details"))
        self.labelTitulo.setText(_translate("MainWindow", "Título"))
        self.lineEditTitulo.setPlaceholderText(_translate("MainWindow", "Título"))
        self.labelArtista.setText(_translate("MainWindow", "Artista"))
        self.lineEditArtista.setPlaceholderText(_translate("MainWindow", "Artista"))
        self.labelTituloAlbum.setText(_translate("MainWindow", "Album"))
        self.lineEditAlbum.setPlaceholderText(_translate("MainWindow", "Album"))
        self.editarPortadaDownloadButton.setText(_translate("MainWindow", "Editar portada"))
        self.editarAudioDownloadButton.setText(_translate("MainWindow", "Editar audio"))
        self.botonCancelDownload.setText(_translate("MainWindow", "Volver"))
        self.botonAgregarCola.setText(_translate("MainWindow", "Agregar a la cola"))
        self.botonDownloadSong.setText(_translate("MainWindow", "Descargar"))
        self.label.setText(_translate("MainWindow", "Descargas"))
        self.label_2.setText(_translate("MainWindow", "Copie el link de Youtube en el siguiente campo y aprete el botón para empezar la búsqueda"))
        self.tituloQueue.setText(_translate("MainWindow", "Cola"))
        self.labelTituloNCanciones.setText(_translate("MainWindow", "Cantidad de canciones"))
        self.labelDisplayNCanciones.setText(_translate("MainWindow", "TextLabel"))
        self.labelTituloPeso.setText(_translate("MainWindow", "Tamaño aproximado"))
        self.labelDisplayPeso.setText(_translate("MainWindow", "TextLabel"))
        self.buttonReiniciarCola.setText(_translate("MainWindow", "Vaciar Cola"))
        self.buttonDescargarCola.setText(_translate("MainWindow", "Descargar Cola"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
