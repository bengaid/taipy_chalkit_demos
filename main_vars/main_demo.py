from taipy.gui import Gui
from chlkt import *
from taipy.gui.custom import Page

gui = Gui()

L = ["A", "B", "C"]
s = "A"
u = "D"

def on_change(state, var, val):
    if var == "u":
        state.L = L.append(val)

# Define xprjson file name
xprjson_file_name = "main.xprjson"
# Create a Page instance with the resource handler
page = Page(PureHTMLResourceHandler())

gui.add_page("basic", page)
gui.run(run_browser=True, use_reloader=True)