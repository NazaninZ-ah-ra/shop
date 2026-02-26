from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogConfirm(object):
    def __init__(self , msg , title):
        self.msg = msg 
        self.title = title
    def setupUi(self, DialogConfirm):
        DialogConfirm.setObjectName("DialogConfirm")
        DialogConfirm.resize(414, 97)
        self.labelQuestion = QtWidgets.QLabel(DialogConfirm)
        self.labelQuestion.setGeometry(QtCore.QRect(30, 20, 470, 13))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelQuestion.sizePolicy().hasHeightForWidth())
        self.labelQuestion.setSizePolicy(sizePolicy)
        self.labelQuestion.setObjectName("labelQuestion")
        self.widget = QtWidgets.QWidget(DialogConfirm)
        self.widget.setGeometry(QtCore.QRect(90, 60, 301, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Yes = QtWidgets.QPushButton(self.widget)
        self.pushButton_Yes.setObjectName("pushButton_Yes")
        self.horizontalLayout.addWidget(self.pushButton_Yes)
        self.pushButton_No = QtWidgets.QPushButton(self.widget)
        self.pushButton_No.setObjectName("pushButton_No")
        self.horizontalLayout.addWidget(self.pushButton_No)
        self. pushButton_Cancel = QtWidgets.QPushButton(self.widget)
        self. pushButton_Cancel.setObjectName(" pushButton_Cancel")
        self.horizontalLayout.addWidget(self. pushButton_Cancel)

        self.retranslateUi(DialogConfirm)
        QtCore.QMetaObject.connectSlotsByName(DialogConfirm)

    def retranslateUi(self, DialogConfirm):
        _translate = QtCore.QCoreApplication.translate
        DialogConfirm.setWindowTitle(_translate("DialogConfirm", self.title))
        self.labelQuestion.setText(_translate("DialogConfirm", self.msg))
        self.pushButton_Yes.setText(_translate("DialogConfirm", "Yes"))
        self.pushButton_No.setText(_translate("DialogConfirm", "No"))
        self. pushButton_Cancel.setText(_translate("DialogConfirm", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogConfirm = QtWidgets.QDialog()
    ui = Ui_DialogConfirm("myMsg", "title")
    ui.setupUi(DialogConfirm)
    DialogConfirm.show()
    sys.exit(app.exec_())
