#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import common
import resources
import preferences




class Favourites(QtGui.QWidget):
    def __init__(self, objname, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.zen = common.Common()

        gridlayout = QtGui.QGridLayout(self)
        self.table = QtGui.QTableWidget()
        gridlayout.addWidget(self.table)
        self.setLayout(gridlayout)
        
        fileNameItem = QtGui.QTableWidgetItem('hello')
        self.table.insertRow(0)
        self.table.setItem(0, 0, fileNameItem)
#
#
#        for fn in files:
#            print(fn)
#            file = QtCore.QFile(self.currentDir.absoluteFilePath(fn))
#            fileNameItem = QtGui.QTableWidgetItem(fn)
#            row = self.ui.theTable.rowCount()
#            self.ui.theTable.insertRow(row)
#            self.ui.theTable.setItem(row, 0, fileNameItem)

#
#
#    def get_favourites(self):