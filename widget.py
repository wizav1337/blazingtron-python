# This Python file uses the following encoding: utf-8
# import os
from pathlib import Path
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QClipboard
from PySide6.QtCore import QFile, QObject
from PySide6.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.load_ui()
        self.leServiceValue = self.findChild(QObject, 'leServiceValue')
        self.vipPrice = self.findChild(QObject, 'vipPrice')
        self.popust0 = self.findChild(QObject, 'popust0')
        self.popust7 = self.findChild(QObject, 'popust7')
        self.popust10 = self.findChild(QObject, 'popust10')
        self.popust12 = self.findChild(QObject, 'popust12')
        self.cut30 = self.findChild(QObject, 'cut30')
        self.cut35 = self.findChild(QObject, 'cut35')
        self.cut40 = self.findChild(QObject, 'cut40')
        self.cut50 = self.findChild(QObject, 'cut50')
        self.exit1 = self.findChild(QObject, 'exit1')
        self.boosterNote = self.findChild(QObject, 'boosterNote')
        self.noteValue = self.findChild(QObject, 'noteValue')
        self.boosterCut = self.findChild(QObject, 'boosterCut')
        self.pcPlatform = self.findChild(QObject, 'pcPlatform')
        self.xboxPlatform = self.findChild(QObject, 'xboxPlatform')
        self.ps4Platform = self.findChild(QObject, 'ps4Platform')
        self.sherpaPlatform = self.findChild(QObject, 'sherpaPlatform')
        self.noteCopy = self.findChild(QObject, 'noteCopy')
        self.copied = self.findChild(QObject, 'copied')
        self.leServiceValue.textChanged.connect(self.update_vip_price)
        self.leServiceValue.textChanged.connect(self.update_cut_price)
        self.boosterNote.textChanged.connect(self.update_platform)
        self.popust0.toggled.connect(self.update_vip_price)
        self.popust7.toggled.connect(self.update_vip_price)
        self.popust10.toggled.connect(self.update_vip_price)
        self.popust12.toggled.connect(self.update_vip_price)
        self.popust0.toggled.connect(self.update_cut_price)
        self.popust7.toggled.connect(self.update_cut_price)
        self.popust10.toggled.connect(self.update_cut_price)
        self.popust12.toggled.connect(self.update_cut_price)
        self.pcPlatform.toggled.connect(self.update_platform)
        self.xboxPlatform.toggled.connect(self.update_platform)
        self.ps4Platform.toggled.connect(self.update_platform)
        self.sherpaPlatform.toggled.connect(self.update_platform)
        self.connect_radio_buttons()
        self.update_cut_price()
        self.update_vip_price()
        self.exit1.clicked.connect(self.close_application)
        self.noteCopy.clicked.connect(self.copy_data)

    def load_ui(self):
        loader = QUiLoader()
        path = Path(__file__).resolve().parent / "form.ui"
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def connect_radio_buttons(self):
        self.popust0.toggled.connect(self.update_vip_price)
        self.popust7.toggled.connect(self.update_vip_price)
        self.popust10.toggled.connect(self.update_vip_price)
        self.popust12.toggled.connect(self.update_vip_price)
        self.cut30.toggled.connect(self.update_cut_price)
        self.cut35.toggled.connect(self.update_cut_price)
        self.cut40.toggled.connect(self.update_cut_price)
        self.cut50.toggled.connect(self.update_cut_price)
        self.pcPlatform.toggled.connect(self.update_platform)
        self.xboxPlatform.toggled.connect(self.update_platform)
        self.ps4Platform.toggled.connect(self.update_platform)
        self.sherpaPlatform.toggled.connect(self.update_platform)

    def update_vip_price(self):
            service_value = self.leServiceValue.text()
            if service_value:
                discount_rate = 0.0
                if self.popust7.isChecked():
                    discount_rate = 0.07
                elif self.popust10.isChecked():
                    discount_rate = 0.10
                elif self.popust12.isChecked():
                    discount_rate = 0.12
                vip_price = float(service_value) * (1.0 - discount_rate)
                self.vipPrice.setText('€{:.2f}'.format(vip_price))
            else:
                self.vipPrice.setText('€0.00')


    def update_cut_price(self):
        service_value = float(self.vipPrice.text()[1:])
        if service_value:
            cut_rate = 0.0
            if self.cut30.isChecked():
                cut_rate = 0.30
            if self.cut35.isChecked():
                cut_rate = 0.35
            if self.cut40.isChecked():
                cut_rate = 0.40
            if self.cut50.isChecked():
                cut_rate = 0.50
            cut_price = float(service_value) * cut_rate
            self.boosterCut.setText('€{:.2f}'.format(cut_price))
        else:
            self.boosterCut.setText('€0.00')

    def update_platform(self):
        platform = self.boosterNote.text()
        if platform:
            platform_sel = 'PC'
            if self.pcPlatform.isChecked():
                platform_sel = 'PC'
            if self.ps4Platform.isChecked():
                platform_sel = 'PS4'
            if self.xboxPlatform.isChecked():
                platform_sel = 'XBOX'
            if self.sherpaPlatform.isChecked():
                platform_sel = 'Sherpa'
            boostercuttext = str(self.boosterCut.text())
            platform_note = f"{platform_sel} - {boostercuttext} - {platform}"
            self.noteValue.setText(platform_note)

    def copy_data(self):
        self.copied.setText('copied')
        clipboard = QApplication.clipboard()
        clipboard.setText(self.noteValue.text())


    def close_application(self):
        QApplication.quit()
















if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
