from InterfacesRaw.WidgetCola import Ui_Form
from PyQt5.QtWidgets import QWidget

class WidgetCola(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        super().setupUi(self)