

class Apis():
    '''Provide words to the Text Edit autocompletion features'''
    def __init__(self, language):
        self.language = language
    

    def get_words(self):
        if self.language == 'Python':
            words = self.get_python_words()
        else:
            words = ''
        return words
            
            
    def get_python_words(self):
        # /usr/share/qt4/qsci/api/python/Python-2.6.api
        w = '''
self
        '''
        return w
        
        