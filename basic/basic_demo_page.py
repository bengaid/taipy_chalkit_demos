from chlkt import *


a = 1
b = 2
c = {"d": 3, "e": 4}
e = "toto"
l = ["A", "B", "C"]
t = ("A", "B", "C")

res = a*b

tab = [["H1", "H2", "H3"],[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tab2 = [["H1", "H2", "H3"],[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def compute(state):
    state.res = state.a*state.b

# Create a Designer Page instance
page = ChalkitPage("basic_demo_page.xprjson", designer_mode=True)
