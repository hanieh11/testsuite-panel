from PySide2 import QtGui,QtWidgets
from dialog_ui import Ui_Dialog
from form import Ui_Form
from loader import Loader
from result import Result

class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.t_form = False
        self.a_form = False
        self.ag_form = False

        self.tests = QtWidgets.QComboBox(self)
        self.ui.formWidgetLayout.insertWidget(1,self.tests)

        self.loader = Loader()
        self.loadTests()

        self.act_lable = QtWidgets.QLabel(self.ui.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.act_lable.setFont(font)
        self.ui.formWidgetLayout.insertWidget(3,self.act_lable)
        self.actions = QtWidgets.QComboBox(self)
        self.ui.formWidgetLayout.insertWidget(4,self.actions)
        self.loadActions()

        self.agg_lable = QtWidgets.QLabel(self.ui.formWidget)
        self.agg_lable.setFont(font)
        self.ui.formWidgetLayout.insertWidget(6,self.agg_lable)
        self.aggregation = QtWidgets.QComboBox(self)
        self.ui.formWidgetLayout.insertWidget(7,self.aggregation)
        self.loadAggregation()

        self.loadKeys()

        self.tests.currentIndexChanged.connect(self.loadTestFile)
        self.actions.currentIndexChanged.connect(self.loadActionFile)
        self.aggregation.currentIndexChanged.connect(self.loadAggFile)

        self.ui.fromDate.dateChanged.connect(self.updateResult)
        self.ui.toDate.dateChanged.connect(self.updateResult)
        self.ui.fromTime.timeChanged.connect(self.updateResult)
        self.ui.toTime.timeChanged.connect(self.updateResult)
        self.ui.statusCheckbox.stateChanged.connect(self.updateResult)
        self.ui.periodSpinBox.valueChanged.connect(self.updateResult)
        self.ui.resultCombo.currentIndexChanged.connect(self.updateResult)

    def loadTests(self):
        for i in self.loader.t_names :
            self.tests.addItem(i)
        self.loadTestFile()

    def loadTestFile(self):
        if self.t_form:
            self.t_form.deleteLater()
        item_list = self.loader.readFile("Test/",self.loader.t_names.get(self.tests.currentText()))
        self.t_form = Ui_Form()
        self.t_form.english = True
        self.t_form.setupUi(item_list)
        self.t_form.flagged.connect(self.updateResult)
        self.ui.formWidgetLayout.insertWidget(2,self.t_form)
        self.updateResult()
    
    def loadActions(self):
        self.actions.addItem("NULL")
        for i in self.loader.a_names :
            self.actions.addItem(i)
        self.loadActionFile()

    def loadActionFile(self):
        if self.a_form :
            self.a_form.deleteLater()
        if self.actions.currentText() != "NULL" :   
            item_list = self.loader.readFile("Action/",self.loader.a_names.get(self.actions.currentText()))
        else:
            item_list = []
        self.a_form = Ui_Form()
        self.a_form.english = True
        self.a_form.setupUi(item_list)
        self.a_form.flagged.connect(self.updateResult)
        self.ui.formWidgetLayout.insertWidget(5,self.a_form)
        self.updateResult()

    def loadAggregation(self):
        self.aggregation.addItem("NULL")
        for i in self.loader.ag_names :
            self.aggregation.addItem(i)
        self.loadAggFile()

    def loadAggFile(self):
        if self.ag_form:
            self.ag_form.deleteLater()
        if self.aggregation.currentText() != "NULL":
            item_list = self.loader.readFile("Aggregation/",self.loader.ag_names.get(self.aggregation.currentText()))
        else:
            item_list = []
        self.ag_form = Ui_Form()
        self.ag_form.english = True
        self.ag_form.setupUi(item_list)
        self.ag_form.flagged.connect(self.updateResult)
        self.ui.formWidgetLayout.insertWidget(8,self.ag_form)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ui.formWidgetLayout.addItem(spacer_item)
        self.updateResult()
    
    def loadKeys(self):
        keys = self.loader.readFile("","keys.json")
        self.ui.resultCombo.addItem("All")
        for i in keys :
            self.ui.resultCombo.addItem(i)
    
    def updateResult(self):
        result = Result(self)
        self.ui.resultLineEdit.setText(result.final_result)