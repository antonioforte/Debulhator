#!/usr/bin/env python
from PyQt4.Qsci import QsciLexerPython
from PyQt4.QtCore import QString
import PyQt4
import Lexer


class LexerPython(QsciLexerPython):
    def __init__(self, parent):
        QsciLexerPython.__init__(self, parent)
        
        self.lexer = Lexer.Lexer(self.language())

        self.setDefaultPaper(self.lexer.get_globaldefault_paper())
        self.setFont(self.lexer.get_default_font())
        self.setIndentationWarning(QsciLexerPython.Inconsistent)
        self.apiwords = self.lexer.api_words.split('\n')

        api = PyQt4.Qsci.QsciAPIs(self)
        for word in self.apiwords:
            api.add(word)
        api.prepare()

        self.comment_string = QString("#")
        self.stream_comment_string = {
            'start' : QString(''),
            'end'   : QString('')
        }
        

    def defaultColor(self, style):
        '''Returns the foreground colour of the text for style number style'''
        color = self.lexer.get_default_color(style, self.description(style))
        if color != 'not':
            return color
        return QsciLexerPython.defaultColor(self, style)



    def defaultPaper(self, style):
        '''Returns the background colour of the text for style number style'''
        return self.lexer.get_default_paper(style, self.description(style))


