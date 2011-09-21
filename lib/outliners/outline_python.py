#!/usr/bin/env python
import lib.common
import lib.resources
import lib.preferences
import outliner
import os



class PythonOutliner():
    '''Provide the preferences defaults to the application'''
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

        members = []
        classes = []
        namespaces = []
        variables = []
        functions = []

        #######################################################################
        # Harvest
        for item in output:
            type = item[3]
            name = item[0]
            lineno = item[2]
            
            if type == 'kind:namespace':
                namespaces.append({'name':name, 'lineno':lineno})
            if type == 'kind:function':
                functions.append({'name':name, 'lineno':lineno})
            if type == 'kind:class':
                classes.append({'name':name, 'lineno':lineno})
            if type == 'kind:member':
                if len(item) > 4:
                    # method belongs to class
                    members.append({'name':name,
                                    'class':item[4].replace('class:', ''),
                                    'lineno':lineno})
                elif len(item) <= 4:
                    # method do not belong to class
                    members.append({'name':name, 'lineno':lineno})     
            if type == 'kind:variable':
                if len(item) > 4:
                    # variable belongs to class
                    variables.append({'name':name,
                                    'class':item[4].replace('class:', ''),
                                    'lineno':lineno})
                elif len(item) <= 4:
                    # variable do not belong to class
                    variables.append({'name':name, 'lineno':lineno})

        #######################################################################
        # Publish

        # Get classes  
        for class_ in classes:
            class_node = outliner.myNode(class_['name'],
                                        'class', 
                                        class_['lineno'], 
                                        self.root)
            for var in variables:
                if 'class' in var:
                    if var['class'] == class_['name']:
                        outliner.myNode(var['name'], 
                                        'variable', 
                                        var['lineno'], 
                                        class_node)
            for member in members:
                if 'class' in member:
                    if member['class'] == class_['name']:
                        outliner.myNode(member['name'], 
                                        'member', 
                                        member['lineno'], 
                                        class_node)
                        
        # Get variables not belonging to a class
        for var in variables:
            if 'class' not in var:
                outliner.myNode(var['name'], 
                                'variable', 
                                var['lineno'], 
                                self.root)

        # Get functions
        for func in functions:
            outliner.myNode(func['name'], 
                            'function', 
                            func['lineno'], 
                            self.root)
                
        # Get methods not belonging to a class
        for member in members:
            if 'class' not in member:
                outliner.myNode(member['name'], 
                                'member', 
                                member['lineno'], 
                                self.root)
                
        # Get imports
        for namespace in namespaces:
            outliner.myNode(namespace['name'], 
                            'namespace', 
                            namespace['lineno'], 
                            self.root)
                
                
                