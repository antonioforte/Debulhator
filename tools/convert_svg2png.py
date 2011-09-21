import os
import subprocess
from xml.etree import ElementTree as ET



class Main:   
    def __init__(self):   
        # convert svg to png
        # create qrc
        # create py file
        
        self.overwrite__png = False

        self.curdir = os.path.abspath(os.path.dirname(__file__))
        self.svg_folder = os.path.join(self.curdir, 'svg')
        self.png_folder = os.path.join(self.curdir, 'png')

        self.go_convert_svg2png()
        self.create_qrc()
        self.create_py()


    def go_convert_svg2png(self):
        for root, dirs, files in os.walk(unicode(self.svg_folder)):
            for fn in files:
                fullurl = os.path.join(root, fn)
                filebasename, ext = os.path.splitext(fn)
                png_path = os.path.join(self.png_folder, filebasename + '.png')

                if not os.path.exists(png_path) or self.overwrite__png == True:
                    cmd = ["inkscape","-f",fullurl,"--export-png",png_path]
                    try:
                        proc = subprocess.call(cmd)
                    except Exception as e:
                        print('Problems inkscape : ',e)


    def create_qrc(self):
        qrc = ET.fromstring('''<RCC></RCC>''')
        node = ET.SubElement(qrc, 'qresource')

        for root, dirs, files in os.walk(unicode(self.png_folder)):
            for fn in files:
                file = ET.SubElement(node, 'file')
                file.text = 'png/'+fn
        
        self.indent(qrc)
        xml_file = os.path.join(self.curdir,'resources.qrc')
        ET.ElementTree(qrc).write(xml_file, 'utf-8')


    def create_py(self):
        qrc_file = os.path.join(self.curdir,'resources.qrc')
        py_file = os.path.join(self.curdir,'resources.py')
        try:
            cmd = ['pyrcc4',qrc_file,'-o',py_file]
            proc = subprocess.call(cmd)
        except Exception as e:
            print('Problems pyrcc4 : ',e)


    def indent(self, elem, level=0):
        # http://effbot.org/zone/element-lib.htm
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self.indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i


if __name__ == "__main__":
    Main()
            
            
            
            
            
            
            
