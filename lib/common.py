from PyQt4 import QtCore
from PyQt4 import QtGui
import subprocess
import os
import sys
import pprint



class Common():
    '''Provide graphics, icons to the application'''
    def __init__(self):
        pass
    

    def is_ctags_available(self):
        #http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
        return True


    def get_ctags_exepath(self):
        path = ''
        if sys.platform == "linux2":
            path = 'ctags'
        elif sys.platform == "win32":
            path = 'must think about this'
        return path


    def run_ctags(self, cmd):
        info = []
        try:
            retval = subprocess.Popen(cmd,stdout=subprocess.PIPE)
            stdout_value = retval.communicate()[0]
            for line in stdout_value.split('\n'):
                if len(line) != 0:
                    line_info = line.split('\t')
                    line_info[2] = line_info[2].replace(';"','')
                    info.append(line_info)
        except Exception as e:
            print ("Error executing ctags. ",e.args)
        return info
    
    
    
    def get_icon_frombase64(self, data):
        icon = QtGui.QIcon()
        pic = QtGui.QImage()
        pic.loadFromData(QtCore.QByteArray.fromBase64(data),'PNG')
        icon.addPixmap(QtGui.QPixmap.fromImage(pic), 
                       QtGui.QIcon.Normal, 
                       QtGui.QIcon.Off)
        return icon
        
        
    def get_home_dir(self):
        #homedir = os.path.expanduser('~user')
        homedir = os.getenv('HOME')
        return homedir
    
    
    def get_main_instance(self):
        tops = QtGui.QApplication.topLevelWidgets()
        mainwindow = None
        for top in tops:
            if top.objectName() == 'MainWindow':
                mainwindow = top
        return mainwindow
    
    
    def print_pretty(self, data):
        '''Pretty print data'''
        print(pprint.pprint(data))
        
        
    def determine_language(self, filename):
        basename, ext = os.path.splitext(unicode(filename))
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
    
    def ctags_supported_langs(self):
        s = '''Ant
Asm
Asp
Awk
Basic
BETA
C
C++
C#
Cobol
Batch
Eiffel
Erlang
Flex
Fortran
HTML
xml
Java
JavaScript
Lisp
Lua
Make
MatLab
OCaml
Pascal
Perl
PHP
Python
REXX
Ruby
Scheme
Bash
SLang
SML
SQL
Tcl
Tex
Vera
Verilog
VHDL
Vim
YACC'''.splitlines()
        return s

        
        
        