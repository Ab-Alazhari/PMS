# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(661, 599)
        self.verticalLayout = QtWidgets.QVBoxLayout(About)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(About)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "حول"))
        self.label_2.setText(_translate("About", "<html><head/><body><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:14pt;\">هذا البرنامج مقدم ضمن مشروع تخرج استكمالاً لمتطلبات الدبلوم العالي الهندسي التقني بعنوان</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">:</span></p><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:28pt; font-weight:600;\">مراقبة جهد الشبكة العامة للكهرباءبإستخدام الحاسوب والأردوينو</span></p><p align=\"right\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">اعداد الطالب:</span></p><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt; font-weight:600;\">      عبدالرحمن علي المختار الأزهري</span></p><p align=\"right\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">تحت اشراف :</span></p><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt; font-weight:600;\">      أ. علاء القيب</span></p><p align=\"right\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">العام الدراسي : </span></p><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">2017-2018</span></p><p align=\"center\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:11pt;\">تاريخ هذا الإصدار: 8/2/2018</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

