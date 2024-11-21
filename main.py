import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.Centimeters.valueChanged.connect(self.centimeters_to_inches)
        self.ui.Cals.valueChanged.connect(self.inches_to_centimeters)
        self.ui.Meters.valueChanged.connect(self.meters_to_feet)
        self.ui.Foots.valueChanged.connect(self.feet_to_meters)
        self.ui.Kilometers.valueChanged.connect(self.kilometers_to_miles)
        self.ui.Miles.valueChanged.connect(self.miles_to_kilometers)
        self.show()

    def centimeters_to_inches(self):
        cm = self.ui.Centimeters.value()
        inches = cm * 0.393701
        self.ui.Cals.blockSignals(True)
        self.ui.Cals.setValue(inches)
        self.ui.Cals.blockSignals(False)


    def inches_to_centimeters(self):
        inches = self.ui.Cals.value()
        cm = inches / 0.393701
        self.ui.Centimeters.blockSignals(True)
        self.ui.Centimeters.setValue(cm)
        self.ui.Centimeters.blockSignals(False)


    def meters_to_feet(self):
        meters = self.ui.Meters.value()
        feet = meters * 3.28084
        self.ui.Foots.blockSignals(True)
        self.ui.Foots.setValue(feet)
        self.ui.Foots.blockSignals(False)


    def feet_to_meters(self):
        feet = self.ui.Foots.value()
        meters = feet / 3.28084
        self.ui.Meters.blockSignals(True)
        self.ui.Meters.setValue(meters)
        self.ui.Meters.blockSignals(False)


    def kilometers_to_miles(self):
        kilometers = self.ui.Kilometers.value()
        miles = kilometers * 0.621371
        self.ui.Miles.blockSignals(True)
        self.ui.Miles.setValue(miles)
        self.ui.Miles.blockSignals(False)

    def miles_to_kilometers(self):
        miles = self.ui.Miles.value()
        kilometers = miles / 0.621371
        self.ui.Kilometers.blockSignals(True)
        self.ui.Kilometers.setValue(kilometers)
        self.ui.Kilometers.blockSignals(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
