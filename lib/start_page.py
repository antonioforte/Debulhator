#!/usr/bin/env python
from PyQt4 import QtCore
from PyQt4 import QtGui


        
        
        
class StartPage(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        label = QtGui.QLabel(self.tr("Hello World"))

        pal = self.palette()
        pal.setColor(QtGui.QPalette.Window, QtCore.Qt.blue)
        self.setPalette(pal)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
        
    def mousePressEvent(self,e):
        print('GeneralTab clicked')
        self.deleteLater()
        
        