#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui

import lib.common
import lib.resources
import lib.preferences

import outline_python
import outline_javascript
import outline_generic
import outline_html


class Outliner(QtGui.QWidget):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        
        self.setObjectName('Outliner')
        self.zen = lib.common.Common()
        self.prefs = lib.preferences.Preferences()
        self.file = None

        self.gridlayout = QtGui.QGridLayout(self)
        self.setMinimumSize(0, 0)
        self.sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Expanding)

        # QTreeView
        self.tree = QtGui.QTreeView(self)
        self.tree.setHeaderHidden(True)
        self.tree.setObjectName("OutlinerTreeView")
        self.tree.setSizePolicy(self.sizePolicy)
        self.tree.clicked.connect(self.goto_line)

        # Actions
        self.act_collapse_all = QtGui.QAction(self.tr("&Collapse all"), self)
        self.act_collapse_all.setIcon(QtGui.QIcon(":/png/collapse_all.png"))
        self.act_collapse_all.setStatusTip(self.tr("Collapse all"))
        self.act_collapse_all.triggered.connect(self.tree.collapseAll)
        
        self.act_uncollapse_all = QtGui.QAction(self.tr("&Uncollapse all"), self)
        self.act_uncollapse_all.setIcon(QtGui.QIcon(":/png/expand_all.png"))
        self.act_uncollapse_all.setStatusTip(self.tr("Uncollapse all"))
        self.act_uncollapse_all.triggered.connect(self.tree.expandAll)
        
        # ToolBar
        self.toolbar = QtGui.QToolBar()
        self.toolbar.setObjectName("ClassBrowserToolBar")
        self.toolbar.setIconSize(QtCore.QSize(20, 20))
        self.toolbar.addAction(self.act_collapse_all)
        self.toolbar.addAction(self.act_uncollapse_all)
        self.toolbar.setStyleSheet('''QToolBar{border:1px solid #000000;}''')
        
        self.gridlayout.addWidget(self.toolbar)
        self.gridlayout.addWidget(self.tree)


    def update_tree(self, file):
        self.file = file
        self.model = OutlinerModel(file)     
        self.tree.setModel(self.model)
        self.tree.expandAll()


    def goto_line(self, event):
        lineno = self.model.nodeFromIndex(event).lineno
        if lineno != 'nonumber': 
            main = self.zen.get_main_instance()
            active_textedit = main.get_active_textedit()
            active_textedit.setCursorPosition(int(lineno) - 1, 0)
            active_textedit.ensureCursorVisible() 
            active_textedit.ensureLineVisible(int(lineno))
            active_textedit.setFocus()



class myNode(object):
    '''Represents node of QAbstractItemModel'''
    def __init__(self, name, kind, lineno, parent=None):
       
        self.name = name
        self.kind = kind
        self.lineno = lineno
        self.parent = parent
        self.children = []
       
        self.setParent(parent)
       
       
    def setParent(self, parent):
        if parent != None:
            self.parent = parent
            self.parent.appendChild(self)
        else:
            self.parent = None
           
           
    def appendChild(self, child):
        self.children.append(child)
       
       
    def childAtRow(self, row):
        return self.children[row]
   
   
    def rowOfChild(self, child):       
        for i, item in enumerate(self.children):
            if item == child:
                return i
        return -1
   
   
    def removeChild(self, row):
        value = self.children[row]
        self.children.remove(value)
        return True
       
       
    def __len__(self):
        return len(self.children)
       
        

class OutlinerModel(QtCore.QAbstractItemModel):
    def __init__(self, file):
        QtCore.QAbstractItemModel.__init__(self)

        self.zen = lib.common.Common()
        self.prefs = lib.preferences.Preferences()
        self.file = file
        self.language = self.zen.determine_language(str(self.file))

        self.root = myNode('root', 'on', 'this is root', None)
        self.add_data()

        self.columns = 1
        self.setObjectName('OutlinerModel')
        

    def data(self, index, role):
        ''' 
        Returns the data stored under the given role for the item 
        referred to by the index.

        @param index PySide.QtCore.QModelIndex
        @param role int
        @return QtCore.QVariant
        '''
        node = self.nodeFromIndex(index)
        
        if role == QtCore.Qt.DecorationRole:

            if node.kind == 'namespace':
                return QtGui.QIcon(":/png/source-import.png")
            if node.kind == 'class':
                return QtGui.QIcon(":/png/source-class.png")
            if node.kind == 'variable':
                return QtGui.QIcon(":/png/source-var.png")
            if node.kind == 'member':
                return QtGui.QIcon(":/png/source-member.png")
            if node.kind == 'function':
                return QtGui.QIcon(":/png/source-func.png")
            
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.QVariant(int(QtCore.Qt.AlignVCenter | 
                                       QtCore.Qt.AlignLeft))
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if index.column() == 0:
            return QtCore.QVariant(node.name)
        elif index.column() == 1:
            return QtCore.QVariant(node.kind)
        elif index.column() == 2:
            return QtCore.QVariant(node.lineno)
        else:
            return QtCore.QVariant()
        
        
        
    def columnCount(self, parent):
        ''' 
        Returns the number of columns for the children of the given parent .
        
        @param parent PySide.QtCore.QModelIndex
        @return type int
        '''
        return self.columns


    def index(self, row, column, parent):
        '''
        Returns the index of the item in the model specified 
        by the given row , column and parent index.

        @param row int
        @param column int
        @param parent PySide.QtCore.QModelIndex
        @return QtCore.QModelIndex
        '''
        node = self.nodeFromIndex(parent)
        return self.createIndex(row, column, node.childAtRow(row))


    def rowCount(self, parent):
        '''
        Returns the number of rows under the given parent . 
        When the parent is valid it means that rowCount 
        is returning the number of children of parent.        

        @param parent PySide.QtCore.QModelIndex
        @return type int
        '''
        node = self.nodeFromIndex(parent)
        if node is None:
            return 0
        return len(node)


    def nodeFromIndex(self, index):
        return index.internalPointer() if index.isValid() else self.root


    def parent(self, child):
        '''
        Returns the parent of the model item with the given index. 
        If the item has no parent, an invalid QModelIndex is returned.
        
        @param child PySide.QtCore.QModelIndex
        @return type PySide.QtCore.QModelIndex
        '''
        if not child.isValid():
            return QtCore.QModelIndex()

        node = self.nodeFromIndex(child)
        if node is None:
            return QtCore.QModelIndex()

        parent = node.parent
        if parent is None:
            return QtCore.QModelIndex()
       
        grandparent = parent.parent
        if grandparent is None:
            return QtCore.QModelIndex()
        row = grandparent.rowOfChild(parent)
       
        assert row != -1
        return self.createIndex(row, 0, parent)



    def add_data(self):
        # HTML and XML are not handled by ctags
        if self.language == 'HTML' or self.language == 'xml':
            self.create_html_outline()
            return
        
        # Check if language is supported by ctags
        ctags_supported_langs = self.zen.ctags_supported_langs()
        if self.zen.is_ctags_available() == False:
            return 

        if self.language in ctags_supported_langs:
            if self.language == 'Python':
                try:
                    _outliner = outline_python.PythonOutliner(self.root, self.file)
                    _outliner.outline()
                except Exception as e:
                    print ("Error making python outline. ", e)
                    self.create_error_outline()
            elif self.language == 'JavaScript':
                try:
                    _outliner = outline_javascript.JavascriptOutliner(self.root, self.file)
                    _outliner.outline()
                except Exception as e:
                    print ("Error making Javascript outline. ", e)
                    self.create_error_outline()
            else:
                try:
                    _outliner = outline_generic.GenericOutliner(self.root, self.file)
                    _outliner.outline()
                except Exception as e:
                    print ("Error making generic outline. ", e)
                    self.create_error_outline()
        else:
            self.create_empty_outline()
        
        
    def create_error_outline(self):
        myNode('error', 'on', 'this an error outline', self.root)

        
    def create_empty_outline(self):
        myNode('not available', 'on', 'this an empty outline', self.root)


    def create_html_outline(self):
        _outliner = outline_html.HtmlOutliner(self.root, self.file, self.language)
        _outliner.outline()

        
  
        
