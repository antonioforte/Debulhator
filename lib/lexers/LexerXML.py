#!/usr/bin/env python
from PyQt4.Qsci import QsciLexerXML
from PyQt4.QtCore import QString

import Lexer


class LexerXML(QsciLexerXML):
    def __init__(self, parent=None):
        QsciLexerXML.__init__(self, parent)
        
        self.lexer = Lexer.Lexer(self.language())

        self.setDefaultPaper(self.lexer.get_globaldefault_paper())
        self.setFont(self.lexer.get_default_font())
        
        self.comment_string = QString("")
        self.stream_comment_string = {
            'start' : QString('<!-- '),
            'end'   : QString(' -->')
        }
    
    
    def defaultColor(self, style):
        '''Returns the foreground colour of the text for style number style'''
        color = self.lexer.get_default_color(style, self.description(style))
        if color != 'not':
            return color
        return QsciLexerXML.defaultColor(self, style)



    def defaultPaper(self, style):
        '''Returns the background colour of the text for style number style'''
        return self.lexer.get_default_paper(style, self.description(style))


