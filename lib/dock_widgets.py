#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import file_explorer
import favourites
import preferences


class DockWidget(QtGui.QDockWidget):
    def __init__(self, title, mother, parent=None):
        QtGui.QDockWidget.__init__(self, parent)
        prefs = preferences.Preferences()

        self.parent = mother
        self.setFeatures(QtGui.QDockWidget.DockWidgetClosable | 
                         QtGui.QDockWidget.DockWidgetMovable | 
                         QtGui.QDockWidget.DockWidgetFloatable)
        self.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea | 
                             QtCore.Qt.RightDockWidgetArea | 
                             QtCore.Qt.BottomDockWidgetArea)
        self.setWindowTitle(title)
        self.setMinimumSize(QtCore.QSize(0, 0))

        if prefs.get_setting('Docks/ShowTitle', False).toBool() == False:
            empty_widget = QtGui.QFrame()
            self.setTitleBarWidget(empty_widget)





class TabDialog(QtGui.QTabWidget):
    def __init__(self, parent=None):
        QtGui.QTabWidget.__init__(self, parent)
        expandingSizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, 
                                                QtGui.QSizePolicy.Expanding)
        self.setSizePolicy(expandingSizePolicy)

        self.setDocumentMode(False)
        self.setMinimumSize(0, 0)



###############################################################################
## Dock widgets childs
###############################################################################
      

class LeftDockChildWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        prefs = preferences.Preferences()

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.setContentsMargins(1, 1, 1, 1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(0, 0)

        self.tabs = TabDialog()
        tab_position = prefs.get_setting('Docks/LeftDockTabPosition', 
                                         QtGui.QTabWidget.North).toInt()[0]
        self.tabs.setTabPosition(tab_position)
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        explorer = file_explorer.FileExplorer('FileExplorer')
        favourites_ = favourites.Favourites('Favourites')
        self.tabs.addTab(explorer, 'File Browser')
        self.tabs.addTab(favourites_, 'Bookmarks')





class RightDockChildWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        prefs = preferences.Preferences()

        mainLayout = QtGui.QGridLayout()
        mainLayout.setContentsMargins(1, 1, 1, 1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(0, 0)

        self.tabs = TabDialog()
        tab_position = prefs.get_setting('Docks/RightDockTabPosition', 
                                         QtGui.QTabWidget.North).toInt()[0]
        self.tabs.setTabPosition(tab_position)
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        self.tabs.addTab(QtGui.QPlainTextEdit(), 'Right 1')
        self.tabs.addTab(QtGui.QPlainTextEdit(), 'Right 2')
        self.tabs.currentChanged.connect(self.tabSelected)
     

    def tabSelected(self, index):
        print('tabSelected')




class BottomDockChildWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        prefs = preferences.Preferences()

        mainLayout = QtGui.QGridLayout()
        mainLayout.setContentsMargins(1, 1, 1, 1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(0, 0)
        
        self.tabs = TabDialog()
        tab_position = prefs.get_setting('Docks/BottomDockTabPosition', 
                                         QtGui.QTabWidget.North).toInt()[0]
        self.tabs.setTabPosition(tab_position)
        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)

        self.tabs.addTab(QtGui.QPlainTextEdit(), 'Bottom 1')
        self.tabs.addTab(QtGui.QPlainTextEdit(), 'Bottom 2')
        self.tabs.currentChanged.connect(self.tabSelected)
     
     
    def tabSelected(self, index):
        print('tabSelected')



###############################################################################
## Dock widgets assemble
###############################################################################
      

class DockWidgetsInit(QtCore.QObject):

    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.mother = parent
        self.setObjectName('DockWidgetsInit')


    def createLeftDock(self):
        dockWidget = DockWidget('Navigator', self.mother)
        dockWidget.setObjectName("dockWidgetLeft")

        dockWidget.setWidget(LeftDockChildWidget())
        self.mother.addDockWidget(QtCore.Qt.LeftDockWidgetArea, dockWidget)


    def createRightDock(self):
        dockWidget = DockWidget('Snippets', self.mother)
        dockWidget.setObjectName("dockWidgetRight")

        dockWidget.setWidget(RightDockChildWidget())
        self.mother.addDockWidget(QtCore.Qt.RightDockWidgetArea, dockWidget)


    def createBottomDock(self):
        dockWidget = DockWidget('Output', self.mother)
        dockWidget.setObjectName("dockWidgetBottom")

        dockWidget.setWidget(BottomDockChildWidget())
        self.mother.addDockWidget(QtCore.Qt.BottomDockWidgetArea, dockWidget)







