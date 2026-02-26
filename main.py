
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from newperson import Ui_newPerson
from Confirm import Ui_DialogConfirm
from login import Ui_login
from database import CRUD
from newproduct import Ui_NewProduct
from open import Ui_Open
import jdatetime 
from product_find import Ui_ProductFind
from find_person import Ui_Find_Person
from account import Ui_Account


class Ui_MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        self.costumername = " "
        self.db = CRUD()
        self.factor =[]
        self.products = [{'id': i, 'Name': n, 'Fee': f} for i, n, f in self.db.read_all_products()]
        self.products.insert(0,{"Name" : "Select one" , "Fee" : "0" , "id": 1 })
        self.costumer_id = -1
        self.factor_id = -1

    def show_combobox(self):
        self.comboBoxTName = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBoxTName.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxTName.setObjectName("comboBoxTName")
        for item in self.products:
           self.comboBoxTName.addItem(item["Name"])
        

    def mySignals(self):
        self.pushButtonAdd.clicked.connect(self.add)
        self.comboBoxTName.currentIndexChanged.connect(self.btnAddActive)
        self.spinBoxNo.valueChanged.connect(self.btnAddActive)
        self.pushbottunSave.clicked.connect(self.save)
        self.actionClose.triggered.connect(self.close)
        self.actionnew_Person.triggered.connect(self.newp_Create)
        self.actionfind_Person.triggered.connect(self.find_person)
        self.actionNew.triggered.connect(self.newFactor)
        self.actionOpen.triggered.connect(self.openFactor)
        self.tableWidget.clicked.connect(self.AddorDeL)
        self.actionProduct_NewProduct.triggered.connect(self.new_product)
        self.actionProduct_FindProduct.triggered.connect(self.find_product)

        
    def openFactor(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Open()
        ui.setupUi(Dialog)
        
        if Dialog.exec_():
            self.factor_id = ui.lineEditFid.text()
            self.factor.clear()
            self.setWindowTitle(f"factor_id : {self.factor_id}")
            data = self.db.read_factor_details(self.factor_id)
            print(data)
            self.factor = [
                {"id" : d[0],"Name":d[1],"Fee":d[2],"No":d[3],"Sum":d[4]}
                for d in data
            ]
            self.show_table()
    
    def find_person(self,):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Find_Person()
        ui.setupUi(Dialog)
        Dialog.exec()

    def find_product(self,):
        Dialog = QtWidgets.QDialog()
        ui = Ui_ProductFind()
        ui.setupUi(Dialog)
        Dialog.exec()

    def new_product(self,):
        Dialog = QtWidgets.QDialog()
        uiForm = Ui_NewProduct()
        uiForm.setupUi(Dialog)
        uiForm.pushButtonDone.clicked.connect(lambda : self.done(Dialog))
        Dialog.exec()

    def done(self,Dialog):
        self.products.clear()
        self.products = [{'id': i, 'Name': n, 'Fee': f} for i, n, f in self.db.read_all_products()]

        self.comboBoxTName.clear()
        for p in self.products:
            self.comboBoxTName.addItem(p["Name"])
        Dialog.close()
        
    def newp_Create ( self ) : 
        Dialog = QtWidgets.QDialog()
        uiForm = Ui_newPerson()
        uiForm.setupUi(Dialog)
        uiForm.pushButtonSave.clicked.connect(lambda : self.myNewperson(uiForm,Dialog))
        
        Dialog.exec()

    def myNewperson( self,ui , di ):
        cname = ui.lineEditName.text()
        if cname :
            self.costumer_id = self.db.add_new_costumer(cname) # we put it here so that we can save it 
            self.lineEditCustomerName.setText(cname)
            self.setWindowTitle(f'Costumer : {cname} id = {self.costumer_id}')
            di.close()




    def newFactor(self):
        if self.pushbottunSave.isEnabled():
            DialogConfirm = QtWidgets.QDialog()
            ui = Ui_DialogConfirm("DO you want to Save ?" , "WARNING")
            ui.setupUi(DialogConfirm)


            def on_yes ():
                self.save()
                self.factor.clear()
                DialogConfirm.accept()
                self.show_table()
                
            def on_no() :
                self.factor.clear()
                DialogConfirm.accept()
                self.show_table()
            
            def on_cancel() :
                DialogConfirm.reject()
                self.show_table()
    
            ui.pushButton_Yes.clicked.connect(on_yes)
            ui.pushButton_No.clicked.connect(on_no)
            ui.pushButton_Cancel.clicked.connect(on_cancel)
            DialogConfirm.exec()

                
        else:
            self.factor.clear()
            self.show_table()

    def AddorDeL(self):
        row = self.tableWidget.currentRow()
        col = self.tableWidget.currentColumn()
        if col == 4 :
            self.factor[row]["No"] += 1 
            self.factor[row]["Sum"] += self.factor[row]["No"] * self.factor[row]["Fee"]
        elif col == 5 :
             self.factor[row]["No"] -= 1 
             self.factor[row]["Sum"] = self.factor[row]["No"] * self.factor[row]["Fee"]
             if self.factor[row]["No"] == 0 :
                 self.factor.pop(row)
        self.pushbottunSave.setEnabled(True)
        self.show_table()


    def save (self):
        self.pushbottunSave.setEnabled(False)
        
        mydate = jdatetime.datetime.now().strftime("%Y/%m/%d")
        if self.factor_id== -1: #NewFACTOR 
            self.factor_id = self.db.add_new_factor(
                cid = self.costumer_id,
                date = mydate,
                total = self.lineEditTotal.text(),
            )
            self.setWindowTitle(f"factor_id : {self.factor_id}")
        else:
            self.db.update_factor(factor_id=self.factor_id,total=self.lineEditTotal.text())
            self.db.del_factor_details(factor_id = self.factor_id )
        
        details = [(self.factor_id, d['id'], d['Fee'], d['No'], d["Sum"]) for d in self.factor]
        self.db.add_factor_details(data_list = details )
        self.pushbottunSave.setEnabled(False)

    def  btnAddActive(self):
        index = self.comboBoxTName.currentIndex()
        no = self.spinBoxNo.value()
        self.pushButtonAdd.setEnabled(index and no  )
  

    def add(self):
        newRow = {}    
        index = self.comboBoxTName.currentIndex()
        newRow['id'] =  self.products[index]['id']
        newRow['Name'] = self.products[index]['Name']
        newRow['Fee'] = self.products[index]['Fee']
        newRow['No'] = int(self.spinBoxNo.text())
        newRow['Sum'] =  newRow['Fee'] * newRow['No']
        for index , item in enumerate(self.factor):
            if item['id'] == newRow['id']:
                self.factor[index]['No'] += newRow['No'] 
                self.factor[index]['Sum'] += newRow['Sum'] 
                break
        else:    
            self.factor.append(newRow)
        
        
        self.pushbottunSave.setEnabled(True)
        self.show_table()
        self.comboBoxTName.setCurrentIndex(0)
        self.spinBoxNo.setValue(0)
        
       
    def show_table(self):
        columns = ["Name","No","Fee","Sum","Add","Delete"]
        
        rowCount = len(self.factor)
    
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(rowCount)
 
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        for row in range (rowCount):
            item = QtWidgets.QTableWidgetItem()
            item.setText(str(row+1))
            item.setFont(font)
            self.tableWidget.setVerticalHeaderItem(row, item)
        
        for col , txt in enumerate (columns):
            item = QtWidgets.QTableWidgetItem()
            item.setText(txt)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(col, item)

        for row in range ( rowCount):
            for col in range (4):
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(self.factor[row][columns[col]]))
                item.setFont(font)
                item.setFlags(QtCore.Qt.NoItemFlags)
                self.tableWidget.setItem(row, col, item)
               
 
        AddIcon = QtGui.QIcon()
        AddIcon.addPixmap(QtGui.QPixmap("pic/Edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for row in range( rowCount):
            item = QtWidgets.QTableWidgetItem()
            item.setIcon(AddIcon)
            item.setText("Add")
            item.setFont(font)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row, 4, item)

        DelIcon = QtGui.QIcon()
        DelIcon.addPixmap(QtGui.QPixmap("pic/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        for row in range (rowCount):
            item = QtWidgets.QTableWidgetItem()
            item.setIcon(DelIcon)
            item.setText("Delete")
            item.setFont(font)
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row, 5, item)
        sum = 0 
        for data in self.factor : 
            sum += data["Sum"]
        self.lineEditTotal.setText(str(sum))      
                

    def setupUi(self,):
        self.setObjectName("self")
        self.setEnabled(True)
        self.resize(800, 600)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 30, 741, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEditCustomerName = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEditCustomerName.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEditCustomerName.setObjectName("lineEditCustomerName")
        self.horizontalLayout.addWidget(self.lineEditCustomerName)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 741, 91))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 21, 681, 56))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        # show combobox
        self.show_combobox()
  
        self.horizontalLayout_2.addWidget(self.comboBoxTName)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        # spinbox
        self.spinBoxNo = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBoxNo.setMinimumSize(QtCore.QSize(100, 0))
        self.spinBoxNo.setObjectName("spinBoxNo")
        self.horizontalLayout_2.addWidget(self.spinBoxNo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        # pushbottun Add
        self.pushButtonAdd = QtWidgets.QPushButton(self.layoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pic/Filter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAdd.setIcon(icon1)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.pushButtonAdd.setEnabled(False)
        self.verticalLayout.addWidget(self.pushButtonAdd)
        # Table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 180, 741, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.lineEditTotal = QtWidgets.QLineEdit(self)
        self.lineEditTotal.setText("0")
        self.lineEditTotal.move(50,520,)
        self.show_table()
       

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.pushbottunSave = QtWidgets.QPushButton(self.centralwidget)
        self.pushbottunSave.setGeometry(QtCore.QRect(630, 490, 161, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("pic/Save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushbottunSave.setIcon(icon4)
        self.pushbottunSave.setIconSize(QtCore.QSize(20, 20))
        self.pushbottunSave.setCheckable(True)
        self.pushbottunSave.setChecked(True)
        self.pushbottunSave.setObjectName("pushbottunSave")
        self.pushbottunSave.setEnabled(False)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menucustomer = QtWidgets.QMenu(self.menubar)
        self.menucustomer.setObjectName("menucustomer")
        self.menunew = QtWidgets.QMenu(self.menucustomer)
        self.menunew.setObjectName("menunew")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(self)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionnew_Person = QtWidgets.QAction(self)
        self.actionnew_Person.setObjectName("actionnew_Person")
        self.actionfind_Person = QtWidgets.QAction(self)
        self.actionfind_Person.setObjectName("actionfind_Person")
        self.actionImport_from_file = QtWidgets.QAction(self)
        self.actionImport_from_file.setObjectName("actionImport_from_file")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menunew.addAction(self.actionnew_Person)
        self.menunew.addAction(self.actionfind_Person)
        self.menunew.addAction(self.actionImport_from_file)
        self.menucustomer.addAction(self.menunew.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menucustomer.menuAction())
        self.menuProduct = QtWidgets.QMenu(self.menubar)
        self.menuProduct.setObjectName("menuProduct")
        self.menuProduct.setTitle("Product")
        self.actionProduct_NewProduct = QtWidgets.QAction(self)
        self.actionProduct_NewProduct.setObjectName("actionProduct_NewProduct")
        self.actionProduct_NewProduct.setText("New Product")
        self.actionProduct_FindProduct = QtWidgets.QAction(self)
        self.actionProduct_FindProduct.setObjectName("actionProduct_FindProduct")
        self.actionProduct_FindProduct.setText("Find Product")
        self.menuProduct.addAction(self.actionProduct_NewProduct)
        self.menuProduct.addAction(self.actionProduct_FindProduct)
        self.menubar.addAction(self.menuProduct.menuAction())

        self.mySignals()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, ):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "ShopMangement By Naxi-"))
        self.label.setText(_translate("self", "Customer Name:"))
        self.groupBox.setTitle(_translate("self", "Tools"))
        self.label_2.setText(_translate("self", "name:"))
        # combo box
   
        self.pushButtonAdd.setText(_translate("self", "Add"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        # ----------------------------------------------------
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushbottunSave.setText(_translate("self", "Save"))
        self.menuFile.setTitle(_translate("self", "File"))
        self.menucustomer.setTitle(_translate("self", "customer"))
        self.menunew.setTitle(_translate("self", "new"))
        self.actionNew.setText(_translate("self", "New"))
        self.actionOpen.setText(_translate("self", "Open..."))
        self.actionClose.setText(_translate("self", "Close"))
        self.actionnew_Person.setText(_translate("self", "New Person"))
        self.actionfind_Person.setText(_translate("self", "Find Person"))
        self.actionImport_from_file.setText(_translate("self", "Import from file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui_login = Ui_login()
    ui_login.setupUi(Dialog)

    result = Dialog.exec()
    
    if result == 1 :
        ui = Ui_MainWindow()
        ui.setupUi()
        ui.show()
        sys.exit(app.exec_())
    else:
        pass

