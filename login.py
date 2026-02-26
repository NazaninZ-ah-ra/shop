from PyQt5 import QtCore, QtGui, QtWidgets
from account import Ui_Account
from database import CRUD

class Ui_login(object):
    def __init__(self):
        self.counter = 0
        self.db = CRUD()

    def mySignals(self):
        self.pushButton_log.clicked.connect( self.login)
        self.pushButton_account.clicked.connect(self.sign_up)

    def sign_up(self,):
        
        Dialog = QtWidgets.QDialog()
    
        ui = Ui_Account()
        ui.setupUi(Dialog)
        Dialog.exec_()
     
        


    def login(self,):
       
        myPass = self.lineEditPassword.text()
        myUser = self.lineEditUserName.text()
        
        user_data = self.db.read_username_pass(uname=myUser,password=myPass)

        
        if myPass == "":
            self.labelMSG.setText("pls Enter ur password")
            self.labelMSG.setVisible(True)
        elif myUser == "":
            self.labelMSG.setText("pls Enter ur username")
            self.labelMSG.setVisible(True)
        else:
            if user_data :
                self.labelMSG.setText("Logged in Sucessfully")
                print("Logged in Sucessfully")
                self.labelMSG.setVisible(True)
                self.dialog.accept()
            else: 
                self.counter += 1
                self.labelMSG.setText("Incorrect Username and Password!retry ...  ")
                self.labelMSG.setVisible(True)
                if self.counter >= 3 :
                    self.dialog.reject()
               

        
            


    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 135)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.pushButton_log = QtWidgets.QPushButton(Dialog)
        self.pushButton_log.setGeometry(QtCore.QRect(40, 100, 160, 33))
        self.pushButton_log.setObjectName("pushButton_log")
        self.pushButton_account = QtWidgets.QPushButton(Dialog)
        self.pushButton_account.setGeometry(QtCore.QRect(220, 100, 190, 33))
        self.pushButton_account.setObjectName("pushButton_account")
        self.lineEditUserName = QtWidgets.QLineEdit(Dialog)
        self.lineEditUserName.setGeometry(QtCore.QRect(140, 20, 201, 20))
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditUserName.setText("nazanin")#-->
        self.lineEditPassword = QtWidgets.QLineEdit(Dialog)
        self.lineEditPassword.setGeometry(QtCore.QRect(140, 50, 201, 20))
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.lineEditPassword.setText("Nn2011@90")#-->
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 20, 100, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
       
        self.label_2.setGeometry(QtCore.QRect(60, 50, 100, 16))
        self.label_2.setObjectName("label_2")
        self.labelMSG = QtWidgets.QLabel(Dialog)
        self.labelMSG.setGeometry(QtCore.QRect(110, 80, 351, 16))
        self.labelMSG.setObjectName("labelMSG")
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.pushButton_log.setText(_translate("Dialog", "Login"))
        self.pushButton_account.setText(_translate("Dialog", "New Account"))
        self.label.setText(_translate("Dialog", "User Name"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.labelMSG.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
