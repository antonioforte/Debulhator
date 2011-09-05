#!/usr/bin/env python
from PyQt4 import QtCore, Qsci
from PyQt4 import QtGui
from PyQt4.Qsci import QsciScintilla
import os

import get_lexer
import preferences
import common

'''Thanks to eric4'''

class TextEdit(QsciScintilla):
    '''TextEdit control'''
    
    def __init__(self, isnewfile, filename, text, parent=None):
        QsciScintilla.__init__(self, parent)
        print('Creating TextEdit', isnewfile, filename)
        
        self.setObjectName('TextEdit')
        self.currentfile = filename
        self.isnewfile = isnewfile
        self.nedits = 0
        self.bookmarks = {}
        self.zen = common.Common()

        self.bookmark = self.markerDefine(QtGui.QPixmap(':/png/bookmark.png'))
        self.prefs = preferences.Preferences()
        self.setIndentationsUseTabs(False)
        self.setAutoCompletionThreshold(2)

        self.copyAvailable.connect(self.enable_copy)
        self.textChanged.connect(self.text_changed)

        self.setText(text)
        self.setModified(False)
        
        self.lexer_ = None
        self.set_lexer()
        self.set_style_and_config()

        self.marginClicked.connect(self.on_margin_clicked)
        self.modificationChanged.connect(self.document_was_modified)
        self.linesChanged.connect(self.lines_changed)


    def lines_changed(self):
        '''Adjust margin numbers width'''
        fontmetrics = QtGui.QFontMetrics(self.font())
        numberlines = str(self.lines())+'00'

        if len(numberlines) != 1:
            width = fontmetrics.width(numberlines) + self.prefs.get_setting(\
                                        'MarginLineNumbersWidth', 1).toInt()[0]
            self.setMarginWidth(0, width)
                


    def document_was_modified(self, state):
        '''Signal modifications of TextEdit'''
        mainwindow = self.get_mainwindow()
        comboBox = self.parent().parent().findChild(QtGui.QWidget, 'EditorComboBox')
        index = comboBox.currentIndex()
        filename = QtCore.QFileInfo(self.currentfile).fileName()
        
        if self.isModified():
            comboBox.setItemText(index, '* ' + filename)
            self.nedits += 1
        else:
            comboBox.setItemText(index, filename)
            
        mainwindow.update_actions()
        print('TextEdit isModified()', state)
        
        
        
    def set_lexer(self, language=None):
        '''Apply the lexer to the TextEdit'''
        lexer = get_lexer.GetLexer(self.currentfile, language, self)
        _lexer = lexer.get_lexer()
        
        if _lexer != None:
            self.setLexer(_lexer)
            self.lexer_ = _lexer
            print('Language is supported', self.lexer())
        elif _lexer == None:
            print('Language not supported or is plain text')

        self.deal_comment_actions()



    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backtab:
            self.unindent_()
        elif event.key() == QtCore.Qt.Key_Tab:
            self.indent_()
        else:
            return QsciScintilla.keyPressEvent(self,event)



    def wheelEvent(self, event):
        zoom_level = self.SendScintilla(QsciScintilla.SCI_GETZOOM)                        
        if event.modifiers() == QtCore.Qt.ControlModifier:
            delta = event.delta()
            if delta < 0:
                if zoom_level > -10:
                    self.zoomOut()
                    self.setMarginWidth(0, self.marginWidth(0)-2)
            elif delta > 0:
                if zoom_level < 20:
                    self.zoomIn()
                    self.setMarginWidth(0, self.marginWidth(0)+2)
            return
        return QsciScintilla.wheelEvent(self, event)


   
    def enable_copy(self, yes):
        mainwindow = self.get_mainwindow()
        mainwindow.act_copy.setEnabled(yes)
        mainwindow.act_cut.setEnabled(yes)



    def text_changed(self):
        mainwindow = self.get_mainwindow()
        mainwindow.act_undo.setEnabled(self.isUndoAvailable())
        mainwindow.act_redo.setEnabled(self.isRedoAvailable())
                


    def set_style_and_config(self):
        globalstyles = self.prefs.global_styles
        config = {}
        
        # The default has no use
        for key in self.prefs.settings.allKeys():
            config[str(key)] = self.prefs.get_setting(key, None)

        # Default paper, and text color , only if there is no lexer
        self.setPaper(globalstyles['Default Style']['bgColor'])
        self.setColor(globalstyles['Default Style']['fgColor'])
        
        # Fonts
        font = QtGui.QFont()
        font.setFamily(globalstyles['Default Style']['fontName'])
        font.setPointSize(int(globalstyles['Default Style']['fontSize']))
        self.setFont(font)
        self.setMarginsFont(font)
        
        # Folding
        self.setFolding(self.get_fold_styles()[config['Editor/Folding'].toInt()[0]], 2)
        
        self.setFoldMarginColors(globalstyles['Fold']['fgColor'],
                                 globalstyles['Fold']['bgColor'])

        # Line numbers margin.
        fontmetrics = QtGui.QFontMetrics(font)
        self.setMarginWidth(0,
            fontmetrics.width("00") + config['Editor/MarginLineNumbersWidth'].toInt()[0])
        self.setMarginLineNumbers(0, config['Editor/MarginLineNumbers'].toBool())
        self.setMarginsBackgroundColor(globalstyles['Line number margin']['bgColor'])
        self.setMarginsForegroundColor(globalstyles['Line number margin']['fgColor'])

        # Indent guides
        self.setIndentationWidth(config['Editor/IndentWidth'].toInt()[0])
        self.setIndentationGuides(config['Editor/IndentationGuides'].toBool())
        self.setIndentationGuidesBackgroundColor(globalstyles['Indent guideline style']['bgColor'])
        self.setIndentationGuidesForegroundColor(globalstyles['Indent guideline style']['fgColor'])

        # Limit chars edge
        self.setEdgeMode(self.get_edge_modes()[config['Editor/EdgeMode'].toInt()[0]])
        self.setEdgeColumn(config['Editor/EdgeColumnChars'].toInt()[0])
        self.setEdgeColor(globalstyles['Edge colour']['fgColor'])

        # Brace matching
        self.setBraceMatching(config['Editor/BraceMatchMode'].toInt()[0])
        self.setMatchedBraceBackgroundColor(globalstyles['Brace highlight style']['bgColor'])
        self.setMatchedBraceForegroundColor(globalstyles['Brace highlight style']['fgColor'])
        self.setUnmatchedBraceBackgroundColor(globalstyles['Bad brace colour']['bgColor'])
        self.setUnmatchedBraceForegroundColor(globalstyles['Bad brace colour']['fgColor'])

        # Caret
        self.setCaretLineVisible(config['Editor/CaretLineVisible'].toBool())
        self.setCaretLineBackgroundColor(globalstyles['Current line background colour']['bgColor'])
        self.setCaretForegroundColor(globalstyles['Caret colour']['fgColor'])

        # Misc
        self.setTabWidth(config['Editor/TabWidth'].toInt()[0])
        self.setAutoIndent(config['Editor/AutoIndent'].toBool())

        # Markers
        self.setMarginSensitivity(1, True)



    def on_margin_clicked(self, nmargin, nline, modifiers):
        '''Show or hide markers on the editor margin'''
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.bookmark)
            if nline in self.bookmarks.keys():
                del self.bookmarks[nline]
        else:
            handle = self.markerAdd(nline, self.bookmark)
            self.bookmarks[nline] = [self.text(nline), handle]
      
        mainwindow = self.get_mainwindow()
        mainwindow.active_editor = self.parent().parent()
        mainwindow.activeEditorChanged.emit('clickedTextEdit')
        
            
    def next_bookmark(self):
        line, index = self.getCursorPosition()
        if line == self.lines()-1:
            line = 0
        else:
            line += 1
        bmline = self.markerFindNext(line, 1 << self.bookmark)
        if bmline < 0:
            bmline = self.markerFindNext(0, 8)
        if bmline >= 0:
            self.setCursorPosition(bmline, 0)
            self.ensureLineVisible(bmline)


    def previous_bookmark(self):
        line, index = self.getCursorPosition()
        if line == 0:
            line = self.lines()-1
        else:
            line -= 1
        bmline = self.markerFindPrevious(line, 1 << self.bookmark)
        if bmline < 0:
            bmline = self.markerFindPrevious(self.lines() - 1, 1 << self.bookmark)
        if bmline >= 0:
            self.setCursorPosition(bmline, 0)
            self.ensureLineVisible(bmline)
      
      
    def delete_bookmarks(self):
        for bookmark in self.bookmarks.keys():
            handle = self.bookmarks[bookmark][1]
            self.markerDeleteHandle(handle)
        self.bookmarks = {}
        self.get_mainwindow().update_actions()
        
      
    def mousePressEvent(self, e):
        '''Make the text edit parent the active editor'''
        mainwindow = self.get_mainwindow()
        mainwindow.active_editor = self.parent().parent()
        mainwindow.activeEditorChanged.emit('clickedTextEdit')
        return QsciScintilla.mousePressEvent(self, e)
    
    

    def get_mainwindow(self):
        tops = QtGui.QApplication.topLevelWidgets()
        mainwindow = None
        for top in tops:
            if top.objectName() == 'MainWindow':
                mainwindow = top
        return mainwindow
    
    
    def get_fold_styles(self):
        options = {
             0 : self.NoFoldStyle,
             1 : self.PlainFoldStyle,
             2 : self.CircledFoldStyle,
             3 : self.BoxedFoldStyle,
             4 : self.CircledTreeFoldStyle,
             6 : self.BoxedTreeFoldStyle
         }
        return options
    
    
    def get_edge_modes(self):
        options = {
             0 : self.EdgeNone,
             1 : self.EdgeLine,
             2 : self.EdgeBackground
         }
        return options
       
       
    def get_bracematch_mode(self):
        options = {
             0 : self.NoBraceMatch,
             1 : self.StrictBraceMatch,
             2 : self.SloppyBraceMatch    
         } 
        return options
        
    

############################################################################
## Indentation handling methods 
############################################################################


    def indent_(self):
        if self.hasSelectedText():
            self.__indentSelection(True)
        else:
            self.__indentLine(True)
        


    def unindent_(self):
        if self.hasSelectedText():
            self.__indentSelection(False)
        else:
            self.__indentLine(False)
        


    def __indentLine(self, indent = True):
        """If the flag is true, an indent operation is performed.
        Otherwise the current line is unindented.
        """
        line, index = self.getCursorPosition()
        self.beginUndoAction()
        if indent:
            self.indent(line)
        else:
            self.unindent(line)
        self.endUndoAction()
        if indent:
            self.setCursorPosition(line, index + self.indentationWidth())
        else:
            self.setCursorPosition(line, index - self.indentationWidth())
        
        
         
    def __indentSelection(self, indent = True):
        """If the flag is true, an indent operation is performed.
        Otherwise the current line is unindented.
        """
        if not self.hasSelectedText():
            return
        
        # get the selection
        lineFrom, indexFrom, lineTo, indexTo = self.getSelection()
        
        if indexTo == 0:
            endLine = lineTo - 1
        else:
            endLine = lineTo
        
        self.beginUndoAction()
        # iterate over the lines
        for line in range(lineFrom, endLine+1):
            if indent:
                self.indent(line)
            else:
                self.unindent(line)
        self.endUndoAction()
        if indent:
            if indexTo == 0:
                self.setSelection(lineFrom, indexFrom + self.indentationWidth(),
                                  lineTo, 0)
            else:
                self.setSelection(lineFrom, indexFrom + self.indentationWidth(),
                                  lineTo, indexTo + self.indentationWidth())
        else:
            indexStart = indexFrom - self.indentationWidth()
            if indexStart < 0:
                indexStart = 0
            indexEnd = indexTo - self.indentationWidth()
            if indexEnd < 0:
                indexEnd = 0
            self.setSelection(lineFrom, indexStart, lineTo, indexEnd)
        
        
        
############################################################################
## Comment handling methods
############################################################################


    def deal_comment_actions(self):
        mainwindow = self.get_mainwindow()
        mainwindow.act_commentcode.setEnabled(self.can_block_comment())
        mainwindow.act_uncommentcode.setEnabled(self.can_block_comment())
        mainwindow.act_streamcommentcode.setEnabled(self.can_stream_comment())



    def can_block_comment(self):
        if self.lexer_ is None:
            return False
        else:
            return not self.lexer_.comment_string.isEmpty()



    def can_stream_comment(self):
        if self.lexer_ is None:
            return False
        else:
            return not self.lexer_.stream_comment_string['start'].isEmpty()



    def comment(self):
        if self.hasSelectedText():
            self.comment_selection()
        else:
            self.comment_line()



    def uncomment(self):
        if self.hasSelectedText():
            self.uncomment_selection()
        else:
            self.uncomment_line()



    def stream_comment(self):
        if self.hasSelectedText():
            self.stream_comment_selection()
        else:
            self.stream_comment_line()
            


    def comment_line(self):
        if self.lexer_ is None or self.can_block_comment() is False:
            return
        
        commentStr = self.lexer_.comment_string
        line, index = self.getCursorPosition()
        self.beginUndoAction()
        self.insertAt(commentStr, line, 0)
        self.endUndoAction()
        
        

    def comment_selection(self):
        if self.lexer_ is None or self.can_block_comment() is False:
            return

        if not self.hasSelectedText():
            return

        commentStr = self.lexer_.comment_string
        
        # get the selection boundaries
        lineFrom, indexFrom, lineTo, indexTo = self.getSelection()
        if indexTo == 0:
            endLine = lineTo - 1
        else:
            endLine = lineTo
        
        self.beginUndoAction()
        # iterate over the lines
        for line in range(lineFrom, endLine + 1):
            self.insertAt(commentStr, line, 0)
        # change the selection accordingly
        self.setSelection(lineFrom, 0, endLine + 1, 0)
        self.endUndoAction()



    def uncomment_line(self):
        if self.lexer_ is None or self.can_block_comment() is False:
            return
        
        commentStr = self.lexer_.comment_string
        line, index = self.getCursorPosition()

        if not self.text(line).trimmed().startsWith(commentStr):
            # check if line starts with the comment string
            # if not exit the function
            return
        
        # now remove the comment string
        self.beginUndoAction()
        self.setSelection(line, 0, line, commentStr.length())
        self.removeSelectedText()
        self.endUndoAction()



    def uncomment_selection(self):
        if self.lexer_ is None or self.can_block_comment() is False:
            return

        if not self.hasSelectedText():
            return

        commentStr = self.lexer_.comment_string
        
        # get the selection boundaries
        lineFrom, indexFrom, lineTo, indexTo = self.getSelection()
        if indexTo == 0:
            endLine = lineTo - 1
        else:
            endLine = lineTo
        
        self.beginUndoAction()
        # iterate over the lines
        for line in range(lineFrom, endLine + 1):
            # check if line starts with the comment string
            # if not proceed to next line
            if not self.text(line).trimmed().startsWith(commentStr):
                continue

            self.setSelection(line, 0, line, commentStr.length())

            self.removeSelectedText()
            
            # adjust selection start
            if line == lineFrom:
                indexFrom -= commentStr.length()
                if indexFrom < 0:
                    indexFrom = 0
            
            # adjust selection end
            if line == lineTo:
                indexTo -= commentStr.length()
                if indexTo < 0:
                    indexTo = 0
            
        # change the selection accordingly
        self.setSelection(lineFrom, indexFrom, lineTo, indexTo)
        self.endUndoAction()



    def stream_comment_line(self):
        if self.lexer_ is None or self.can_stream_comment() is False:
            return
        
        commentStr = self.lexer_.stream_comment_string
        line, index = self.getCursorPosition()
        
        self.beginUndoAction()
        self.insertAt(commentStr['end'], line, self.lineLength(line))
        self.insertAt(commentStr['start'], line, 0)
        self.endUndoAction()



    def stream_comment_selection(self):
        if self.lexer_ is None or self.can_stream_comment() is False:
            return
        
        if not self.hasSelectedText():
            return
        
        commentStr = self.lexer_.stream_comment_string
        
        # get the selection boundaries
        lineFrom, indexFrom, lineTo, indexTo = self.getSelection()
        if indexTo == 0:
            endLine = lineTo - 1
            endIndex = self.lineLength(endLine)
        else:
            endLine = lineTo
            endIndex = indexTo
        
        self.beginUndoAction()
        self.insertAt(commentStr['end'], endLine, endIndex)
        self.insertAt(commentStr['start'], lineFrom, indexFrom)
        
        # change the selection accordingly
        if indexTo > 0:
            indexTo += commentStr['end'].length()
            if lineFrom == endLine:
                indexTo += commentStr['start'].length()
        self.setSelection(lineFrom, indexFrom, lineTo, indexTo)
        self.endUndoAction()
        
        
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
                main = self.zen.get_main_instance()
                checkfile = main.isfile_open(str(filename.toLocalFile()))
                if checkfile[0]:
                    checkfile[1].setCurrentIndex(checkfile[2])
                else:
                    main.load_file(str(filename.toLocalFile()))



