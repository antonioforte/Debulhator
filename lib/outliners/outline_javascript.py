#!/usr/bin/env python
import lib.common
import lib.resources
import lib.preferences
import outliner
import os



class JavascriptOutliner():
    '''Parse javascript ctags tags'''
    def __init__(self, tree_root, file):
        self.file = str(file)
        self.root = tree_root
        self.zen = lib.common.Common()
        self.prefs = lib.preferences.Preferences()


    def outline(self):
        cmd = []
        cmd.append(self.zen.get_ctags_exepath())
        cmd.append('--excmd=number')
        cmd.append('-f -')
        cmd.append('--fields=+zK')
        cmd.append(self.file)
        output = self.zen.run_ctags(cmd)

        # Harvest
        info = {}
        for item in output:
            print(item)
            type = item[3].replace('kind:','')
            name = item[0]
            lineno = item[2]
            
            if type not in info:
                info[type] = []
            info[type].append({'name':name, 'lineno':lineno})
            
        # Publish
        for item_type in info.keys():
            type_root = outliner.myNode(item_type.title(), 
                                        item_type, 
                                        'nonumber', 
                                        self.root)
            for token in info[item_type]:
                outliner.myNode(token['name'], 
                                item_type, 
                                token['lineno'], 
                                type_root)
            