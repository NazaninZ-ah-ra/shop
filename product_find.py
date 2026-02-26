


from PyQt5 import QtCore, QtGui, QtWidgets
from database import CRUD

class Ui_ProductFind(object):

    def __init__(self):
        self.data = []
        self.db = CRUD()


    def mySignals(self):
        self.pushButton_Search.clicked.connect(self.search)

    def search (self):
        pid = self.lineEdit_Pid.text().strip()
        pname = self.lineEdit_Pname.text().strip()

        font = QtGui.QFont()
        font.setFamily("Poppins")  # Beautiful modern font
        font.setPointSize(11)
        self.label_Msg.setFont(font)

        if not pid and not pname:
            self.label_Msg.setText("⚠️ Please Enter Product Info")

        elif not pid:
            self.label_Msg.setText("⚠️ Please Enter Product ID")
            self.data = []

        elif not pname:
            self.label_Msg.setText("⚠️ Please Enter Product Name")
            self.data = []

        else :
            self.lineEdit_Pid.setText("")
            self.lineEdit_Pname.setText("")

            self.data = self.db.read_products_by_id_name(pid,pname)

            if self.data == []:
                self.label_Msg.setText("❌ Product Not Found")
            else:
                self.label_Msg.setText(f"📦 {len(self.data)} Product(s) Found")
            self.showtable()
                
        self.showtable()



    def showtable(self):
        columns = ["ID","Name","Price"]
        rowCount = len(self.data)

        self.tableWidget_ProductFind.setColumnCount(3)
        self.tableWidget_ProductFind.setRowCount(rowCount)

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
            self.tableWidget_ProductFind.setVerticalHeaderItem(row, item)
      
        for col, col_txt in enumerate(columns):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            item.setText(col_txt)
            self.tableWidget_ProductFind.setHorizontalHeaderItem(col, item)
          
        for row,row_txt in enumerate (self.data):
            for col, col_txt in enumerate (row_txt):
                item = QtWidgets.QTableWidgetItem()
                item.setFont(font)
                item.setText(str(col_txt))
                self.tableWidget_ProductFind.setItem(row, col, item)
            
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 500)
        self.label_Pid = QtWidgets.QLabel(Dialog)
        self.label_Pid.setGeometry(QtCore.QRect(20, 10, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_Pid.setFont(font)
        self.label_Pid.setObjectName("label_Pid")
        self.label_Pname = QtWidgets.QLabel(Dialog)
        self.label_Pname.setGeometry(QtCore.QRect(20, 40, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_Pname.setFont(font)
        self.label_Pname.setObjectName("label_Pname")
        self.lineEdit_Pid = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Pid.setGeometry(QtCore.QRect(230, 10, 213, 25))
        self.lineEdit_Pid.setObjectName("lineEdit_Pid")
        self.lineEdit_Pname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_Pname.setGeometry(QtCore.QRect(230, 40, 213, 25))
        self.lineEdit_Pname.setObjectName("lineEdit_Pname")
        self.pushButton_Search = QtWidgets.QPushButton(Dialog)
        self.pushButton_Search.setGeometry(QtCore.QRect(20, 70, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setObjectName("pushButton_Search")

        # ==================TABLE=========================
        self.tableWidget_ProductFind = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_ProductFind.setGeometry(QtCore.QRect(0, 100, 521, 521))
        self.tableWidget_ProductFind.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_ProductFind.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.showtable()

        self.label_Msg = QtWidgets.QLabel(Dialog)
        self.label_Msg.setGeometry(QtCore.QRect(120, 70, 381, 20))
        self.label_Msg.setObjectName("label_Msg")
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Find_Product"))
        self.label_Pid.setText(_translate("Dialog", "Product ID:"))
        self.label_Pname.setText(_translate("Dialog", "Product Name:"))
        self.pushButton_Search.setText(_translate("Dialog", "Search"))
        __sortingEnabled = self.tableWidget_ProductFind.isSortingEnabled()
        self.tableWidget_ProductFind.setSortingEnabled(False)
        self.tableWidget_ProductFind.setSortingEnabled(__sortingEnabled)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ProductFind()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
