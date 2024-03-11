from taipy.gui import Gui
from basic_demo_page import page

gui = Gui()
gui.add_page("basic", page)

gui.run(run_browser=True, use_reloader=True)