# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Work\Code\greenyy\uisrc\window\log.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogWindow(object):
    def setupUi(self, LogWindow):
        LogWindow.setObjectName("LogWindow")
        LogWindow.resize(600, 400)
        LogWindow.setMinimumSize(QtCore.QSize(600, 400))
        LogWindow.setStyleSheet("QTextEdit, QLineEdit, QComboBox, QPushButton {\n"
"    font-family: \"Cascadia Code\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(LogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 7, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txtLogDisplay = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.txtLogDisplay.setFont(font)
        self.txtLogDisplay.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.txtLogDisplay.setReadOnly(True)
        self.txtLogDisplay.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.txtLogDisplay.setObjectName("txtLogDisplay")
        self.verticalLayout.addWidget(self.txtLogDisplay)
        self.frmSend = QtWidgets.QFrame(self.centralwidget)
        self.frmSend.setObjectName("frmSend")
        self.sendPanel = QtWidgets.QHBoxLayout(self.frmSend)
        self.sendPanel.setContentsMargins(7, 0, 7, 0)
        self.sendPanel.setObjectName("sendPanel")
        self.cbbPort = QtWidgets.QComboBox(self.frmSend)
        self.cbbPort.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbbPort.setObjectName("cbbPort")
        self.sendPanel.addWidget(self.cbbPort)
        self.lneMessage = QtWidgets.QLineEdit(self.frmSend)
        self.lneMessage.setObjectName("lneMessage")
        self.sendPanel.addWidget(self.lneMessage)
        self.cbbSendMode = QtWidgets.QComboBox(self.frmSend)
        self.cbbSendMode.setMaximumSize(QtCore.QSize(75, 16777215))
        self.cbbSendMode.setObjectName("cbbSendMode")
        self.sendPanel.addWidget(self.cbbSendMode)
        self.btnSend = QtWidgets.QPushButton(self.frmSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSend.setObjectName("btnSend")
        self.sendPanel.addWidget(self.btnSend)
        self.verticalLayout.addWidget(self.frmSend)
        LogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.meiSettings = QtWidgets.QMenu(self.menuWindow)
        self.meiSettings.setObjectName("meiSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        LogWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogWindow)
        self.statusbar.setStyleSheet("font-size: 8pt;")
        self.statusbar.setObjectName("statusbar")
        LogWindow.setStatusBar(self.statusbar)
        self.meiLogLvlDEBUG = QtWidgets.QAction(LogWindow)
        self.meiLogLvlDEBUG.setObjectName("meiLogLvlDEBUG")
        self.meiLogLvlINFO = QtWidgets.QAction(LogWindow)
        self.meiLogLvlINFO.setObjectName("meiLogLvlINFO")
        self.meiLogLvlWARNING = QtWidgets.QAction(LogWindow)
        self.meiLogLvlWARNING.setObjectName("meiLogLvlWARNING")
        self.meiLogLvlERROR = QtWidgets.QAction(LogWindow)
        self.meiLogLvlERROR.setObjectName("meiLogLvlERROR")
        self.meiLogLvlCRITICAL = QtWidgets.QAction(LogWindow)
        self.meiLogLvlCRITICAL.setObjectName("meiLogLvlCRITICAL")
        self.meiExit = QtWidgets.QAction(LogWindow)
        self.meiExit.setObjectName("meiExit")
        self.meiLogFolder = QtWidgets.QAction(LogWindow)
        self.meiLogFolder.setObjectName("meiLogFolder")
        self.meiScroll = QtWidgets.QAction(LogWindow)
        self.meiScroll.setObjectName("meiScroll")
        self.meiIncreaseFontSize = QtWidgets.QAction(LogWindow)
        self.meiIncreaseFontSize.setObjectName("meiIncreaseFontSize")
        self.meiReduceFontSize = QtWidgets.QAction(LogWindow)
        self.meiReduceFontSize.setObjectName("meiReduceFontSize")
        self.meiASCII = QtWidgets.QAction(LogWindow)
        self.meiASCII.setObjectName("meiASCII")
        self.meiLogSource = QtWidgets.QAction(LogWindow)
        self.meiLogSource.setObjectName("meiLogSource")
        self.meiDevices = QtWidgets.QAction(LogWindow)
        self.meiDevices.setObjectName("meiDevices")
        self.meiRules = QtWidgets.QAction(LogWindow)
        self.meiRules.setObjectName("meiRules")
        self.meiKeys = QtWidgets.QAction(LogWindow)
        self.meiKeys.setObjectName("meiKeys")
        self.meiLog = QtWidgets.QAction(LogWindow)
        self.meiLog.setCheckable(True)
        self.meiLog.setObjectName("meiLog")
        self.meiGeneral = QtWidgets.QAction(LogWindow)
        self.meiGeneral.setCheckable(True)
        self.meiGeneral.setObjectName("meiGeneral")
        self.meiEnvironment = QtWidgets.QAction(LogWindow)
        self.meiEnvironment.setObjectName("meiEnvironment")
        self.menuFile.addAction(self.meiLogFolder)
        self.menuFile.addSeparator()
        self.meiSettings.addAction(self.meiDevices)
        self.meiSettings.addAction(self.meiRules)
        self.meiSettings.addAction(self.meiKeys)
        self.meiSettings.addAction(self.meiEnvironment)
        self.menuWindow.addAction(self.meiGeneral)
        self.menuWindow.addAction(self.meiLog)
        self.menuWindow.addAction(self.meiSettings.menuAction())
        self.menuWindow.addSeparator()
        self.menuView.addAction(self.meiScroll)
        self.menuView.addSeparator()
        self.menuView.addAction(self.meiIncreaseFontSize)
        self.menuView.addAction(self.meiReduceFontSize)
        self.menuView.addSeparator()
        self.menuView.addAction(self.meiASCII)
        self.menuView.addAction(self.meiLogSource)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(LogWindow)
        self.meiExit.triggered.connect(LogWindow.close)
        QtCore.QMetaObject.connectSlotsByName(LogWindow)
        LogWindow.setTabOrder(self.cbbPort, self.lneMessage)
        LogWindow.setTabOrder(self.lneMessage, self.txtLogDisplay)

    def retranslateUi(self, LogWindow):
        _translate = QtCore.QCoreApplication.translate
        LogWindow.setWindowTitle(_translate("LogWindow", "Журнал и последовательный порт"))
        self.cbbPort.setPlaceholderText(_translate("LogWindow", "Порт"))
        self.lneMessage.setPlaceholderText(_translate("LogWindow", "Отправить сообщение на COM-порт..."))
        self.btnSend.setText(_translate("LogWindow", "=>"))
        self.menuFile.setTitle(_translate("LogWindow", "Файл"))
        self.menuWindow.setTitle(_translate("LogWindow", "Окно"))
        self.meiSettings.setTitle(_translate("LogWindow", "Настройки"))
        self.menuView.setTitle(_translate("LogWindow", "Вид"))
        self.meiLogLvlDEBUG.setText(_translate("LogWindow", "Отладка (DEBUG)"))
        self.meiLogLvlDEBUG.setToolTip(_translate("LogWindow", "Уровень журналирования: Отладка (DEBUG)"))
        self.meiLogLvlINFO.setText(_translate("LogWindow", "Информирование (INFO)"))
        self.meiLogLvlINFO.setToolTip(_translate("LogWindow", "Уровень журналирования: Информирование (INFO)"))
        self.meiLogLvlWARNING.setText(_translate("LogWindow", "Предупреждение (WARNING)"))
        self.meiLogLvlWARNING.setToolTip(_translate("LogWindow", "Уровень журналирования: Предупреждение (WARNING)"))
        self.meiLogLvlERROR.setText(_translate("LogWindow", "Ошибки (ERROR)"))
        self.meiLogLvlERROR.setToolTip(_translate("LogWindow", "Уровень журналирования: Ошибки (ERROR)"))
        self.meiLogLvlCRITICAL.setText(_translate("LogWindow", "Критические ошибки (CRITICAL)"))
        self.meiLogLvlCRITICAL.setToolTip(_translate("LogWindow", "Уровень журналирования: Критические ошибки (CRITICAL)"))
        self.meiExit.setText(_translate("LogWindow", "Выход"))
        self.meiLogFolder.setText(_translate("LogWindow", "Открыть папку с журналом"))
        self.meiScroll.setText(_translate("LogWindow", "Автопрокрутка"))
        self.meiIncreaseFontSize.setText(_translate("LogWindow", "Увеличить кегль"))
        self.meiReduceFontSize.setText(_translate("LogWindow", "Уменьшить кегль"))
        self.meiASCII.setText(_translate("LogWindow", "Декодирование в ASCII..."))
        self.meiLogSource.setText(_translate("LogWindow", "Источники журнала..."))
        self.meiDevices.setText(_translate("LogWindow", "Устройства..."))
        self.meiRules.setText(_translate("LogWindow", "Правила..."))
        self.meiKeys.setText(_translate("LogWindow", "Клавиши..."))
        self.meiLog.setText(_translate("LogWindow", "Журнал"))
        self.meiGeneral.setText(_translate("LogWindow", "Основное окно"))
        self.meiEnvironment.setText(_translate("LogWindow", "Среда..."))
