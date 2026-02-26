from PyQt5 import QtCore, QtGui, QtWidgets
from database import CRUD

class Ui_Find_Person(object):
        
    def __init__(self):
        self.db = CRUD()
        self.data = []
    
    def mySignals(self):
        self.pushButton_Search.clicked.connect(self.search)

    def search(self):
        cname = self.lineEdit_Name_3.text().strip()
        cid = self.lineEdit_Id_3.text().strip()
        
        font = QtGui.QFont()
        font.setFamily("Poppins")  # Beautiful modern font
        font.setPointSize(11)
        self.label_Msg.setFont(font)

        if not cid and not cname:
            self.label_Msg.setText("⚠️ Please Enter Costumer Info")

        elif not cid:
            self.label_Msg.setText("⚠️ Please Enter Costumer ID")

        elif not cname:
            self.label_Msg.setText("⚠️ Please Enter Costumer Name")

        else :
            self.lineEdit_Id_3.setText("")
            self.lineEdit_Name_3.setText("")

            self.data = self.db.read_costumer_by_id_name(cid,cname)
            
            if self.data == []:
                self.label_Msg.setText("❌ Costumer Not Found")
            else:
                self.label_Msg.setText(f"👥 {len(self.data)} Costumer(s) Found")
        self.showtable()

    def showtable(self):
        columns = ["ID","Name","Factor ID","Product ID"]
        rowCount = len(self.data)

        self.tableWidget_PersonFind.setColumnCount(4)
        self.tableWidget_PersonFind.setRowCount(rowCount)

        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)

        for row in range (rowCount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            item.setText(str(row+1))
            self.tableWidget_PersonFind.setVerticalHeaderItem(row, item)
        
        for col , col_txt in enumerate (columns):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            item.setText(str(col_txt))
            self.tableWidget_PersonFind.setHorizontalHeaderItem(col, item)

        for row, row_txt in enumerate(self.data):
            for col, col_txt in enumerate (row_txt):
                item = QtWidgets.QTableWidgetItem()
                item.setFont(font)
                item.setText(str(col_txt))
                self.tableWidget_PersonFind.setItem(row, col, item)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(423, 289)
        self.label_Msg = QtWidgets.QLabel(Dialog)
        self.label_Msg.setGeometry(QtCore.QRect(110, 80, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_Msg.setFont(font)
        self.label_Msg.setObjectName("label_Msg")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 10, 171, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_Name_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Name_3.setFont(font)
        self.label_Name_3.setObjectName("label_Name_3")
        self.horizontalLayout_5.addWidget(self.label_Name_3)
        self.lineEdit_Name_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_Name_3.setObjectName("lineEdit_Name_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_Name_3)
        self.tableWidget_PersonFind = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_PersonFind.setGeometry(QtCore.QRect(0, 100, 421, 192))
        self.tableWidget_PersonFind.setObjectName("tableWidget_PersonFind")
        self.tableWidget_PersonFind.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_PersonFind.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.showtable()
        self.pushButton_Search = QtWidgets.QPushButton(Dialog)
        self.pushButton_Search.setGeometry(QtCore.QRect(150, 50, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 10, 156, 22))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_Id_3 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_Id_3.setFont(font)
        self.label_Id_3.setObjectName("label_Id_3")
        self.horizontalLayout_6.addWidget(self.label_Id_3)
        self.lineEdit_Id_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_Id_3.setObjectName("lineEdit_Id_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_Id_3)
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Find_Person"))
        self.label_Name_3.setText(_translate("Dialog", "Name:"))
        __sortingEnabled = self.tableWidget_PersonFind.isSortingEnabled()
        self.tableWidget_PersonFind.setSortingEnabled(False)
        self.tableWidget_PersonFind.setSortingEnabled(__sortingEnabled)
        self.pushButton_Search.setText(_translate("Dialog", "Search"))
        self.label_Id_3.setText(_translate("Dialog", "ID:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Find_Person()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
