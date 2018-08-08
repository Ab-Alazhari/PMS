

# version 1.2.0     24-2-2018

import sys  # We need sys so that we can pass argv to QApplication
import time
import serial
import serial.tools.list_ports

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QObject, QThread, pyqtSignal, pyqtSlot

import pms_Gui   # This file holds the MainWindow
from about import Ui_About as aboutDlg


class Window(QMainWindow, pms_Gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # call the initialization of the super class
        self.setupUi(self)  # use the UI that is defined pms_Gui.py file
        # list = ports.Get_list()
        self.t = ThreadClass()
        self.t.sig.connect(self.updateUI)
        self.t.start()
        self.Record = True

    def startRecording(self):
        self.Record = True

    def stopRecording(self):
        self.Record = False

    def onAbout(self):
        dialog = QDialog()
        dialog.ui = aboutDlg()
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def updateUI(self, voltage):
        if self.Record:
            timeTag = 'Date-Time ' + time.strftime("%c")
            str = '{0}:\tVoltage: {1}\tVac(rms);\n'.format(timeTag, voltage)
            fw = open('log.txt', 'a')
            fw.write(str)
            fw.close()
        self.lbl_volt_value.setText(voltage)


class ThreadClass(QThread):
    # Create the signal
    sig = pyqtSignal(str)
    voltageCal = 0.288

    def __init__(self, parent=None):
        QThread.__init__(self, parent)

    def measureVoltage(self):
        index = 0
        sum = 0
        while index < 6:
            self.ser.write(bytes('v', 'ascii'))
            line = self.ser.readline()
            print(line)
            count = int(line[:-5])  # this line some times raises exception if received line is not a number
            if (count > 1023) | (count < 0):  # if count > 1023 or < 0 continue
                continue
            voltage = count * self.voltageCal
            sum = sum + voltage
            index = index + 1
        value = sum / 6
        return value

    def run(self):
        while True:
            try:
                self.ser = serial.Serial('COM3', 9600, timeout=2)  # open serial port
                #self.ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)  # open serial port
                break
            except:
                print("No serial port found !!!")
                time.sleep(1)
                continue
        while True:
            try:
                average = self.measureVoltage()
                self.sig.emit(str("%3.0f" % round(average, 1)))     # format the string to three digits and one decimal
            except:
                continue


def main():
    app = QApplication(sys.argv)  # A new instance of QApplication
    form = Window()                     # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()                  # run the main function
