from ipywidgets import Output
from IPython.display import display, HTML

class AboutTab(object):

    def __init__(self):
#        self.tab = Output(layout={'height': '600px'})
        self.tab = Output(layout={'height': '300px'})
        # self.tab.append_display_data(HTML(filename='latin.html'))
        self.tab.append_display_data(HTML(filename='latin2.html'))
        
