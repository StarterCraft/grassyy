# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uisrc\device.ui'
#
# Created by: PySide6 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_DevicePropertiesDialog(object):
    def setupUi(self, DevicePropertiesDialog):
        DevicePropertiesDialog.setObjectName("DeviceDialog")
        DevicePropertiesDialog.resize(350, 350)
        DevicePropertiesDialog.setMinimumSize(QtCore.QSize(350, 350))
        self.gridLayout = QtWidgets.QGridLayout(DevicePropertiesDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.cbbTempMode = QtWidgets.QComboBox(DevicePropertiesDialog)
        self.cbbTempMode.setObjectName("cbbTempMode")
        self.cbbTempMode.addItem("")
        self.cbbTempMode.addItem("")
        self.gridLayout.addWidget(self.cbbTempMode, 5, 1, 1, 1)
        self.liwPlants = QtWidgets.QListWidget(DevicePropertiesDialog)
        self.liwPlants.setObjectName("liwPlants")
        self.gridLayout.addWidget(self.liwPlants, 8, 0, 1, 2)
        self.label = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAddPlant = QtWidgets.QPushButton(DevicePropertiesDialog)
        self.btnAddPlant.setObjectName("btnAddPlant")
        self.horizontalLayout.addWidget(self.btnAddPlant)
        self.btnRmvPlant = QtWidgets.QPushButton(DevicePropertiesDialog)
        self.btnRmvPlant.setObjectName("btnRmvPlant")
        self.horizontalLayout.addWidget(self.btnRmvPlant)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 1, 1, 1)
        self.lneDeviceName = QtWidgets.QLineEdit(DevicePropertiesDialog)
        self.lneDeviceName.setObjectName("lneDeviceName")
        self.gridLayout.addWidget(self.lneDeviceName, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.cbbPort = QtWidgets.QComboBox(DevicePropertiesDialog)
        self.cbbPort.setObjectName("cbbPort")
        self.gridLayout.addWidget(self.cbbPort, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 2)
        self.pteDeviceDesc = QtWidgets.QPlainTextEdit(DevicePropertiesDialog)
        self.pteDeviceDesc.setObjectName("pteDeviceDesc")
        self.gridLayout.addWidget(self.pteDeviceDesc, 4, 0, 1, 2)
        self.buttonBox = QtWidgets.QDialogButtonBox(DevicePropertiesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 9, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(DevicePropertiesDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.btnStatus = QtWidgets.QPushButton(DevicePropertiesDialog)
        self.btnStatus.setCheckable(True)
        self.btnStatus.setObjectName("btnStatus")
        self.gridLayout.addWidget(self.btnStatus, 2, 1, 1, 1)

        self.retranslateUi(DevicePropertiesDialog)
        self.buttonBox.accepted.connect(DevicePropertiesDialog.accept)
        self.buttonBox.rejected.connect(DevicePropertiesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DevicePropertiesDialog)

    def retranslateUi(self, DeviceDialog):
        _translate = QtCore.QCoreApplication.translate
        DeviceDialog.setWindowTitle(_translate("DeviceDialog", "Устройство"))
        self.cbbTempMode.setItemText(0, _translate("DeviceDialog", "Один на все грядки"))
        self.cbbTempMode.setItemText(1, _translate("DeviceDialog", "По каждому на грядку"))
        self.label.setText(_translate("DeviceDialog", "Имя устройства:"))
        self.btnAddPlant.setText(_translate("DeviceDialog", "Добавить..."))
        self.btnRmvPlant.setText(_translate("DeviceDialog", "Удалить"))
        self.lneDeviceName.setPlaceholderText(_translate("DeviceDialog", "Имя устройства..."))
        self.label_4.setText(_translate("DeviceDialog", "Датчик температуры:"))
        self.label_2.setText(_translate("DeviceDialog", "Порт:"))
        self.label_5.setText(_translate("DeviceDialog", "Грядки:"))
        self.label_3.setText(_translate("DeviceDialog", "Описание (необязательно):"))
        self.pteDeviceDesc.setPlaceholderText(_translate("DeviceDialog", "Описание устройства..."))
        self.label_6.setText(_translate("DeviceDialog", "Статус:"))
        self.btnStatus.setText(_translate("DeviceDialog", "Активно"))
