from PyQt5 import QtCore, QtGui, QtWidgets
from database import CRUD

class Ui_Open(object):

    def __init__(self):
        self.db = CRUD()
        self.data = []
    
    def mySignals(self):
        self.pushButtonSearch.clicked.connect(self.search)
        self.tableWidget.cellClicked.connect(self.Ok)

    def Ok (self,):
        col = self.tableWidget.currentColumn()
        if col == 5:
            print("5")
            self.dialog.accept()

    def search(self,):
        fid = self.lineEditFid.text().strip()
        cname = self.lineEditCostumer.text().strip()

        self.data = self.db.read_factor(fid,cname)
        if not self.data:
            self.labelMSG.setText("Not Found")

        else:
            self.labelMSG.setText(f"{len(self.data)} Result Found")

        self.show_table()

    def show_table(self,):
        columns = ["ID","Name","Fid","Date","Total","OK"]
        rowCount = len(self.data)

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(rowCount)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        for row in range (rowCount):
             item = QtWidgets.QTableWidgetItem()
             item.setFont(font)
             item.setText(str(row + 1))
             self.tableWidget.setVerticalHeaderItem(row, item)
            
        for col,txt in enumerate (columns) :
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            item.setText(txt)
            
            self.tableWidget.setHorizontalHeaderItem(col, item)

        for r_index, r_data in enumerate(self.data):
            for col_index, col_data in enumerate (r_data):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(col_data))
                self.tableWidget.setItem(r_index,col_index,item)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/1f197.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for row in range (rowCount):
            item = QtWidgets.QTableWidgetItem("OK")
            item.setIcon(icon)
            item.setText("OK")
            item.setFont(font)
            self.tableWidget.setItem(row, 5, item)
        
    
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        for row in range (self.tableWidget.rowCount()):
            item = self.tableWidget.item(row,5)
            if not item:
                item = QtWidgets.QTableWidgetItem("OK")
                self.tableWidget.setItem(row,5,item)
            item.setFlags(QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsSelectable)

    
    def setupUi(self, Dialog):
        self.dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 317)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Dialog.setFont(font)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 110, 611, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.show_table()
        self.pushButtonSearch = QtWidgets.QPushButton(Dialog)
        self.pushButtonSearch.setGeometry(QtCore.QRect(230, 50, 150, 23))
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 591, 28))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Costumer = QtWidgets.QLabel(self.layoutWidget)
        self.label_Costumer.setObjectName("label_Costumer")
        self.horizontalLayout.addWidget(self.label_Costumer)
        self.lineEditCostumer = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditCostumer.setObjectName("lineEditCostumer")
        self.horizontalLayout.addWidget(self.lineEditCostumer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelFid = QtWidgets.QLabel(self.layoutWidget)
        self.labelFid.setObjectName("labelFid")
        self.horizontalLayout.addWidget(self.labelFid)
        self.lineEditFid = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditFid.setObjectName("lineEditFid")
        self.horizontalLayout.addWidget(self.lineEditFid)
        self.labelMSG = QtWidgets.QLabel(Dialog)
        self.labelMSG.setGeometry(QtCore.QRect(230, 80, 161, 20))
        self.labelMSG.setObjectName("labelMSG")
        self.labelMSG.setText("")


        #=============================================
        # HERE IT IS 

        self.lineEditCostumer.setText("fatima")
        self.lineEditFid.setText("7")
        self.mySignals()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Factor_Search", "Factor_search"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
       
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButtonSearch.setText(_translate("Dialog", "Search"))
        self.label_Costumer.setText(_translate("Dialog", "Costumer:"))
        self.labelFid.setText(_translate("Dialog", "factor ID:"))
        self.labelMSG.setText(_translate("Dialog", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Open()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
