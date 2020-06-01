import graphviz as gz

g = gz.Digraph('G', filename='bp.gv')
# dot.node('1','Test1')
# dot.node('2','Test2')
# dot.edges(['12'])
g.attr('node', shape='circle', style='filled', fontcolor='black', rank='L', size='4,8')

text = [['x', '', 'white'], ['1', 'a', 'yellow'], ['3', 'c', 'blue'],
        ['y', '', 'white'], ['2', 'b', 'red'], ['4', 'd', 'pink'], ['5', 'e', 'orange']]
edges = ['x1', 'y2', '13', '14', '23', '24', '35', '45']

status = 0
# for l, t, c in text:
# if status1:
#     g.node(l, t, fillcolor=c, color='white')
#     status1 = False
# elif status2:
#     g.node(l, t, fillcolor=c, color='white')
#     status2 = False
# else:
#     g.node(l, t, fillcolor=c)
with g.subgraph(name='r1') as r1:
    r1.attr(rank='same')
    for l, t, c in text:
        if status < 3:
            r1.node(l, t, fillcolor=c)
            status += 1
status = 0
with g.subgraph(name='r2') as r2:
    r2.attr(rank='same')
    for l, t, c in text:
        if status < 3:
            status += 1
        else:
            r2.node(l, t, fillcolor=c)

g.node(text[6][0], text[6][1], fillcolor=text[6][2])
g.edges(edges)

g.view()
