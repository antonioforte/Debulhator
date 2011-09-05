from PyQt4 import QtCore
from PyQt4 import QtGui

import os
import pprint

class Common():
    '''Provide graphics, icons to the application'''
    def __init__(self):
        pass
    

    
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