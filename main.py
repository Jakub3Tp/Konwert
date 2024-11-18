import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Cals.textChanged.connect(cent)
        self.show()

    def centimeters_to_cals(self):
        Cm = self.ui.Centimeters.value()
        Cal = Cm * 0.39
        self.ui.Cals.setValue(Cal)

    def meters_to_foots(self):
        M = self.ui.Meters.value()

    def kilometers_to_miles(self):
        Km = self.ui.Kilometers.value()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
