#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import common
import resources
import preferences


class SortFilterProxyModel(QtGui.QSortFilterProxyModel):

    def __init__(self, files_to_hide, files_to_hide_strings, parent=None):
        QtGui.QSortFilterProxyModel.__init__(self, parent)
        self.setDynamicSortFilter(True)
        self.files_to_hide = files_to_hide
        self.files_to_hide_strings = files_to_hide_strings


    def filterAcceptsRow (self, source_row, source_parent):
        index0 = self.sourceModel().index(source_row, 0, source_parent)
        filePath = self.sourceModel().filePath(index0)
        
        # Hide based on string 
        for filetypestring in self.files_to_hide_strings:
            if filePath.contains(filetypestring.toString(), QtCore.Qt.CaseInsensitive):
                return False
            
        # Hide based on extension
        for filetype in self.files_to_hide:
            if filePath.endsWith(filetype.toString(), QtCore.Qt.CaseInsensitive):
                return False

        return True





class FileExplorer(QtGui.QWidget):
    def __init__(self, objname, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.zen = common.Common()
        self.prefs = preferences.Preferences()

        self.files_to_hide_strings = self.prefs.get_setting(\
                                 'Explorer/FileTypesToHideStrings', '').toList()

        self.files_to_hide = self.prefs.get_setting(\
                                        'Explorer/FileTypesToHide', '').toList()

        self.currentindex = None

        expandingSizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                                QtGui.QSizePolicy.Expanding)
        gridlayout = QtGui.QGridLayout(self)
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
        self.toolbar.setStyleSheet('''QToolBar{border:1px solid #000000;}''')
        gridlayout.addWidget(self.toolbar)

        # todo : Save 5 last dirs visited
        # ComboBox current path
#        self.combobox_curpath = QtGui.QComboBox()
#        self.combobox_curpath.setObjectName("FileExplorerCombobox_curpath")
#        self.combobox_curpath.setEditable(True)
#        gridlayout.addWidget(self.combobox_curpath)

        # QFileSystemModel
        self.model = QtGui.QFileSystemModel()
        self.model.setNameFilterDisables(0)
        self.model.setNameFilters([])
        self.currentindex = self.model.index(self.prefs.get_setting(\
                                        'Explorer/StartDir', '/').toString())
        self.proxii = SortFilterProxyModel(self.files_to_hide,
                                           self.files_to_hide_strings,
                                           self)
        self.model.setRootPath("/")
        self.proxii.setSourceModel(self.model)
        
        # QTreeView
        self.tree = QtGui.QTreeView(self)
        self.tree.setModel(self.proxii)
        self.tree.setObjectName("fileExplorerTreeView")
        self.tree.setSizePolicy(expandingSizePolicy)
        self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))
        self.tree.setHeaderHidden(True)
        self.tree.setSortingEnabled(True)
        self.tree.sortByColumn(-1, QtCore.Qt.AscendingOrder)
        self.tree.hideColumn(1)
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
        self.tree.setRootIsDecorated(True)
        self.tree.mouseDoubleClickEvent = self.openFile
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu) 
        self.tree.customContextMenuRequested.connect(self.tree_rightclick)
        gridlayout.addWidget(self.tree)
        
        # Filter
        self.filter_line = QtGui.QLineEdit(self)
        self.filter_line.setToolTip('''Enter filters''')
        self.filter_line.textChanged.connect(self.update_filters)
        self.filter_line.setObjectName("FileExplorer_filter")
        self.filter_line.resizeEvent = self.filter_resize_event

        # todo : hover state icon
        self.clearfilter = QtGui.QToolButton(self.filter_line)
        self.clearfilter.setIcon(QtGui.QIcon(":/png/lineedit-clear.png"))
        self.clearfilter.setIconSize(QtCore.QSize(20, 20))
        self.clearfilter.setMinimumSize(20, 20)
        self.clearfilter.setCursor(QtCore.Qt.ArrowCursor)
        self.clearfilter.clicked.connect(self.clear_lineedit_filter)
        
        gridlayout.addWidget(self.filter_line)

        self.filter_line.setStyleSheet('''QLineEdit {border:none;padding:3px;;margin:0px;}''') 
        self.clearfilter.setStyleSheet('''QToolButton {border:none;margin:0px;}''')



    def tree_rightclick(self, point):
        '''Handle Explorer right click'''
        menu = QtGui.QMenu(self.tree)
        menu.addAction(self.show_allfiles_act)
        menu.addAction(self.hide_somefiles_act)
        menu.popup(QtGui.QCursor.pos())



    def filter_resize_event(self, size):
        '''Position the clear button'''
        sz = self.clearfilter.sizeHint()
        self.clearfilter.move(self.filter_line.width() - sz.width() - 1,
                              self.filter_line.height() - sz.height() + 1)
        


    def clear_lineedit_filter(self):
        '''Clear filter_line QTextEdit'''
        self.filter_line.clear()
        


    def update_filters(self, text):
        '''Update model filters'''
        if len(text) == 0:
            self.model.setNameFilters([])
        else:
            if text.contains(';'):
                filters = []
                for item in text.split(';'):
                    filters.append(item)
                self.model.setNameFilters(filters)
            else:
                self.model.setNameFilters([text])

        
        
    def show_allfiles(self):
        '''Show system files and those specified in settings to be hidden'''
        self.model.setFilter(QtCore.QDir.Hidden | 
                             QtCore.QDir.AllDirs | 
                             QtCore.QDir.Files | 
                             QtCore.QDir.NoDotAndDotDot)
        self.proxii = SortFilterProxyModel([], [], self)
        self.proxii.setSourceModel(self.model)
        self.tree.setModel(self.proxii)
        self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))
        
        
        
    def hide_some_files(self):
        '''Hide system files and those specified in settings to be hidden'''
        self.model.setFilter(QtCore.QDir.NoDotAndDotDot | 
                             QtCore.QDir.AllDirs | 
                             QtCore.QDir.Files)
        self.proxii = SortFilterProxyModel(self.files_to_hide,
                                           self.files_to_hide_strings,
                                           self)
        self.proxii.setSourceModel(self.model)
        self.tree.setModel(self.proxii)
        self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))
        
        
        
    def go_up_onedir(self):
        curpath = self.currentindex
        self.tree.setRootIndex(self.proxii.mapFromSource(curpath.parent()))
        self.currentindex = curpath.parent()
        
        
        
    def go_home(self):
        homedir = self.zen.get_home_dir()
        self.currentindex = self.model.index(homedir)
        self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))
        
        
        
    def go_doc_path(self):
        main = self.zen.get_main_instance()

        if main.active_editor != None:
            active_textedit = main.get_active_textedit()
            folder = QtCore.QFileInfo(active_textedit.currentfile).absoluteDir()

            if folder.exists():
                self.currentindex = self.model.index(folder.absolutePath())
                self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))



    def openFile(self, event):
        indexChosen = self.tree.indexAt(event.pos())
        main = self.zen.get_main_instance()
        fileInfo = self.model.fileInfo(self.proxii.mapToSource(indexChosen))
        
        if fileInfo.isFile():
            checkFile = main.isfile_open(fileInfo.absoluteFilePath())
            if checkFile[0]:
                checkFile[1].setCurrentIndex(checkFile[2])
            else:
                main.load_file(fileInfo.absoluteFilePath())
        elif fileInfo.isDir():
            self.currentindex = self.model.index(fileInfo.absoluteFilePath())
            self.tree.setRootIndex(self.proxii.mapFromSource(self.currentindex))
            

        
        
    def create_actions(self):
        '''Create actions to the Explorer'''
        # Explorer bar
        self.goup_act = QtGui.QAction(self.tr("&Up"), self)
        self.goup_act.setIcon(QtGui.QIcon(":/png/explorer-up-arrow.png"))
        self.goup_act.setStatusTip(self.tr("Go up one dir"))
        self.goup_act.triggered.connect(self.go_up_onedir)
        
        self.gohome_act = QtGui.QAction(self.tr("&Home"), self)
        self.gohome_act.setIcon(QtGui.QIcon(":/png/explorer-home.png"))
        self.gohome_act.setStatusTip(self.tr("Go to home dir"))
        self.gohome_act.triggered.connect(self.go_home)
        
        self.godoc_path_act = QtGui.QAction(self.tr("&Go to document path"), self)
        self.godoc_path_act.setIcon(QtGui.QIcon(":/png/explorer-go-doc-path.png"))
        self.godoc_path_act.setStatusTip(self.tr("Go to document path"))
        self.godoc_path_act.triggered.connect(self.go_doc_path)
        
        # Context Menu TreeView 
        self.show_allfiles_act = QtGui.QAction(self.tr("&Show all files"), self)
        self.show_allfiles_act.setStatusTip(self.tr("Show all files"))
        self.show_allfiles_act.triggered.connect(self.show_allfiles)
        
        self.hide_somefiles_act = QtGui.QAction(self.tr("&Hide some files"), self)
        self.hide_somefiles_act.setStatusTip(self.tr("Hide some files"))
        self.hide_somefiles_act.triggered.connect(self.hide_some_files)
    
    
