# Created: Tue Sep  3 18:51:49 2019
#      by: Hanieh running on PySide2 5.13.0
from PySide2 import QtCore,QtWidgets

class Ui_Form(QtWidgets.QWidget):

    flagged = QtCore.Signal(bool)

    def setupUi(self,item_list):
        self.setObjectName("Form")
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.formWidget = QtWidgets.QWidget()
        self.mainLayout.addWidget(self.formWidget)
        self.formWidget.setAutoFillBackground(True)
        self.formWidget.setStyleSheet("QWidget#formWidget{ border-style: outset; border-width: 2px; border-color: PaleTurquoise }")
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName("formLayout")
        self.counter = 0
        self.properties = {}
        self.english = True
        self.item_list = item_list
        self.createForm()
        QtCore.QMetaObject.connectSlotsByName(self)

    def createForm(self):
        if not self.item_list:
            self.formWidget.hide()
        else:
            for i in range(len(self.item_list)):
                typ = str(type(self.item_list[i]["defaultValue"]))
                if typ == "<class 'str'>" :
                    self.strType(i)
                elif typ == "<class 'int'>" :
                    self.intType(i)
                elif typ == "<class 'bool'>" :
                    self.boolType(i)
                elif typ == "<class 'list'>" :
                    self.listType(i)
                else :
                    print("the type of item is not defined!  " + typ)

    def strType(self,index):
        self.LabelCreator(index)
        line = QtWidgets.QLineEdit(self)
        self.properties.update({self.item_list[index]["name"] : line})
        if self.item_list[index]["name"].lower() == "password" :
            line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(self.counter, QtWidgets.QFormLayout.FieldRole, line)
        line.textChanged.connect(self.valueChanged)
        line.setProperty("type", "QLineEdit")
        self.counter = self.counter + 1

    def intType(self,index):
        self.LabelCreator(index)
        spin_box = QtWidgets.QSpinBox(self)
        spin_box.setMaximum(999999999)
        spin_box.setValue(self.item_list[index]["defaultValue"])
        self.properties.update({self.item_list[index]["name"] : spin_box})
        self.formLayout.setWidget(self.counter, QtWidgets.QFormLayout.FieldRole, spin_box)
        spin_box.valueChanged.connect(self.valueChanged)
        spin_box.setProperty("type","QSpinBox")
        self.counter = self.counter + 1

    def boolType(self,index):
        self.LabelCreator(index)
        check_box = QtWidgets.QCheckBox(self)
        self.properties.update({self.item_list[index]["name"] : check_box})
        self.formLayout.setWidget(self.counter, QtWidgets.QFormLayout.FieldRole, check_box)
        check_box.stateChanged.connect(self.valueChanged)
        check_box.setProperty("type", "QCheckBox")
        self.counter = self.counter + 1

    def listType(self,index = None):
        self.LabelCreator(index)
        mylist = QtWidgets.QComboBox(self)
        for i in range(len(self.item_list[index]["defaultValue"])):
            mylist.addItem(self.item_list[index]["defaultValue"][i])
        self.properties.update({self.item_list[index]["name"] : mylist})
        self.formLayout.setWidget(self.counter, QtWidgets.QFormLayout.FieldRole, mylist)
        mylist.currentIndexChanged.connect(self.valueChanged)
        mylist.setProperty("type", "QComboBox")
        self.counter = self.counter + 1

    def LabelCreator (self,index):
        label = QtWidgets.QLabel(self)
        if self.english == True :
            label.setText(self.item_list[index]["translations"]["en"])
        else :
            label.setText(self.item_list[index]["translations"]["fa"]) 
        self.formLayout.setWidget(self.counter, QtWidgets.QFormLayout.LabelRole, label)

    def valueChanged(self):
        self.flagged.emit(True)
