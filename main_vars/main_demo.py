from taipy.gui import Gui
from chlkt import *

gui = Gui()

L = ["A", "B", "C"]
s = "A"
u = "D"

def on_change(state, var, val):
    if var == "u":
        state.L = L.append(val)

# Create a Chalk'it Page instance
page = ChalkitPage("main.xprjson")

gui.add_page("basic", page)
gui.run(run_browser=True, use_reloader=True)