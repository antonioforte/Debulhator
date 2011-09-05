#!/usr/bin/env python
import sys, os
from xml.etree import ElementTree as ET

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.Qsci import QsciScintilla

import lib.text_edit
import lib.start_page
import lib.editor_widget
import lib.split_screen
import lib.preferences
import lib.dock_widgets

__appname__ = 'Debulhator'
__company__ = 'My Company'


class SplitterDialog(QtGui.QSplitter):
    def __init__(self, parent=None):
        QtGui.QSplitter.__init__(self, parent)
        self.setObjectName('HorizontalSplitter')
        


class MainWindow(QtGui.QMainWindow):
    activeEditorChanged = QtCore.pyqtSignal(str)

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setObjectName('MainWindow')

        self.prefs = lib.preferences.Preferences()

        self.newfile_n = 0
        self.max_recent_files = self.prefs.get_setting(\
                                        'Recent/MaxRecentFiles', 10).toInt()[0]
        self.recent_files = [''] * self.max_recent_files
        self.curdir = self.app_dir()
        self.setAcceptDrops(True)

        self.activeEditorChanged.connect(self.active_editor_changed)
        self.active_editor = None

        self.centralwidget = QtGui.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.main_layout = QtGui.QGridLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.splitter = SplitterDialog()
        self.main_layout.addWidget(self.splitter)
        startpage = lib.start_page.StartPage(self.splitter)
        
        self.split_screen = lib.split_screen.SplitScreen(self)
        self.docks = lib.dock_widgets.DockWidgetsInit(self)
        self.docks.createLeftDock()
        self.docks.createBottomDock()
        self.docks.createRightDock()
        
        self.statusBar().show()
        self.setWindowTitle(__appname__)
        self.setWindowIcon(QtGui.QIcon(':/png/app_icon.png'))
        self.centralwidget.setLayout(self.main_layout)

        self.restore_window_state()
        self.get_recent_files()
        self.create_actions()
        self.create_toolbars()
        self.create_menus()
        

###############################################################################
## Get initial settings
###############################################################################


    def restore_window_state(self):
        '''Restore window state'''
        pos = self.prefs.get_setting('Window/Position', 
                                     QtCore.QPoint(200, 200)).toPoint()
        size = self.prefs.get_setting('Window/Size', 
                                     QtCore.QSize(400, 400)).toSize()
        state = self.prefs.get_setting('Window/State', 
                                     QtCore.QByteArray()).toByteArray()
        self.restoreState(state)
        self.resize(size)
        self.move(pos)



    def get_recent_files(self):
        '''Get Recent files'''
        for i in range(len(self.recent_files)):
            file = self.prefs.get_setting('RecentFiles/file'+str(i), 
                                          '').toString()
            self.recent_files[i] = file



    def write_settings_app_exit(self):
        '''Write settings on application exit'''
        self.prefs.set_setting("Window/Position", self.pos())
        self.prefs.set_setting("Window/Size", self.size())
        self.prefs.set_setting("Window/State", self.saveState())

        for i in range(len(self.recent_files)):
            self.prefs.set_setting("RecentFiles/file"+str(i), 
                                    self.recent_files[i])
            

###############################################################################
## active_editor_changed
###############################################################################


    def active_editor_changed(self, reason):
        '''React to change of active editor'''
        print('active_editor_changed', reason)
        if reason == 'deletedEditor':
            editors = self.findChildren(QtGui.QWidget,'Editor')
            if len(editors) != 1:
                for editor in editors:
                    if not editor.isHidden():
                        self.active_editor = editor
                        self.update_actions()
            elif len(editors) == 1:
                self.update_actions_noeditors()
        else:
            self.update_actions()
            
       
       
    def update_actions_noeditors(self):
        print('No editors left')
        self.active_editor = None
        self.setWindowTitle(__appname__)
        
        self.act_save.setEnabled(False) 
        self.act_saveas.setEnabled(False) 
        self.act_saveall.setEnabled(False) 
        
        self.act_cut.setEnabled(False)
        self.act_copy.setEnabled(False)

        self.act_undo.setEnabled(False)
        self.act_redo.setEnabled(False)
        
        self.act_closefile.setEnabled(False)
        self.act_closeallfiles.setEnabled(False)
        
        self.act_split_h_screen.setEnabled(False)
        self.act_split_v_screen.setEnabled(False)
        
        self.act_zoomin.setEnabled(False)
        self.act_zoomout.setEnabled(False)
        
        self.act_togglewhitespace.setEnabled(False)

        self.act_next_bookmark.setEnabled(False)
        self.act_previous_bookmark.setEnabled(False)
        self.act_delete_bookmarks.setEnabled(False)

        self.deal_with_saveall_act()
        


    def update_actions(self):
        print('Updating actions')
        text_edit = self.get_active_textedit()
        text_edit.setFocus()
        self.setWindowTitle(text_edit.currentfile+' - '+__appname__)
        
        self.act_save.setEnabled(text_edit.isModified()) 
        self.act_saveas.setEnabled(True) 

        self.act_cut.setEnabled(False)
        self.act_copy.setEnabled(False)
        self.act_paste.setEnabled(self.clipboard_mimedata().hasText()) 

        self.act_undo.setEnabled(text_edit.isUndoAvailable())
        self.act_redo.setEnabled(text_edit.isRedoAvailable())
        
        self.act_closefile.setEnabled(True)
        self.act_closeallfiles.setEnabled(True)

        self.act_split_h_screen.setEnabled(True)
        self.act_split_v_screen.setEnabled(True)

        self.act_zoomin.setEnabled(True)
        self.act_zoomout.setEnabled(True)
        
        self.act_togglewhitespace.setEnabled(True)

        active_textedit = self.get_active_textedit()
        if len(active_textedit.bookmarks.keys()) == 0:
            self.act_next_bookmark.setEnabled(False)
            self.act_previous_bookmark.setEnabled(False)
            self.act_delete_bookmarks.setEnabled(False)
        else:
            self.act_next_bookmark.setEnabled(True)
            self.act_previous_bookmark.setEnabled(True)
            self.act_delete_bookmarks.setEnabled(True)
        
        self.deal_with_saveall_act()

###############################################################################
## Drag and Drops
###############################################################################


    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/uri-list'):
            event.acceptProposedAction()

    
    
    def dropEvent(self, event):
        if event.mimeData().hasFormat('text/uri-list'):
            urls = event.mimeData().urls()
            for filename in urls:
                checkfile = self.isfile_open(str(filename.toLocalFile()))
                if checkfile[0]:
                    checkfile[1].setCurrentIndex(checkfile[2])
                else:
                    self.load_file(str(filename.toLocalFile()))


###############################################################################
## Get active editor widgets
###############################################################################
   
       
    def get_active_combobox(self):
        combobox = self.active_editor.findChild(QtGui.QWidget, 'EditorComboBox')
        return combobox

        
    def get_active_textedit(self):
        index = self.get_active_stackwidget().currentIndex()
        active_text_edit = self.get_active_stackwidget().widget(index)
        return active_text_edit


    def get_active_stackwidget(self):
        active_stack = self.active_editor.findChild(QtGui.QStackedWidget,
                                                    'EditorStackWidget')
        return active_stack   
       
       
    def show_laststack(self):
        active_stack = self.get_active_stackwidget()
        nstacks = active_stack.count() - 1
        active_stack.setCurrentIndex(nstacks)

 
###############################################################################
## Edits
###############################################################################
      
      
    def edit_cut(self):
        self.get_active_textedit().cut()
        
        
    def edit_copy(self):
        self.get_active_textedit().copy()
        
        
    def edit_paste(self):
        if self.active_editor == None:
            self.newfile_n += 1
            newfilename = 'new '+str(self.newfile_n)

            editor = lib.editor_widget.EditorWidget(\
                                newfilename, '', True, self.splitter)
            self.active_editor = editor
            self.activeEditorChanged.emit('newEditorByPasteClipboard')
        self.get_active_textedit().paste()
        self.get_active_textedit().lines_changed()


    def edit_undo(self):
        self.get_active_textedit().undo()
        
        
    def edit_redo(self):
        self.get_active_textedit().redo()
        
        
###############################################################################
## Manipulate text edit
###############################################################################
             
        
    def toggle_whitespace(self):
        if self.active_editor != None:
            is_visible = self.get_active_textedit().whitespaceVisibility()
            if is_visible:
                self.get_active_textedit().setWhitespaceVisibility(False)
            else:
                self.get_active_textedit().setWhitespaceVisibility(True)



    def comment_code(self):
        if self.active_editor != None:
            self.get_active_textedit().comment()



    def uncomment_code(self):
        if self.active_editor != None:
            self.get_active_textedit().uncomment()

    
    
    def stream_comment_code(self):
        if self.active_editor != None:
            self.get_active_textedit().stream_comment()
        
        
###############################################################################
## Close files
###############################################################################
         
  
    def close_file(self):
        active_stack = self.get_active_stackwidget()
        active_textedit = self.get_active_textedit()
        curfile = active_textedit.currentfile

        if active_textedit.isModified():
            ret = QtGui.QMessageBox.warning(self, 
                    "Save file "+curfile,
                    "The document "+curfile+" has been modified.\n"
                    "Do you want to save your changes?",
                    QtGui.QMessageBox.Save | 
                    QtGui.QMessageBox.Discard |
                    QtGui.QMessageBox.Cancel)
            if ret == QtGui.QMessageBox.Save:
                self.save()
            elif ret == QtGui.QMessageBox.Cancel:
                return False
            elif ret == QtGui.QMessageBox.Discard:
                pass
            
        print('Closing file',curfile)
        active_textedit.hide()
        active_stack.removeWidget(active_textedit)
        active_textedit.deleteLater()



    def close_allfiles(self):
        print('Close all files')
        text_edits = self.findChildren(QsciScintilla,'TextEdit')
        for text_edit in text_edits:
            stack = text_edit.parent()
            stack.setCurrentIndex(stack.indexOf(text_edit))
            
            self.active_editor = text_edit.parent().parent()
            self.activeEditorChanged.emit('closingFile')
            ret = self.close_file()
            if ret == False:
                print('Cancelled close all files')
                return
            
        self.active_editor = None
        self.update_actions_noeditors()
          
        
        
    def closeEvent(self, event):
        text_edits = self.findChildren(QsciScintilla,'TextEdit')
        if len(text_edits) == 0:
            self.write_settings_app_exit()
            print('Exiting application')
            event.accept()
        elif len(text_edits) > 0:
            ret = True
            
            for text_edit in text_edits:
                stack = text_edit.parent()
                stack.setCurrentIndex(stack.indexOf(text_edit))
                self.active_editor = text_edit.parent().parent()
                self.activeEditorChanged.emit('closingFile')
                
                ret = self.close_file()
                if ret == False:
                    event.ignore()
                    print('Cancelled exit application')
                    return
                
            print('Exiting application')
            self.write_settings_app_exit()
            event.accept()
            
          
###############################################################################
## Saves
###############################################################################
    
      
    def save(self):
        print('Save')     
        curfile = self.get_active_textedit().currentfile
        isnewfile = self.get_active_textedit().isnewfile
        if isnewfile:
            self.save_as()
        else:
            self.save_file(curfile)
            


    def save_as(self):
        lastdir = self.prefs.get_setting('Recent/LastDirVisited', '/')
        curfile = self.get_active_textedit().currentfile
        print('Save as',curfile)
        fileurl = QtGui.QFileDialog.getSaveFileName(self,
                                 self.tr("Save as : "+curfile),
                                 lastdir.toString())
        if fileurl:
            self.save_file(fileurl)
            self.write_lastdir_visited(fileurl)



    def save_all(self):
        print('Save all')
        text_edits = self.findChildren(QsciScintilla,'TextEdit')
        for text_edit in text_edits:

            stack = text_edit.parent()
            stack.setCurrentIndex(stack.indexOf(text_edit))
            
            if text_edit.isModified():
                text = text_edit.text()
                if text_edit.isnewfile:
                    fileurl = QtGui.QFileDialog.getSaveFileName(self,
                                         self.tr("Save : "+text_edit.currentfile),
                                         self.lastdir)
                    if fileurl:
                        self.save_file(fileurl, text, text_edit)
                else:
                    fileurl = text_edit.currentfile
                    self.save_file(fileurl, text, text_edit)



    def save_file(self, fileurl, text=False, text_edit=False):
        '''Save file'''
        file = QtCore.QFile(fileurl)
        if not file.open(QtCore.QFile.WriteOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Application",
                    "Cannot write file %s:\n%s." % (fileurl, file.errorString()))
            return False
        
        outfile = QtCore.QTextStream(file)
        QtGui.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        if text:
            # Happens on save all
            outfile << text
        else:
            # Happens on saving individual files
            outfile << self.get_active_textedit().text()
        QtGui.QApplication.restoreOverrideCursor()
        
        self.update_save_status(fileurl, text_edit)
        self.refresh_recent_files(fileurl)
        self.statusBar().showMessage("File saved : "+fileurl, 2000)
        print('Saving file',  fileurl)
        return True
       


    def update_save_status(self, fileurl, text_edit):
        if text_edit:
            text_edit_2_save = text_edit
            comboBox = text_edit_2_save.parent().parent().findChild(\
                                        QtGui.QWidget,'EditorComboBox')
        else:  
            text_edit_2_save = self.get_active_textedit()
            comboBox = self.get_active_combobox()
            
        text_edit_2_save.currentfile = fileurl
        text_edit_2_save.setModified(False)
        text_edit_2_save.isnewfile = False
        
        # Todo : Check if there is a need to reapply the lexer
        text_edit_2_save.set_lexer()
        text_edit_2_save.set_style_and_config()
        text_edit_2_save.lines_changed()
        
        index = comboBox.currentIndex()
        comboBox.setItemText(index, self.get_filename(fileurl))
        self.act_save.setEnabled(False)
        self.deal_with_saveall_act()



    def deal_with_saveall_act(self):
        text_edits = self.findChildren(QsciScintilla,'TextEdit')
        stats = []
        for text_edit in text_edits:
            stats.append(text_edit.isModified())
        if True in stats:
            self.act_saveall.setEnabled(True)
        else:
            self.act_saveall.setEnabled(False)


###############################################################################
## Docks
###############################################################################


    def show_leftdock(self):
        self.show_dock('dockWidgetLeft')
        
        
    def show_bottomdock(self):
        self.show_dock('dockWidgetBottom')
        
        
    def show_rightdock(self):
        self.show_dock('dockWidgetRight')  
        
        
    def show_dock(self,which):
        dock = self.findChild(QtGui.QDockWidget, which)
        if dock.isHidden():
            dock.show()
        else:
            dock.hide()


###############################################################################
## Zoom text
###############################################################################


    def zoom_in(self):
        if self.active_editor != None:
            self.get_active_textedit().zoomIn()

    def zoom_out(self):
        if self.active_editor != None:
            self.get_active_textedit().zoomOut()


###############################################################################
## New file, open file, load file
###############################################################################
      
      
    def new_file(self):
        '''Create new file. '''
        self.newfile_n += 1
        newfilename = 'new '+str(self.newfile_n)

        if self.active_editor == None:
            editor = lib.editor_widget.EditorWidget(\
                                            newfilename,
                                            '',
                                            True,
                                            self.splitter)
            self.active_editor = editor
            self.activeEditorChanged.emit('newEditorByLoadFile')
        else:
            newtab = lib.text_edit.TextEdit(True, newfilename, '')
            active_stack = self.get_active_stackwidget()
            active_stack.addWidget(newtab)
            
            combobox = self.get_active_combobox()
            combobox.addItem(newfilename)
        self.show_laststack()
        self.update_actions()



    def write_lastdir_visited(self, fileurl):
        filedir = QtCore.QFileInfo(fileurl).absolutePath()
        self.prefs.set_setting('Recent/LastDirVisited', filedir)
        self.prefs.settings.sync()



    def open_file(self):
        '''Show the open file dialog.'''
        lastdir = self.prefs.get_setting('Recent/LastDirVisited', '/')
        fileurl = QtGui.QFileDialog.getOpenFileName(self,
                                                self.tr("Open file"),
                                                lastdir.toString())
        if fileurl:
            checkfile = self.isfile_open(fileurl)
            if checkfile[0]:
                checkfile[1].setCurrentIndex(checkfile[2])
                print('File is already opened') 
            else:
                self.load_file(fileurl)
                self.write_lastdir_visited(fileurl)



    def load_file(self, fileurl):
        '''Load the file contents into the editor'''

        file = QtCore.QFile(fileurl)
        if not file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
            QtGui.QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (fileurl, file.errorString()))
            return
        
        inf = QtCore.QTextStream(file)

        # If there is no editor create a new one, signal its creation and return
        if self.active_editor == None:
            print('Creating new editor and loading file', fileurl)
            editor = lib.editor_widget.EditorWidget(fileurl, 
                                                    inf.readAll(),
                                                    False,
                                                    self.splitter)
            self.active_editor = editor
            self.activeEditorChanged.emit('newEditorByLoadFile')
            self.refresh_recent_files(fileurl)
            self.get_active_textedit().lines_changed()
            return

        # If the text edit is virgin delete it
        if self.isactive_textedit_virgin():
            active_text_edit = self.get_active_textedit()
            active_text_edit.hide()
            active_text_edit.deleteLater()

        combobox = self.get_active_combobox()
        combobox.addItem(self.get_filename(fileurl))
        
        print('Deleting active text edit and loading file',fileurl)
        active_stack = self.get_active_stackwidget()
        newtab = lib.text_edit.TextEdit(False, fileurl, inf.readAll())
        active_stack.addWidget(newtab)
        self.refresh_recent_files(fileurl)
        self.show_laststack()
        self.get_active_textedit().lines_changed()
        


    def refresh_recent_files(self, fileurl):
        '''Limit recent files number, append latest file and
        change the text of the action to the file url. Also
        hide actions that do not have file to open.
        '''
        if len(self.recent_files) >= self.max_recent_files:
            if fileurl not in self.recent_files:
                self.recent_files.pop(0)
                self.recent_files.append(fileurl)

        for act in self.menu_recentfiles.actions():
            i = act.data().toInt()[0]
            if self.recent_files[i] != '':
                act.setText(str(i)+' - '+self.recent_files[i]) 
                act.setVisible(True)
            elif self.recent_files[i] == '':
                act.setVisible(False)
            


    def recent_file_load(self, i):
        '''Load recent file'''
        fileurl = self.recent_files[i]
        checkfile = self.isfile_open(fileurl)
        if checkfile[0]:
            checkfile[1].setCurrentIndex(checkfile[2])
            print('File is already opened', fileurl) 
        else:
            self.load_file(fileurl)
        


    def callback_recent_file_load(self, i):
        ''' This is the function that is applied to each recent file menu.
        Its purpose is to defeat the scope of python lambda functions'''
        return lambda: self.recent_file_load(i)


###############################################################################
## Navigate bookmarks
###############################################################################
  
  
    def next_bookmark(self):
        if self.active_editor == None:
            return
        active_textedit = self.get_active_textedit()
        active_textedit.next_bookmark()


    def previous_bookmark(self):
        if self.active_editor == None:
            return
        active_textedit = self.get_active_textedit()
        active_textedit.previous_bookmark()
        
        
    def delete_bookmarks(self):
        if self.active_editor == None:
            return
        active_textedit = self.get_active_textedit()
        active_textedit.delete_bookmarks()
        
 
###############################################################################
## Misc
###############################################################################


    def fold_all(self):
        if self.active_editor == None:
            return
        active_textedit = self.get_active_textedit()
        active_textedit.foldAll(True)  
        
          
###############################################################################
## Create menus
###############################################################################
    
     
    def create_menus(self):
        '''Create the menus for the application'''
        self.filemenu = self.menuBar().addMenu(self.tr("&File"))
        self.filemenu.addAction(self.act_newfile)
        self.filemenu.addAction(self.act_openfile)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.act_save)
        self.filemenu.addAction(self.act_saveall)
        self.filemenu.addAction(self.act_saveas)
        self.filemenu.addSeparator()
        
        # Recent files menu
        self.menu_recentfiles = self.filemenu.addMenu(self.tr("&Recent Files"))
        for i in range(len(self.recent_files)):
            act = QtGui.QAction(self.recent_files[i], self)
            act.setData(i)   
            self.menu_recentfiles.addAction(act)

            receiver = self.callback_recent_file_load(i)
            act.triggered.connect(receiver)
            
            if self.recent_files[i] == '':
                act.setVisible(False)

        self.filemenu.addAction(self.act_closefile)
        self.filemenu.addAction(self.act_closeallfiles)
        self.filemenu.addSeparator()
        self.filemenu.addAction(self.act_exit)

        self.editmenu = self.menuBar().addMenu(self.tr("&Edit"))
        self.editmenu.addAction(self.act_undo)
        self.editmenu.addAction(self.act_redo)
        self.editmenu.addSeparator()
        self.editmenu.addAction(self.act_cut)
        self.editmenu.addAction(self.act_copy)
        self.editmenu.addAction(self.act_paste)

        self.findmenu = self.menuBar().addMenu(self.tr("&Find"))
        self.findmenu.addAction(self.act_foldall)

        self.sourcemenu = self.menuBar().addMenu(self.tr("&Source"))
        self.sourcemenu.addAction(self.act_commentcode)
        self.sourcemenu.addAction(self.act_uncommentcode)
        self.sourcemenu.addAction(self.act_streamcommentcode)
        self.sourcemenu.addAction(self.act_togglewhitespace)
        
        self.windowmenu = self.menuBar().addMenu(self.tr("&Window"))
        self.windowmenu.addAction(self.act_split_v_screen)
        self.windowmenu.addAction(self.act_split_h_screen)
        self.windowmenu.addSeparator()
        self.windowmenu.addAction(self.act_show_dockleft)
        self.windowmenu.addAction(self.act_show_dockbottom)
        self.windowmenu.addAction(self.act_show_dockright)
        self.windowmenu.addSeparator()
        self.windowmenu.addAction(self.act_zoomin)
        self.windowmenu.addAction(self.act_zoomout)
        
        self.helpmenu = self.menuBar().addMenu(self.tr("&Help"))
        self.helpmenu.addAction(self.act_about)
        self.helpmenu.addAction(self.act_aboutqt)
        
        
###############################################################################
## Create toolbars
###############################################################################
    

    def create_toolbars(self):
        self.filetoolbar = self.addToolBar(self.tr("File"))
        self.filetoolbar.setObjectName('MainToolbar')
        self.filetoolbar.setIconSize(QtCore.QSize(20, 20))
        self.filetoolbar.addAction(self.act_newfile)
        self.filetoolbar.addAction(self.act_openfile)
        
        self.savetoolbar = self.addToolBar(self.tr("Save"))
        self.savetoolbar.setObjectName('SaveToolbar')
        self.savetoolbar.setIconSize(QtCore.QSize(20,20))
        self.savetoolbar.addAction(self.act_save)
        self.savetoolbar.addAction(self.act_saveall)
        
        self.edittoolbar = self.addToolBar(self.tr("Edit"))
        self.edittoolbar.setObjectName('EditToolbar')
        self.edittoolbar.setIconSize(QtCore.QSize(20, 20))
        self.edittoolbar.addAction(self.act_cut)
        self.edittoolbar.addAction(self.act_copy)
        self.edittoolbar.addAction(self.act_paste)
        self.edittoolbar.addSeparator()
        self.edittoolbar.addAction(self.act_undo)
        self.edittoolbar.addAction(self.act_redo)

        self.windowtoolbar = self.addToolBar(self.tr("Window"))
        self.windowtoolbar.setObjectName('WindowToolbar')
        self.windowtoolbar.setIconSize(QtCore.QSize(20,20))
        self.windowtoolbar.addAction(self.act_split_h_screen)
        self.windowtoolbar.addAction(self.act_split_v_screen)
        self.windowtoolbar.addSeparator()
        self.windowtoolbar.addAction(self.act_show_dockleft)
        self.windowtoolbar.addAction(self.act_show_dockbottom)
        self.windowtoolbar.addAction(self.act_show_dockright)
        self.windowtoolbar.addSeparator()
        self.windowtoolbar.addAction(self.act_zoomin)
        self.windowtoolbar.addAction(self.act_zoomout)

        self.bookmarkstoolbar = self.addToolBar(self.tr("Bookmarks"))
        self.bookmarkstoolbar.setObjectName('BookmarksToolbar')
        self.bookmarkstoolbar.setIconSize(QtCore.QSize(20,20))
        self.bookmarkstoolbar.addAction(self.act_previous_bookmark)
        self.bookmarkstoolbar.addAction(self.act_next_bookmark)
        self.bookmarkstoolbar.addAction(self.act_delete_bookmarks)
        
        
###############################################################################
## Create actions
###############################################################################


    def create_actions(self):
        iconsdir = os.path.join(self.curdir, 'res', 'graphics')
        
        self.act_newfile = QtGui.QAction(self.tr("&New"), self)
        self.act_newfile.setShortcut(self.tr("Ctrl+N"))
        self.act_newfile.setIcon(QtGui.QIcon(":/png/document-new.png"))
        self.act_newfile.setStatusTip(self.tr("Create a new file"))
        self.act_newfile.triggered.connect(self.new_file)

        self.act_openfile = QtGui.QAction(self.tr("&Open..."), self)
        self.act_openfile.setIcon(QtGui.QIcon(":/png/document-open.png"))
        self.act_openfile.setShortcut(self.tr("Ctrl+O"))
        self.act_openfile.setStatusTip(self.tr("Open an existing file"))
        self.act_openfile.triggered.connect(self.open_file)

        # save
        self.act_save = QtGui.QAction(self.tr("&Save"), self)
        self.act_save.setIcon(QtGui.QIcon(":/png/document-save.png"))
        self.act_save.setShortcut(self.tr("Ctrl+S"))
        self.act_save.setStatusTip(self.tr("Save the document to disk"))
        self.act_save.triggered.connect(self.save)

        # Save all
        self.act_saveall = QtGui.QAction(self.tr("&Save all"), self)
        self.act_saveall.setIcon(QtGui.QIcon(":/png/document-save-all.png"))
        self.act_saveall.setShortcut(self.tr("Shift+Ctrl+S"))
        self.act_saveall.setStatusTip(self.tr("Save the document to disk"))
        self.act_saveall.triggered.connect(self.save_all)

        # Save as
        self.act_saveas = QtGui.QAction(self.tr("Save &As..."), self)
        self.act_saveas.setIcon(QtGui.QIcon(":/png/document-save-as.png"))
        self.act_saveas.setStatusTip(self.tr("Save the document under a new name"))
        self.act_saveas.triggered.connect(self.save_as)

        # Close 
        self.act_closefile = QtGui.QAction(self.tr("&Close"), self)
        self.act_closefile.setShortcut(self.tr("Ctrl+W"))
        self.act_closefile.setStatusTip(self.tr("Close current file"))
        self.act_closefile.triggered.connect(self.close_file)

        self.act_closeallfiles = QtGui.QAction(self.tr("C&lose all"), self)
        self.act_closeallfiles.setShortcut(self.tr("Shift+Ctrl+W"))
        self.act_closeallfiles.setStatusTip(self.tr("Close all files"))
        self.act_closeallfiles.triggered.connect(self.close_allfiles)

        self.act_exit = QtGui.QAction(self.tr("E&xit"), self)
        self.act_exit.setShortcut(self.tr("Ctrl+Q"))
        self.act_exit.setStatusTip(self.tr("Exit the application"))
        self.act_exit.triggered.connect(self.close)

        # Edit
        self.act_cut = QtGui.QAction(self.tr("Cu&t"), self)
        self.act_cut.setIcon(QtGui.QIcon(":/png/edit-cut.png"))
        self.act_cut.setShortcut(self.tr("Ctrl+X"))
        self.act_cut.setStatusTip(self.tr("Cut the current selection's contents to the clipboard"))
        self.act_cut.triggered.connect(self.edit_cut)

        self.act_copy = QtGui.QAction(self.tr("&Copy"), self)
        self.act_copy.setIcon(QtGui.QIcon(":/png/edit-copy.png"))
        self.act_copy.setShortcut(self.tr("Ctrl+C"))
        self.act_copy.setStatusTip(self.tr("Copy the current selection's contents to the clipboard"))
        self.act_copy.triggered.connect(self.edit_copy)

        self.act_paste = QtGui.QAction(self.tr("&Paste"), self)
        self.act_paste.setIcon(QtGui.QIcon(":/png/edit-paste.png"))
        self.act_paste.setShortcut(self.tr("Ctrl+V"))
        self.act_paste.setStatusTip(self.tr("Paste the clipboard's contents into the current selection"))
        self.act_paste.triggered.connect(self.edit_paste)

        self.act_undo = QtGui.QAction(self.tr("&Undo"), self)
        self.act_undo.setIcon(QtGui.QIcon(":/png/edit-undo.png"))
        self.act_undo.setShortcut(self.tr("Ctrl+Z"))
        self.act_undo.setStatusTip(self.tr("Undo modifications to document"))
        self.act_undo.triggered.connect(self.edit_undo)

        self.act_redo = QtGui.QAction(self.tr("&Redo"), self)
        self.act_redo.setIcon(QtGui.QIcon(":/png/edit-redo.png"))
        self.act_redo.setShortcut(self.tr("Ctrl+Y"))
        self.act_redo.setStatusTip(self.tr("Redo modifications to document"))
        self.act_redo.triggered.connect(self.edit_redo)

        # Commenting code
        self.act_commentcode = QtGui.QAction(self.tr("&Comment"), self)
        self.act_commentcode.setShortcut(self.tr("Ctrl+3"))
        self.act_commentcode.setStatusTip(self.tr("Comment code"))
        self.act_commentcode.triggered.connect(self.comment_code)
        
        self.act_uncommentcode = QtGui.QAction(self.tr("&UnComment"), self)
        self.act_uncommentcode.setShortcut(self.tr("Shift+Ctrl+3"))
        self.act_uncommentcode.setStatusTip(self.tr("UnComment code"))
        self.act_uncommentcode.triggered.connect(self.uncomment_code)

        self.act_streamcommentcode = QtGui.QAction(self.tr("&Stream comment"), self)
        self.act_streamcommentcode.setShortcut(self.tr("Shift+Ctrl+3"))
        self.act_streamcommentcode.setStatusTip(self.tr("Stream comment code"))
        self.act_streamcommentcode.triggered.connect(self.stream_comment_code)

        # Toggle whitespace
        self.act_togglewhitespace = QtGui.QAction(self.tr("&Toggle whitespace"), self)
        self.act_togglewhitespace.setShortcut(self.tr("Shift+Ctrl+3"))
        self.act_togglewhitespace.setStatusTip(self.tr("Toggle whitespace"))
        self.act_togglewhitespace.triggered.connect(self.toggle_whitespace)

        # About
        self.act_about = QtGui.QAction(self.tr("&About"), self)
        self.act_about.setStatusTip(self.tr("Show the application's About box"))
        self.act_about.triggered.connect(self.about)

        self.act_aboutqt = QtGui.QAction(self.tr("About &Qt"), self)
        self.act_aboutqt.setStatusTip(self.tr("Show the Qt library's About box"))
        self.act_aboutqt.triggered.connect(QtGui.qApp.aboutQt)

        # Split screen
        self.act_split_h_screen = QtGui.QAction(self.tr("&Split Screen Horizontal"), self)
        self.act_split_h_screen.setIcon(QtGui.QIcon(":/png/split-h-screen.png"))
        self.act_split_h_screen.setShortcut(self.tr("Shift+Ctrl+H"))
        self.act_split_h_screen.setStatusTip(self.tr("Open an horizontal split"))
        self.act_split_h_screen.triggered.connect(self.split_screen.splitHScreen)

        self.act_split_v_screen = QtGui.QAction(self.tr("&Split Screen Vertical"), self)
        self.act_split_v_screen.setIcon(QtGui.QIcon(":/png/split-v-screen.png"))
        self.act_split_v_screen.setShortcut(self.tr("Shift+Ctrl+V"))
        self.act_split_v_screen.setStatusTip(self.tr("Open a vertical split"))
        self.act_split_v_screen.triggered.connect(self.split_screen.splitVScreen)

        # Docks
        self.act_show_dockleft = QtGui.QAction(self.tr("&Show left dock"), self)
        self.act_show_dockleft.setIcon(QtGui.QIcon(":/png/show-left-dock.png"))
        self.act_show_dockleft.setShortcut(self.tr("Ctrl+Shift+L"))
        self.act_show_dockleft.setStatusTip(self.tr("Show left dock"))
        self.act_show_dockleft.triggered.connect(self.show_leftdock)

        self.act_show_dockright = QtGui.QAction(self.tr("&Show right dock"), self)
        self.act_show_dockright.setIcon(QtGui.QIcon(":/png/show-right-dock.png"))
        self.act_show_dockright.setShortcut(self.tr("Ctrl+Shift+R"))
        self.act_show_dockright.setStatusTip(self.tr("Show right dock"))
        self.act_show_dockright.triggered.connect(self.show_rightdock)

        self.act_show_dockbottom = QtGui.QAction(self.tr("&Show bottom dock"), self)
        self.act_show_dockbottom.setIcon(QtGui.QIcon(":/png/show-bottom-dock.png"))
        self.act_show_dockbottom.setShortcut(self.tr("Ctrl+Shift+B"))
        self.act_show_dockbottom.setStatusTip(self.tr("Show bottom dock"))
        self.act_show_dockbottom.triggered.connect(self.show_bottomdock)

        # Zoom
        self.act_zoomin = QtGui.QAction(self.tr("&Zoom in"), self)
        self.act_zoomin.setIcon(QtGui.QIcon(":/png/zoom-in.png"))
        self.act_zoomin.setShortcut(self.tr("Ctrl++"))
        self.act_zoomin.setStatusTip(self.tr("Zoom in"))
        self.act_zoomin.triggered.connect(self.zoom_in)

        self.act_zoomout = QtGui.QAction(self.tr("&Zoom out"), self)
        self.act_zoomout.setIcon(QtGui.QIcon(":/png/zoom-out.png"))
        self.act_zoomout.setShortcut(self.tr("Ctrl+-"))
        self.act_zoomout.setStatusTip(self.tr("Zoom out"))
        self.act_zoomout.triggered.connect(self.zoom_out)

        # Fold all
        self.act_foldall = QtGui.QAction(self.tr("&Toggle Fold all"), self)
        self.act_foldall.setStatusTip(self.tr("Fold all"))
        self.act_foldall.triggered.connect(self.fold_all)
        
        # Bookmarks
        self.act_next_bookmark = QtGui.QAction(self.tr("&Next bookmark"), self)
        self.act_next_bookmark.setIcon(QtGui.QIcon(":/png/bookmark-next.png"))
        self.act_next_bookmark.setShortcut(self.tr("Ctrl+Alt+B"))
        self.act_next_bookmark.setStatusTip(self.tr("Next bookmark"))
        self.act_next_bookmark.triggered.connect(self.next_bookmark)

        self.act_previous_bookmark = QtGui.QAction(self.tr("&Previous bookmark"), self)
        self.act_previous_bookmark.setIcon(QtGui.QIcon(":/png/bookmark-previous.png"))
        self.act_previous_bookmark.setShortcut(self.tr("Ctrl+Alt+V"))
        self.act_previous_bookmark.setStatusTip(self.tr("Previous bookmark"))
        self.act_previous_bookmark.triggered.connect(self.previous_bookmark)

        self.act_delete_bookmarks = QtGui.QAction(self.tr("&Delete bookmarks"), self)
        self.act_delete_bookmarks.setIcon(QtGui.QIcon(":/png/bookmark-delete-all.png"))
        self.act_delete_bookmarks.setShortcut(self.tr("Ctrl+Alt+D"))
        self.act_delete_bookmarks.setStatusTip(self.tr("Delete bookmarks"))
        self.act_delete_bookmarks.triggered.connect(self.delete_bookmarks)
        
        # Enable or disable actions
        self.act_cut.setEnabled(False)
        self.act_copy.setEnabled(False)
        self.act_paste.setEnabled(self.clipboard_mimedata().hasText()) 

        self.act_undo.setEnabled(False)
        self.act_redo.setEnabled(False)
        
        self.act_save.setEnabled(False)
        self.act_saveas.setEnabled(False)
        self.act_saveall.setEnabled(False)
        
        self.act_closefile.setEnabled(False)
        self.act_closeallfiles.setEnabled(False)

        self.act_commentcode.setEnabled(False)
        self.act_uncommentcode.setEnabled(False)
        self.act_streamcommentcode.setEnabled(False)

        self.act_split_h_screen.setEnabled(False)
        self.act_split_v_screen.setEnabled(False)

        self.act_zoomin.setEnabled(False)
        self.act_zoomout.setEnabled(False)
        
        self.act_next_bookmark.setEnabled(False)
        self.act_previous_bookmark.setEnabled(False)
        self.act_delete_bookmarks.setEnabled(False)
        
        self.act_togglewhitespace.setEnabled(False)
        
        
###############################################################################
## Common
###############################################################################
        
     
    def isactive_textedit_virgin(self):
        is_virgin = False 
        textedit = self.get_active_textedit() 
        if textedit.isnewfile and textedit.nedits == 0:
            is_virgin = True
        return is_virgin
    
      
    def get_filename(self, fullurl):
        '''Get filename from fullurl'''
        return QtCore.QFileInfo(fullurl).fileName()
     

    def get_lastdir_visited(self):
        self.lastdir = "/media/myhouse/temp"


    def isfile_open(self, filename):
        '''This checks if there is a text edit with filename.
        This is to avoid opening a file twice.
        '''
        out = [False, None, 0]
        textedits = self.findChildren(QsciScintilla, 'TextEdit')
        for textedit in textedits:
            if textedit.currentfile == filename: 
                out[0] = True
                out[1] = textedit.parent()
                out[2] = textedit.parent().indexOf(textedit)
        return out


    def get_xml(self, filename):
        try:
            tree = ET.parse(filename)
            print ("Sucess parsing xml file: ", filename)
            return tree
        except Exception as e:
            print ("Error could not get xml file: ", e)



    def app_dir(self):
        '''Get script directory.'''        
        app_path = os.path.abspath(os.path.dirname(__file__))
        return app_path 



    def about(self):
        QtGui.QMessageBox.about(self, self.tr("About Application"),
            self.tr("The <b>Application</b> example demonstrates how to "
                    "write modern GUI applications using Qt, with a menu bar, "
                    "toolbars, and a status bar."))
        


    def clipboard_mimedata(self):
        clipboard = QtGui.QApplication.clipboard()
        mimedata = clipboard.mimeData()
        return mimedata



if __name__ == "__main__":
    print('Welcome to Debulhator')
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("Debulhator")
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())



