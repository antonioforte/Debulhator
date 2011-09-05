#!/usr/bin/env python
from PyQt4 import QtGui

import lib.preferences



class Lexer():
    '''Provides custom coloring to lexers'''
    def __init__(self, language):
        self.prefs = lib.preferences.Preferences()
        self.global_styles = self.prefs.global_styles
        self.lexer_style = self.prefs.langs_styles[language]

        
        
    def get_default_font(self):
        font = QtGui.QFont()
        font.setFamily(self.global_styles['Default Style']['fontName'])
        font.setPointSize(int(self.global_styles['Default Style']['fontSize']))
        return font
        
        
        
    def get_globaldefault_paper(self):
        return self.global_styles['Default Style']['bgColor']
        
        
        
    def get_default_color(self, style, description):
        color = 'not'
        try:
            color = self.lexer_style[str(style)]['fgColor']
        except Exception as e:
            print("Warning get style fg color. ", style, str(description))
        return color
        


    def get_default_paper(self, style, description):
        color = self.global_styles['Default Style']['bgColor']
        try:
            color = self.lexer_style[str(style)]['bgColor']
        except Exception as e:
            print("Warning get style bg color. ", style, str(description))
        return color



    def get_mainwindow(self):
        tops = QtGui.QApplication.topLevelWidgets()
        mainwindow = None
        for top in tops:
            if top.objectName() == 'MainWindow':
                mainwindow = top
        return mainwindow
    
    
    