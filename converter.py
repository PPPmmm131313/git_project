import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow
import requests
from bs4 import BeautifulSoup
from parsing import parse
from otherwindow import Ui_OtherWindow

class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        self.aaa = ""
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()



    def init_UI(self):
        self.setWindowTitle("Converter")

        # self.ui.input_currency.setPlaceholderText("From currency")
        self.ui.input_amount.setPlaceholderText("Amount")
        # self.ui.output_currency.setPlaceholderText("To currency")
        self.ui.outpuy_amount.setPlaceholderText("Amount")

        self.ui.pushButton.clicked.connect(self.converter)
        self.ui.btn_open.clicked.connect(self.openWindow)

    def converter(self):
        input_currency = self.ui.comboBox.currentText()
        output_currency = self.ui.comboBox_2.currentText()
        input_amount = float(self.ui.input_amount.text())
        d = parse()
        if (input_currency == 'USD') & (output_currency == 'RUB'):
            self.ui.outpuy_amount.setText(str(round(input_amount * float(d['sell_dollar'][0]),2)))
            self.aaa = d['sell_dollar'][1] + ", " + d['sell_dollar'][2]
        elif (input_currency == 'RUB') & (output_currency == 'USD'):
            self.ui.outpuy_amount.setText(str(round(input_amount / float(d['buy_dollar'][0]),2)))
            self.aaa = d['buy_dollar'][1] + ", " + d['buy_dollar'][2]
        elif (input_currency == 'EUR') & (output_currency == 'RUB'):
            self.ui.outpuy_amount.setText(str(round(input_amount * float(d['sell_euro'][0]),2)))
            self.aaa = d['sell_euro'][1] + ", " + d['sell_euro'][2]
        elif (input_currency == 'RUB') & (output_currency == 'EUR'):
            self.ui.outpuy_amount.setText(str(round(input_amount / float(d['buy_euro'][0]),2)))
            self.aaa = d['buy_euro'][1] + ", " + d['buy_euro'][2]
        else:
            self.ui.outpuy_amount.setText(str("Use to buy/sell RUB"))
            self.aaa = ""

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui1 = Ui_OtherWindow()
        self.ui1.setupUi(self.window)
        self.window.show()
        self.ui1.OtherWindow.setText(str(self.aaa))




app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
