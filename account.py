

from PyQt5 import QtCore, QtGui, QtWidgets
from database import CRUD


class Ui_Account(object):

    def __init__(self):
        self.db = CRUD()

    def mySignals (self):
        self.pushButton_submit.clicked.connect(self.submit)

    def pass_verify(self,password):
        from string import ascii_uppercase as au, ascii_lowercase as al, digits as d

        special = "#[]{_-*@<>$} "

        u = any([ch in au for ch in password])
        if not u :
            return False , "Password needs Uppercase letter !"
        
        l = any([ch in al for ch in password])
        if not l :
            return False , "Password needs Lowercase letter !"
        
        s = any([ch in special for ch in password])
        if not s:
            return False , "Password needs --> #[]{_-*@<>$} <--"
        
        n = any([ch in d for ch in password])
        if not n :
            return False , "Password needs a Digit"
        
        length = len(password)
        if length < 8 or length > 12:
            return False , "Password needs to have 8-12 Digits"

        return all([l,u,n,s]),"Accepted "

            
    def submit(self):
        password = self.lineEdit_pass.text().strip()
        uname = self.lineEdit_name.text().strip()
        n_data = self.db.read_username(uname=uname)



        if not n_data :

            if not uname or not password :
                self.label_msg.setText("Username and password required")
                return
     
            else:
                result,msg = self.pass_verify(password=password)
                if result == False:
                    self.label_msg.setText(msg)

                else:
                    try:
                        self.db.add_user_data(password=password,uname=uname)
                        self.dialog.accept()
                        
                    except Exception as e:
                        self.label_msg.setText(f"Database error {e} ")   
                        

                   

        else:

                self.label_msg.setText("This username already exists!!! ")

            



    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)

    

        # Message label
        self.label_msg = QtWidgets.QLabel(Dialog)
        self.label_msg.setGeometry(QtCore.QRect(40, 80, 420, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_msg.setFont(font)
        self.label_msg.setObjectName("label_msg")

        # Submit button
        self.pushButton_submit = QtWidgets.QPushButton(Dialog)
        self.pushButton_submit.setGeometry(QtCore.QRect(40, 260, 140, 50))
        font = QtGui.QFont()
        font.setFamily("Mj_Susan")
        font.setPointSize(14)
        self.pushButton_submit.setFont(font)
        self.pushButton_submit.setObjectName("pushButton_submit")

        # Input area
        self.splitter_3 = QtWidgets.QSplitter(Dialog)
        self.splitter_3.setGeometry(QtCore.QRect(40, 130, 420, 110))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")

        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.label_name = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Mj_Susan")
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")

        self.lineEdit_name = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_name.setMinimumHeight(20)
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")

        self.label_pass = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Mj_Susan")
        font.setPointSize(15)
        self.label_pass.setFont(font)
        self.label_pass.setObjectName("label_pass")

        self.lineEdit_pass = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_pass.setMinimumHeight(20)
        self.lineEdit_pass.setObjectName("lineEdit_pass")

        # Title
        self.splitter_4 = QtWidgets.QSplitter(Dialog)
        self.splitter_4.setGeometry(QtCore.QRect(100, 20, 300, 60))
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")

        self.label_title_1 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("IranNastaliq")
        font.setPointSize(13)
        self.label_title_1.setFont(font)
        self.label_title_1.setObjectName("label_title_1")

        self.label_title_2 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setFamily("IranNastaliq")
        font.setPointSize(13)
        self.label_title_2.setFont(font)
        self.label_title_2.setObjectName("label_title_2")
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign up "))
        self.pushButton_submit.setText(_translate("Dialog", "Submit"))
        self.label_name.setText(_translate("Dialog", "Username"))
        self.label_pass.setText(_translate("Dialog", "Password"))
        self.label_title_1.setText(_translate("Dialog", "CREATE"))
        self.label_title_2.setText(_translate("Dialog", "ACCOUNT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Account()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
