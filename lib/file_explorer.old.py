#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import common
import resources
import preferences




class FileExplorer(QtGui.QWidget):
    def __init__(self, objname, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.res = resources.Resources()
        self.zen = common.Common()

        self.currentindex = None

        expandingSizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, 
                                                QtGui.QSizePolicy.Expanding)
        gridlayout = QtGui.QGridLayout(self)
        gridlayout.setContentsMargins(0, 0, 0, 0)
        self.setObjectName(objname)

        self.setMinimumSize(0, 0)
        self.create_actions()

        # ToolBar
        self.toolbar = QtGui.QToolBar()
        self.toolbar.setObjectName("FileExplorerToolBar")
        self.toolbar.setIconSize(QtCore.QSize(20, 20))
        self.toolbar.addAction(self.goup_act)
        self.toolbar.addAction(self.gohome_act)
        self.toolbar.addAction(self.godoc_path_act)
        gridlayout.addWidget(self.toolbar)

        # ComboBox current path
        self.combobox_curpath = QtGui.QComboBox()
        self.combobox_curpath.setObjectName("FileExplorerCombobox_curpath")
        self.combobox_curpath.setEditable(True)
        gridlayout.addWidget(self.combobox_curpath)

        # QFileSystemModel
        self.model = QtGui.QFileSystemModel()
        self.model.setNameFilterDisables(0)
        # File that are shown
        filters = ["*.py","readme"]
        self.model.setNameFilters(filters)

        self.model.setRootPath("/")

        # QTreeView
        self.tree = QtGui.QTreeView(self)
        self.tree.setModel(self.model)
        self.tree.setObjectName("fileExplorerTreeView")
        self.tree.setSizePolicy(expandingSizePolicy)
        
        self.currentindex = self.model.index(\
             preferences.AppSettings().settings['Explorer/StartDir'])
        self.tree.setRootIndex(self.currentindex)
        
        self.tree.setHeaderHidden(True)
        self.tree.sortByColumn(0, QtCore.Qt.AscendingOrder)
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
        self.tree.setRootIsDecorated(True)
        self.tree.setSortingEnabled(True)
        self.tree.mouseDoubleClickEvent = self.openFile
        gridlayout.addWidget(self.tree)
        
        # ComboBox current path
        self.combobox_filter = QtGui.QComboBox()
        self.combobox_filter.setObjectName("FileExplorerCombobox_filter")
        self.combobox_filter.setEditable(True)
        gridlayout.addWidget(self.combobox_filter)



        
    def go_up_onedir(self):
        curpath = self.currentindex
        self.tree.setRootIndex(curpath.parent())
        self.currentindex = curpath.parent()
        
        
    def go_home(self):
        homedir = self.zen.get_home_dir()
        self.currentindex = self.model.index(homedir)
        self.tree.setRootIndex(self.currentindex)
        
        
    def go_doc_path(self):
        main = self.zen.get_main_instance()

        if main.active_editor != None:
            active_textedit = main.get_active_textedit()
            folder = QtCore.QFileInfo(active_textedit.currentfile).absoluteDir()
            if folder.exists():
                self.currentindex = self.model.index(folder.path())
                self.tree.setRootIndex(self.currentindex)



    def openFile(self, event):
        indexChosen = self.tree.indexAt(event.pos())
        main = self.zen.get_main_instance()
        fileInfo = self.model.fileInfo(indexChosen)
        if fileInfo.isFile():
            checkFile = main.isfile_open(fileInfo.absoluteFilePath())
            if checkFile[0]:
                checkFile[1].setCurrentIndex(checkFile[2])
            else:
                main.load_file(fileInfo.absoluteFilePath())
        elif fileInfo.isDir():
            self.currentindex = self.model.index(fileInfo.absoluteFilePath())
            self.tree.setRootIndex(self.currentindex)
            

        
        
    def create_actions(self):
        self.goup_act = QtGui.QAction(self.tr("&Up"), self)
        self.goup_act.setIcon(self.zen.get_icon_frombase64(self.res.up_arrow))
        self.goup_act.setStatusTip(self.tr("Go up one dir"))
        self.goup_act.triggered.connect(self.go_up_onedir)
        
        self.gohome_act = QtGui.QAction(self.tr("&Home"), self)
        self.gohome_act.setIcon(self.zen.get_icon_frombase64(self.res.home))
        self.gohome_act.setStatusTip(self.tr("Go up one dir"))
        self.gohome_act.triggered.connect(self.go_home)
        
        self.godoc_path_act = QtGui.QAction(self.tr("&Home"), self)
        self.godoc_path_act.setIcon(self.zen.get_icon_frombase64(self.res.go_doc_path))
        self.godoc_path_act.setStatusTip(self.tr("Go up one dir"))
        self.godoc_path_act.triggered.connect(self.go_doc_path)
        
        
        
    
    
