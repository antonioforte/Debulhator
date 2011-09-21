#!/usr/bin/env python
import HTMLParser
import string

from lxml import etree

import lib.common
import lib.resources
import lib.preferences
import outliner




class MyHtmlParser(HTMLParser.HTMLParser):
    def __init__(self, file):
        HTMLParser.HTMLParser.__init__(self)
        thefile = open(file, 'r')
        self.feed(thefile.read())

    def handle_starttag(self, tag, attributes):
        pass

    def handle_endtag(self, tag):
        pass



class HtmlOutliner():
    '''Parse html and xml documents'''
    def __init__(self, tree_root, _file, language):
        self.file = str(_file)
        self.root = tree_root
        self.language = language
        self.zen = lib.common.Common()
        self.prefs = lib.preferences.Preferences()


    def test_html_file(self):
        '''Test file using Python HtmlParser'''
        try:
            MyHtmlParser(self.file)
        except Exception as e:
            print ("Error python HTML Parser. ", e)
            error_template = string.Template(\
                             '''Line $line Column $col Message $message''')
            error_msg = error_template.safe_substitute(line=str(e.lineno),
                                                       col=str(e.offset),
                                                       message=e.msg)
            outliner.myNode(error_msg, error_msg, 'nonumber', self.root)



    def get_xml(self, filename):
        '''Parse HTML or XML file.
        Use both Python HTML Parser and lxml parsers for HTML.
        Only the lxml parser is used to populate the QTreeview.
        '''
        tree = 'not'
        try:
            if self.language == 'HTML':
                self.test_html_file()
                parser = etree.HTMLParser()
            if self.language == 'xml':
                parser = etree.XMLParser()
            tree = etree.parse(filename, parser)
        except Exception as e:
            print ("Error could not get xml or html file", e)
            error = parser.error_log[0]
            error_template = string.Template(\
                             '''Line $line Column $col Message $message''')
            error_msg = error_template.safe_substitute(line=str(error.line),
                                                       col=str(error.column),
                                                       message=error.message)
            outliner.myNode(error_msg, error_msg, 'nonumber', self.root)
        return tree
    


    def outline(self):
        '''Find document childs and create the QTreeview nodes'''
        tree = self.get_xml(self.file)
        if tree == 'not':
            return
        
        doc_root = tree.getroot()
        _root = outliner.myNode(doc_root.tag,
                                doc_root.tag,
                                'nonumber',
                                self.root)

        els = doc_root.findall('*')
        for item in els:
            self.add_child(item, _root)

 

    def add_child(self, item, parent):
        node_text = item.tag 
        node_line = item.sourceline

        # todo : specify which atribs to show 
        setting = self.prefs.get_setting(\
                     'SourceBrowser/ShowHtml_XmlAtributtes', False) 
        if setting == True:
            for attrib, value in item.items():
                node_text += ' ' + attrib + '=' + value 

        node = outliner.myNode(node_text, node_text, node_line, parent)
        for child in item.getchildren():
            self.add_child(child, node)





