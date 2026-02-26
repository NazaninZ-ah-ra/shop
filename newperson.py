from PyQt5 import QtCore, QtGui, QtWidgets
from fileDialog import FileOpenDialog
import os
class Ui_newPerson(object):

        
    def mySignals(self):
        self.toolButtonOpen.clicked.connect(self.open_pic)
       
 
  
    
    def open_pic(self):
        self.fod = FileOpenDialog()
        myPath= self.fod.openFileNameDialog()
        if myPath:
            
            ext = os.path.splitext(myPath)[1]
            folder = "cpic"
            if not os.path.isdir(folder):
                os.makedirs(folder)
            fpic = os.path.join(folder , f"temp{ext}")
            for file in  os.listdir(folder) :
                if file.startswith("temp") and file != f"temp{ext}":
                    old_path = os.path.join(folder,file)
                    os.rename(old_path,fpic)

            with open (myPath,"rb") as f1 :
                with open(fpic,"wb") as f2 :
                       f2.write(f1.read())

        self.labelPic.setPixmap(QtGui.QPixmap(fpic))
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(368, 207)
        self.labelPic = QtWidgets.QLabel(Dialog)
        self.labelPic.setGeometry(QtCore.QRect(240, 30, 120, 160))
        self.labelPic.setText("")
        # self.labelPic.setPixmap(QtGui.QPixmap("pic/3.jpg"))
        self.labelPic.setScaledContents(True)
        self.labelPic.setObjectName("labelPic")
        self.toolButtonOpen = QtWidgets.QToolButton(Dialog)
        self.toolButtonOpen.setGeometry(QtCore.QRect(330, 170, 25, 19))
        self.toolButtonOpen.setObjectName("toolButtonOpen")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 30, 211, 151))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(self.widget)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)

   

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditMobile = QtWidgets.QLineEdit(self.widget)
        self.lineEditMobile.setObjectName("lineEditMobile")
        self.gridLayout.addWidget(self.lineEditMobile, 1, 1, 1, 1)
        self.pushButtonSave = QtWidgets.QPushButton(self.widget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 2, 1, 1, 1)
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.toolButtonOpen.setText(_translate("Dialog", "..."))
        self.label.setText(_translate("Dialog", "Name :"))
        self.label_2.setText(_translate("Dialog", "Mobile:"))
        self.pushButtonSave.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_newPerson()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
