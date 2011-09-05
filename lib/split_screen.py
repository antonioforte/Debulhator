#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui
import editor_widget
    
    
    
    
class SplitterDialog(QtGui.QSplitter):
    def __init__(self, parent=None):
        QtGui.QSplitter.__init__(self, parent)

    def childEvent(self,event):
        if event.type() == QtCore.QEvent.ChildRemoved:
            if self.count() == 0:
                self.hide()
                self.deleteLater()
                print('Removing splitter',self.objectName())
        return QtGui.QSplitter.childEvent(self,event)
    
    
    
    
class SplitScreen(QtCore.QObject):
    
    def __init__(self, parent=None):
        QtCore.QObject.__init__(self, parent)
        self.parent = parent
    

    def splitVScreen(self):
        self.splitScreen('VerticalSplitter',2)
        
        
    def splitHScreen(self):
        self.splitScreen('HorizontalSplitter',1)


    def splitScreen(self, typeOfSplitter, orientation):
        pass
#        # todo : provide suitable size 
        self.parent.newfile_n += 1
        newfilename = 'new '+str(self.parent.newfile_n)

        self.active_editor = self.parent.active_editor
        if self.active_editor == None:
            return
        activeEditorParent = self.parent.active_editor.parent()
        
        if activeEditorParent.objectName() == typeOfSplitter:
            editor = editor_widget.EditorWidget(newfilename, '', True)    
            index = activeEditorParent.indexOf(self.active_editor)+1
            activeEditorParent.insertWidget(index,editor)
        else:
            splitter = SplitterDialog()
            splitter.setOrientation(QtCore.Qt.Orientation(orientation))
            splitter.setObjectName(typeOfSplitter)
                
            index = activeEditorParent.indexOf(self.active_editor)+1
            activeEditorParent.insertWidget(index,splitter)

            editor = editor_widget.EditorWidget(newfilename, '', True)  
            splitter.addWidget(self.active_editor)
            splitter.addWidget(editor)

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            