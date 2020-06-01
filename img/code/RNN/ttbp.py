import graphviz as gz

g = gz.Digraph(filename='ttbp')
g.attr(rankdir='TB')

g.view()
