# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Work\python\bioinfo_excercise\PhyloSuite\PhyloSuite\PhyloSuite\uifiles\SeqViewer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Seq_viewer(object):
    def setupUi(self, Seq_viewer):
        Seq_viewer.setObjectName("Seq_viewer")
        Seq_viewer.resize(1050, 580)
        self.centralwidget = QtWidgets.QWidget(Seq_viewer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setAcceptDrops(True)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout.setContentsMargins(2, 0, 2, 2)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setAcceptDrops(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox = QtWidgets.QSpinBox(self.page)
        self.spinBox.setMaximum(999999999)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.page)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(398, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.MarkCombo = QtWidgets.QComboBox(self.page)
        self.MarkCombo.setMinimumSize(QtCore.QSize(150, 0))
        self.MarkCombo.setObjectName("MarkCombo")
        self.horizontalLayout.addWidget(self.MarkCombo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.page)
        self.page_display = QtWidgets.QWidget()
        self.page_display.setObjectName("page_display")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_display)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 227, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(191, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.page_display)
        self.label_5.setAcceptDrops(True)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.page_display)
        self.label_6.setAcceptDrops(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(191, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 227, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_display)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        Seq_viewer.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(Seq_viewer)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        Seq_viewer.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImport = QtWidgets.QAction(Seq_viewer)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/import2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport.setIcon(icon)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(Seq_viewer)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/export2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon1)
        self.actionExport.setObjectName("actionExport")
        self.actionCopy = QtWidgets.QAction(Seq_viewer)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(Seq_viewer)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon3)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(Seq_viewer)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/paste_512px_1175635_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon4)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(Seq_viewer)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon5)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(Seq_viewer)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon6)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRevsComp = QtWidgets.QAction(Seq_viewer)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/28105126-d6a6ce90-66fb-11e7-8546-72517772000b.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRevsComp.setIcon(icon7)
        self.actionRevsComp.setObjectName("actionRevsComp")
        self.actionReverse = QtWidgets.QAction(Seq_viewer)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/transfer-10-67552.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReverse.setIcon(icon8)
        self.actionReverse.setObjectName("actionReverse")
        self.actionComplement = QtWidgets.QAction(Seq_viewer)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/seq_viewer/if_ic_transform_48px_352180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionComplement.setIcon(icon9)
        self.actionComplement.setObjectName("actionComplement")
        self.actionSettings = QtWidgets.QAction(Seq_viewer)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/seq_Viewer/resourses/settings2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon10)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAnalyses = QtWidgets.QAction(Seq_viewer)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/picture/resourses/Menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnalyses.setIcon(icon11)
        self.actionAnalyses.setObjectName("actionAnalyses")
        self.toolBar.addAction(self.actionImport)
        self.toolBar.addAction(self.actionExport)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRevsComp)
        self.toolBar.addAction(self.actionReverse)
        self.toolBar.addAction(self.actionComplement)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(Seq_viewer)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Seq_viewer)

    def retranslateUi(self, Seq_viewer):
        _translate = QtCore.QCoreApplication.translate
        Seq_viewer.setWindowTitle(_translate("Seq_viewer", "Sequence Viewer"))
        self.label_2.setText(_translate("Seq_viewer", "Site:"))
        self.label.setText(_translate("Seq_viewer", "L"))
        self.label_3.setText(_translate("Seq_viewer", "Internal stop codons:"))
        self.label_5.setText(_translate("Seq_viewer", "<html><head/><body><p><a href=\"open_file\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">Open file(s)</span></a><span style=\" font-size:14pt;\"> to import</span></p></body></html>"))
        self.label_6.setText(_translate("Seq_viewer", "<html><head/><body><p><span style=\" font-size:14pt;\">Drop </span><span style=\" font-size:14pt; font-weight:600; color:#ffaa00;\">Alignment</span><span style=\" font-size:14pt;\"> file(s) here to open</span></p></body></html>"))
        self.toolBar.setWindowTitle(_translate("Seq_viewer", "toolBar"))
        self.actionImport.setText(_translate("Seq_viewer", "import"))
        self.actionImport.setToolTip(_translate("Seq_viewer", "Import Alignment"))
        self.actionExport.setText(_translate("Seq_viewer", "export"))
        self.actionExport.setToolTip(_translate("Seq_viewer", "Export Alignment"))
        self.actionCopy.setText(_translate("Seq_viewer", "copy"))
        self.actionCopy.setToolTip(_translate("Seq_viewer", "Copy"))
        self.actionCopy.setShortcut(_translate("Seq_viewer", "Ctrl+C"))
        self.actionCut.setText(_translate("Seq_viewer", "Cut"))
        self.actionCut.setToolTip(_translate("Seq_viewer", "Cut"))
        self.actionCut.setShortcut(_translate("Seq_viewer", "Ctrl+X"))
        self.actionPaste.setText(_translate("Seq_viewer", "Paste"))
        self.actionPaste.setToolTip(_translate("Seq_viewer", "Paste"))
        self.actionPaste.setShortcut(_translate("Seq_viewer", "Ctrl+V"))
        self.actionUndo.setText(_translate("Seq_viewer", "Undo"))
        self.actionUndo.setToolTip(_translate("Seq_viewer", "Undo"))
        self.actionUndo.setShortcut(_translate("Seq_viewer", "Ctrl+Z"))
        self.actionRedo.setText(_translate("Seq_viewer", "Redo"))
        self.actionRedo.setToolTip(_translate("Seq_viewer", "Redo"))
        self.actionRedo.setShortcut(_translate("Seq_viewer", "Ctrl+Y"))
        self.actionRevsComp.setText(_translate("Seq_viewer", "RevsComp"))
        self.actionRevsComp.setToolTip(_translate("Seq_viewer", "Reverse Complement"))
        self.actionReverse.setText(_translate("Seq_viewer", "Reverse"))
        self.actionReverse.setToolTip(_translate("Seq_viewer", "Reverse"))
        self.actionComplement.setText(_translate("Seq_viewer", "Complement"))
        self.actionComplement.setToolTip(_translate("Seq_viewer", "Complement"))
        self.actionSettings.setText(_translate("Seq_viewer", "settings"))
        self.actionSettings.setToolTip(_translate("Seq_viewer", "Settings"))
        self.actionAnalyses.setText(_translate("Seq_viewer", "analyses"))
        self.actionAnalyses.setToolTip(_translate("Seq_viewer", "Analyses"))

from uifiles import myRes_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seq_viewer = QtWidgets.QMainWindow()
    ui = Ui_Seq_viewer()
    ui.setupUi(Seq_viewer)
    Seq_viewer.show()
    sys.exit(app.exec_())

