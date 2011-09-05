from xml.etree import ElementTree as ET

from PyQt4 import QtCore
from PyQt4 import QtGui

import common



class AppDefaults():
    '''Provide the preferences defaults to the application'''
    def __init__(self):
        pass


    def default_config(self):
    
        settings = {
            'Explorer/StartDir' : "/home/antonio",
            'Explorer/FileTypesToHide' : ["pyc","exe"],
            'Explorer/FileTypesToHideStrings' : ["old","new"],
            
            'Recent/MaxRecentFiles': 10,
            'Recent/LastDirVisited': '/media/myhouse/temp/Test',
            
            'Docks/ShowTitle' : False,
            'Docks/LeftDockTabPosition': QtGui.QTabWidget.North,
            'Docks/RightDockTabPosition': QtGui.QTabWidget.North,
            'Docks/BottomDockTabPosition': QtGui.QTabWidget.West,

            # Editor settings
            'Editor/SyntaxTheme':'default',
            'Editor/AutoIndent': True,
            'Editor/BraceMatchMode': 2,
            'Editor/CaretLineVisible': True,
            
            'Editor/EdgeColumnChars': 80,
            'Editor/EdgeMode': 1,
            
            'Editor/EnableBgColorKeywords': True,
            
            'Editor/Folding': 3,
            'Editor/FoldingIsVisible': True,
            
            'Editor/IndentWidth': 4,
            'Editor/IndentationGuides': True,
            
            'Editor/MarginLineNumbers': True,
            'Editor/MarginLineNumbersWidth': 10,
            'Editor/TabWidth': 4,
            'Editor/ZoomFactor': 1}
     
        return settings 
    


class Preferences():
    '''Provide the preferences to the application'''
    def __init__(self):
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat,
                                    QtCore.QSettings.UserScope,
                                    "Debulhator", "My Company")

        self.check_ini_created()

        syntaxtheme = self.get_setting('Editor/SyntaxTheme', 'default')
        if syntaxtheme == 'default':
            import color_themes.default
            theme = color_themes.default.Default().theme_xml_string()
            
        self.styles = ET.fromstring(theme)
        self.global_styles = self.get_global_styles()
        self.langs_styles = self.get_lexers()



    def get_setting(self, setting, default):
        value = self.settings.value(setting, default)
        return value



    def set_setting(self, setting, value):
        self.settings.setValue(setting, value)



    def get_global_styles(self):
        '''Read style xml and extract global styles'''
        globalstyles = {}
        xmlglobalstyles = self.styles.find('GlobalStyles')
        
        for style in xmlglobalstyles.getiterator('WidgetStyle'):
            stylename = style.attrib['name']
            globalstyles[stylename] = {}

            for item in style.keys():
                if item == 'fgColor' or item == 'bgColor':
                    globalstyles[stylename][item] = QtGui.QColor('#'+style.attrib[item])
                else:
                    globalstyles[stylename][item] = style.attrib[item]

        return globalstyles



    def get_lexers(self):
        '''Read style xml and extract lexers'''
        lexers = {}
        for lexertype in self.styles.getiterator('LexerType'):
            language = lexertype.attrib['desc']
            lexers[language] = {}
            
            for wordstyle in lexertype.getiterator('WordsStyle'):
                styleid = wordstyle.attrib['styleID']
                lexers[language][styleid] = {}
                
                for item in wordstyle.keys():
                    if item == 'fgColor' or item == 'bgColor':
                        lexers[language][styleid][item] = QtGui.QColor('#'+wordstyle.attrib[item])
                    else:
                        lexers[language][styleid][item] = wordstyle.attrib[item]

        return lexers
        



    def check_ini_created(self):
        '''Check if settings contains value'''
        if self.settings.contains('Editor/EdgeMode') == False:
            print('Creating new defaults')
            for key in AppDefaults().default_config().keys():
                self.settings.setValue(key, AppDefaults().default_config()[key])


            
