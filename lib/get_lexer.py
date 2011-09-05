#!/usr/bin/env python
import os




class GetLexer():
    def __init__(self, filename, language, parent):
        self.filename = filename
        self.parent = parent

        # Language can be specified or 
        # discovered by the file extension
        if language != None:
            self.language = language 
        else:
            self.language = self.determine_language()



    def get_lexer(self):
        '''Get lexer according to the language'''
        lexer = None
        
        if self.language == 'Python': 
            from lexers.LexerPython import LexerPython
            lexer = LexerPython(self.parent)
        elif self.language == 'HTML':
            from lexers.LexerHTML import LexerHTML
            lexer = LexerHTML(self.parent)
        elif self.language == 'JavaScript':
            from lexers.LexerJavaScript import LexerJavaScript
            lexer = LexerJavaScript(self.parent)
        elif self.language == 'xml':
            from lexers.LexerXML import LexerXML
            lexer = LexerXML(self.parent)
        elif self.language == 'CSS':
            from lexers.LexerCSS import LexerCSS
            lexer = LexerCSS(self.parent)
        elif self.language == 'Bash':
            from lexers.LexerBash import LexerBash
            lexer = LexerBash(self.parent)
        elif self.language == 'C++':
            from lexers.LexerCPP import LexerCPP
            lexer = LexerCPP(self.parent)
        elif self.language == 'POV':
            from lexers.LexerPOV import LexerPOV
            lexer = LexerPOV(self.parent)
                        
            
        return lexer
    
     
    
    def determine_language(self):
        basename, ext = os.path.splitext(unicode(self.filename))
        assocs = self.get_assocs()
        language = ''
        
        if ext in assocs.keys():
            language = assocs[ext]

        return language
        
        
        
    def get_assocs(self):
        assocs = {
        ".sh"              : "Bash",
        ".bash"            : "Bash",
        ".bat"             : "Batch",
        ".cmd"             : "Batch",
        ".cpp"             : "C++",
        ".cxx"             : "C++",
        ".cc"              : "C++",
        ".c"               : "C++",
        ".hpp"             : "C++",
        ".hh"              : "C++",
        ".h"               : "C++",
        ".cs"              : "C#",
        ".html"            : "HTML",
        ".htm"             : "HTML",
        ".asp"             : "HTML",
        ".shtml"           : "HTML",
        ".php"             : "HTML",
        ".xsl"             : "HTML",
        ".svg"             : "HTML",
        ".xsd"             : "HTML",
        ".xslt"            : "HTML",
        ".dtd"             : "HTML",
        ".rdf"             : "HTML",
        ".xul"             : "HTML", 
        ".xml"             : "xml", 
        ".java"            : "Java",
        ".js"              : "JavaScript",
        ".lua"             : "Lua",
        ".pl"              : "Perl",
        ".pm"              : "Perl",
        ".ph"              : "Perl",
        ".pov"             : "POV",
        ".properties"      : "Properties",
        ".ini"             : "Properties",
        ".inf"             : "Properties",
        ".reg"             : "Properties",
        ".cfg"             : "Properties",
        ".cnf"             : "Properties",
        ".rc"              : "Properties",
        ".py"              : "Python",
        ".pyw"             : "Python",
        ".pyx"             : "Python",
        ".ptl"             : "Python",
        ".rb"              : "Ruby",
        ".rbw"             : "Ruby",
        ".sql"             : "SQL",
        ".css"             : "CSS"
    }
        return assocs
    
