# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui',
# licensing of 'dialog.ui' applies.
#
# Created: Sat Sep 28 20:07:23 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(788, 589)
        Dialog.setStyleSheet("QFrame#periodFrame{ border-style: outset; border-width: 2px; border-color: PaleTurquoise}\n"
"QFrame#scheduleFrame{ border-style: outset; border-width: 2px; border-color: PaleTurquoise}\n"
"QFrame#resultFrame{ border-style: outset; border-width: 2px; border-color: PaleTurquoise}")
        self.dLayout = QtWidgets.QVBoxLayout(Dialog)
        self.dLayout.setObjectName("dLayout")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setMinimumSize(QtCore.QSize(700, 150))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 762, 563))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.statusCheckbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents_2)
        self.statusCheckbox.setEnabled(True)
        self.statusCheckbox.setChecked(True)
        self.statusCheckbox.setObjectName("statusCheckbox")
        self.verticalLayout_3.addWidget(self.statusCheckbox)
        self.ruleLineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_2)
        self.ruleLineEdit.setObjectName("ruleLineEdit")
        self.verticalLayout_3.addWidget(self.ruleLineEdit)
        self.formWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.formWidget.setAutoFillBackground(True)
        self.formWidget.setStyleSheet("")
        self.formWidget.setObjectName("formWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.formWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formWidgetLayout = QtWidgets.QVBoxLayout()
        self.formWidgetLayout.setContentsMargins(10, -1, -1, -1)
        self.formWidgetLayout.setObjectName("formWidgetLayout")
        self.label_4 = QtWidgets.QLabel(self.formWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formWidgetLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.formWidgetLayout)
        self.scheduleWidgetsLayout = QtWidgets.QVBoxLayout()
        self.scheduleWidgetsLayout.setObjectName("scheduleWidgetsLayout")
        self.periodFrame = QtWidgets.QFrame(self.formWidget)
        self.periodFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.periodFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.periodFrame.setObjectName("periodFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.periodFrame)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.periodFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.periodLabel = QtWidgets.QLabel(self.periodFrame)
        self.periodLabel.setObjectName("periodLabel")
        self.horizontalLayout_2.addWidget(self.periodLabel)
        self.periodSpinBox = QtWidgets.QSpinBox(self.periodFrame)
        self.periodSpinBox.setMaximum(999)
        self.periodSpinBox.setProperty("value", 15)
        self.periodSpinBox.setObjectName("periodSpinBox")
        self.horizontalLayout_2.addWidget(self.periodSpinBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scheduleWidgetsLayout.addWidget(self.periodFrame)
        self.scheduleFrame = QtWidgets.QFrame(self.formWidget)
        self.scheduleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scheduleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scheduleFrame.setObjectName("scheduleFrame")
        self.sfLayout = QtWidgets.QVBoxLayout(self.scheduleFrame)
        self.sfLayout.setContentsMargins(10, 10, 10, 10)
        self.sfLayout.setObjectName("sfLayout")
        self.label_2 = QtWidgets.QLabel(self.scheduleFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.sfLayout.addWidget(self.label_2)
        self.dateLayout = QtWidgets.QHBoxLayout()
        self.dateLayout.setObjectName("dateLayout")
        self.fromLable = QtWidgets.QLabel(self.scheduleFrame)
        self.fromLable.setObjectName("fromLable")
        self.dateLayout.addWidget(self.fromLable)
        self.fromDate = QtWidgets.QDateEdit(self.scheduleFrame)
        self.fromDate.setCalendarPopup(True)
        self.fromDate.setObjectName("fromDate")
        self.dateLayout.addWidget(self.fromDate)
        self.toLabel = QtWidgets.QLabel(self.scheduleFrame)
        self.toLabel.setObjectName("toLabel")
        self.dateLayout.addWidget(self.toLabel)
        self.toDate = QtWidgets.QDateEdit(self.scheduleFrame)
        self.toDate.setCalendarPopup(True)
        self.toDate.setObjectName("toDate")
        self.dateLayout.addWidget(self.toDate)
        self.sfLayout.addLayout(self.dateLayout)
        self.timeLayout = QtWidgets.QHBoxLayout()
        self.timeLayout.setObjectName("timeLayout")
        self.fromTLabel = QtWidgets.QLabel(self.scheduleFrame)
        self.fromTLabel.setObjectName("fromTLabel")
        self.timeLayout.addWidget(self.fromTLabel)
        self.fromTime = QtWidgets.QTimeEdit(self.scheduleFrame)
        self.fromTime.setObjectName("fromTime")
        self.timeLayout.addWidget(self.fromTime)
        self.toTLabel = QtWidgets.QLabel(self.scheduleFrame)
        self.toTLabel.setObjectName("toTLabel")
        self.timeLayout.addWidget(self.toTLabel)
        self.toTime = QtWidgets.QTimeEdit(self.scheduleFrame)
        self.toTime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(23, 59, 59)))
        self.toTime.setObjectName("toTime")
        self.timeLayout.addWidget(self.toTime)
        self.sfLayout.addLayout(self.timeLayout)
        self.scheduleWidgetsLayout.addWidget(self.scheduleFrame)
        self.resultFrame = QtWidgets.QFrame(self.formWidget)
        self.resultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.resultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.resultFrame.setObjectName("resultFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.resultFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.resultFrame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.resultCombo = QtWidgets.QComboBox(self.resultFrame)
        self.resultCombo.setObjectName("resultCombo")
        self.verticalLayout.addWidget(self.resultCombo)
        self.resultLineEdit = QtWidgets.QLineEdit(self.resultFrame)
        self.resultLineEdit.setReadOnly(True)
        self.resultLineEdit.setObjectName("resultLineEdit")
        self.verticalLayout.addWidget(self.resultLineEdit)
        self.scheduleWidgetsLayout.addWidget(self.resultFrame)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scheduleWidgetsLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.scheduleWidgetsLayout)
        self.verticalLayout_3.addWidget(self.formWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.dLayout.addWidget(self.scrollArea)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.statusCheckbox.setText(QtWidgets.QApplication.translate("Dialog", "Status", None, -1))
        self.ruleLineEdit.setPlaceholderText(QtWidgets.QApplication.translate("Dialog", "Rule", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "Test", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "Duration", None, -1))
        self.periodLabel.setText(QtWidgets.QApplication.translate("Dialog", "Period(min)", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Dialog", "Schedule", None, -1))
        self.fromLable.setText(QtWidgets.QApplication.translate("Dialog", "From Date:", None, -1))
        self.fromDate.setDisplayFormat(QtWidgets.QApplication.translate("Dialog", "yyyy/MM/dd", None, -1))
        self.toLabel.setText(QtWidgets.QApplication.translate("Dialog", "To Date:", None, -1))
        self.toDate.setDisplayFormat(QtWidgets.QApplication.translate("Dialog", "yyyy/MM/dd", None, -1))
        self.fromTLabel.setText(QtWidgets.QApplication.translate("Dialog", "From Time:", None, -1))
        self.toTLabel.setText(QtWidgets.QApplication.translate("Dialog", "To Time:", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Dialog", "Result", None, -1))

