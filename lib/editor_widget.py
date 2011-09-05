#!/usr/bin/env python
import text_edit
from PyQt4 import QtCore
from PyQt4 import QtGui




class StackWidget(QtGui.QStackedWidget):
    def __init__(self, fileName, text, isNewFile, parent=None):
        QtGui.QStackedWidget.__init__(self, parent)

        self.setObjectName('EditorStackWidget')
        tab = text_edit.TextEdit(isNewFile, fileName, text)
        self.addWidget(tab)
        self.currentChanged.connect(self.updateComboBox)
        self.widgetRemoved.connect(self.removeComboBoxItem)
        

    def updateComboBox(self, index):
        comboBox = self.parent().findChild(QtGui.QWidget, 'EditorComboBox')
        comboBox.setCurrentIndex(index)



    def removeComboBoxItem(self, index):
        comboBox = self.parent().findChild(QtGui.QWidget, 'EditorComboBox')  
        comboBox.removeItem(index)

        if self.count() == 0:
            self.parent().hide()
            self.parent().deleteLater()
            self.get_main_window().activeEditorChanged.emit('deletedEditor')



    def get_main_window(self):
        tops = QtGui.QApplication.topLevelWidgets()
        mainwindow = None
        for top in tops:
            if top.objectName() == 'MainWindow':
                mainwindow = top
        return mainwindow




class EditorWidget(QtGui.QWidget):
    def __init__(self, fileurl, text, isnewfile, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setObjectName('Editor')
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setContentsMargins(10, 0, 10, 0)
        mainLayout.setSpacing(0)
        fixedSizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)

        headerLayout = QtGui.QHBoxLayout()
        headerLayout.setContentsMargins(0, 0, 0, 0)
        headerLayout.setSpacing(0)
        
        self.combobox = QtGui.QComboBox(self)
        self.combobox.addItem(QtCore.QFileInfo(fileurl).fileName())
        self.combobox.setObjectName('EditorComboBox')
        self.combobox.setSizePolicy(fixedSizePolicy)
        self.combobox.activated.connect(self.show_other_textedit)
        headerLayout.addWidget(self.combobox)

        self.closeFileButton = QtGui.QPushButton()
        self.closeFileButton.setObjectName('EditorCloseFileButton')
        self.closeFileButton.setText('X')
        self.closeFileButton.clicked.connect(self.closeFile)
        self.closeFileButton.setSizePolicy(QtGui.QSizePolicy(
                                             QtGui.QSizePolicy.Fixed,
                                             QtGui.QSizePolicy.Fixed))
        headerLayout.addWidget(self.closeFileButton)
        mainLayout.addLayout(headerLayout)

        layout = QtGui.QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.stack = StackWidget(fileurl, text, isnewfile)
        layout.addWidget(self.stack)

        mainLayout.addLayout(layout)
        self.setLayout(mainLayout)

        

    def closeFile(self):
        self.setActiveEditor('closeButtonClicked')
        mainwindow = self.get_main_window()
        mainwindow.close_file()


    def show_other_textedit(self, index):
        '''Enable view other text edits'''
        self.stack.setCurrentIndex(self.combobox.currentIndex())
        mainwindow = self.get_main_window()
        mainwindow.active_editor = self
        mainwindow.activeEditorChanged.emit('comboBoxSelection')



    def get_main_window(self):
        tops = QtGui.QApplication.topLevelWidgets()
        mainwindow = None
        for top in tops:
            if top.objectName() == 'MainWindow':
                mainwindow = top
        return mainwindow
        
        

    def setActiveEditor(self, reason):
        mainwindow = self.get_main_window()
        mainwindow.active_editor = self
        mainwindow.activeEditorChanged.emit(reason)
        
        
        
