import ipywidgets as widgets
from about import AboutTab

about_tab = AboutTab()
tab_height = 'auto'
tab_layout = widgets.Layout(width='auto',height=tab_height, overflow_y='scroll',)   # border='2px solid black',
titles = ['About']
tabs = widgets.Tab(children=[about_tab.tab],
                   _titles={i: t for i, t in enumerate(titles)},
                   layout=tab_layout)

tool_title = widgets.Label(r'\(\textbf{scrolltest}\)')
gui = widgets.VBox(children=[tool_title, tabs])
