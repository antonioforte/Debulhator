#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import common
import resources
import preferences


# Buttons on top adding :  
#                        current file dir, 
#                        current file
#                        new empty row
#                        delete row
# Rows are editable
# Populate on app begin
# Save on app close


class MyTable(QtGui.QTableWidget):
    def __init__(self, parent):
        QtGui.QTableWidget.__init__(self, parent)
        self.setObjectName("FavouritesTableWidget")

        self.setHorizontalHeaderLabels(['Filename', 'Location'])

        self.setColumnCount(2)
        self.verticalHeader().hide()


    def add_item(self, newitem):
        rows = self.rowCount()
        self.insertRow(rows)
        for itemstring in newitem:
            item = QtGui.QTableWidgetItem()
            item.setText(QtCore.QString(itemstring))
            
            self.setItem(rows, newitem.index(itemstring), item)
        


class Favourites(QtGui.QWidget):
    def __init__(self, objname, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.zen = common.Common()
        self.setObjectName(objname)
        self.create_actions()

        gridlayout = QtGui.QGridLayout(self)
        
        # ToolBar
        self.toolbar = QtGui.QToolBar()
        self.toolbar.setObjectName("FavouritesWidgetToolBar")
        self.toolbar.setIconSize(QtCore.QSize(20, 20))
        self.toolbar.addAction(self.goup_act)
        self.toolbar.addAction(self.gohome_act)
        self.toolbar.addAction(self.godoc_path_act)
        self.toolbar.setStyleSheet('''QToolBar{border:1px solid #000000;}''')
        gridlayout.addWidget(self.toolbar)
        
        self.table = MyTable(self)
        gridlayout.addWidget(self.table)

        self.table.add_item(['file1','/home/dirq/'])
        self.table.add_item(['file2','/home/dirf/'])
        self.table.add_item(['file3','/home/dire/'])
        self.table.resizeColumnsToContents()
        self.setLayout(gridlayout)
        


    def create_actions(self):
        '''Create actions to the Explorer'''
        # Explorer bar
        self.goup_act = QtGui.QAction(self.tr("&Up"), self)
        self.goup_act.setIcon(QtGui.QIcon(":/png/explorer-up-arrow.png"))
        self.goup_act.setStatusTip(self.tr("Go up one dir"))
        self.goup_act.triggered.connect(self.add_current_file)
        
        self.gohome_act = QtGui.QAction(self.tr("&Home"), self)
        self.gohome_act.setIcon(QtGui.QIcon(":/png/explorer-home.png"))
        self.gohome_act.triggered.connect(self.add_current_dir)
        
        self.godoc_path_act = QtGui.QAction(self.tr("&Home"), self)
        self.godoc_path_act.setIcon(QtGui.QIcon(":/png/explorer-go-doc-path.png"))
        self.godoc_path_act.setStatusTip(self.tr("Go to document path"))
        self.godoc_path_act.triggered.connect(self.add_new_row)
      
      
    def add_current_file(self):
        pass
    def add_current_dir(self):
        pass
    def add_new_row(self):
        pass


