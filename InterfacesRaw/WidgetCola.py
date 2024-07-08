# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\InterfacesRaw\WidgetCola.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 155)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frameDownloadMusicDetails = QtWidgets.QFrame(self.widget)
        self.frameDownloadMusicDetails.setStyleSheet("#frameDownloadMusicDetails{\n"
"    background-color: #21324a;\n"
"    border-radius: 12px;\n"
"}\n"
"\n"
"#frameDownloadMusicDetails QLabel{\n"
"    color: white;\n"
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
        icon.addPixmap(QtGui.QPixmap(".\\InterfacesRaw\\../img/basura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonPlayDownload.setIcon(icon)
        self.buttonPlayDownload.setIconSize(QtCore.QSize(25, 25))
        self.buttonPlayDownload.setObjectName("buttonPlayDownload")
        self.horizontalLayout_4.addWidget(self.buttonPlayDownload, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_5.addWidget(self.musicPreviewWidget)
        self.verticalLayout_2.addWidget(self.frameDownloadMusicDetails)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.imgMusicDownload.setText(_translate("Form", "TextLabel"))
        self.titleDownloadSong.setText(_translate("Form", "TextLabel"))
        self.artistDownloadSong.setText(_translate("Form", "TextLabel"))
        self.albumDownloadSong.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())