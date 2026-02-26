
from PyQt5 import QtCore, QtGui, QtWidgets
from database import CRUD

class Ui_NewProduct(object):

    def __init__(self):
        self.db = CRUD()

        
    def mySignals(self):
        self.pushButtonAdd.clicked.connect(self.add_products)
        self.spinBoxNo.valueChanged.connect(self.btnactive)
        self.lineEditPname.textChanged.connect(self.btnactive)
        self.pushButtonAdd.setEnabled(False)
    
    def btnactive(self):
        self.pname = self.lineEditPname.text().strip()
        self.price = self.spinBoxNo.text().strip()

        if self.pname and self.price :
            self.pushButtonAdd.setEnabled(True)

        else:
            self.pushButtonAdd.setEnabled(False)

    def add_products(self):
        # self.pname = self.lineEditPname.text().strip()
        # self.price = self.lineEditPrice.text().strip()
        
        print(type(self.price))
        # if self.price

        if self.pname and self.price:
            self.db.new_product(self.pname,self.price)

            self.lineEditPname.clear()
            self.spinBoxNo.setValue(0)

            self.pushButtonAdd.setEnabled(False)

            

    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 252)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_title = QtWidgets.QLabel(Dialog)
        self.label_title.setGeometry(QtCore.QRect(100, 10, 256, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 50, 121, 51))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_price = QtWidgets.QLabel(self.widget)
        self.label_price.setObjectName("label_price")
        self.verticalLayout.addWidget(self.label_price)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(160, 50, 135, 51))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEditPname = QtWidgets.QLineEdit(self.widget1)
        self.lineEditPname.setObjectName("lineEditPname")
        

        # spinBox
        # self.spinBoxNo = QtWidgets.QSpinBox(self.widget1)
        # self.spinBoxNo.setMinimumSize(QtCore.QSize(100, 90))
        # self.spinBoxNo.setObjectName("spinBoxNo")
       




        # self.lineEditPrice = QtWidgets.QLineEdit(self.widget1)
        # self.lineEditPrice.setObjectName("lineEditPrice")

        self.verticalLayout_2.addWidget(self.lineEditPname)
        self.spinBoxNo = QtWidgets.QSpinBox(self.widget1)
        self.spinBoxNo.setObjectName("spinBoxNo")
        self.verticalLayout_2.addWidget(self.spinBoxNo)


        self.widget2 = QtWidgets.QWidget(Dialog)
        self.widget2.setGeometry(QtCore.QRect(40, 130, 261, 25))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonAdd = QtWidgets.QPushButton(self.widget2)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        # self.pushButtonAdd.setEnabled(False)
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonDone = QtWidgets.QPushButton(self.widget2)
        self.pushButtonDone.setObjectName("pushButtonDone")
        self.horizontalLayout.addWidget(self.pushButtonDone)
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_title.setText(_translate("Dialog", "ADD YOUR PRODUCT"))
        self.label.setText(_translate("Dialog", "Name:"))
        self.label_price.setText(_translate("Dialog", "Price:"))
        self.pushButtonAdd.setText(_translate("Dialog", "ADD"))
        self.pushButtonDone.setText(_translate("Dialog", "Done"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_NewProduct()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
