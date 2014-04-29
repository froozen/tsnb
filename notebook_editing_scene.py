import curses
import notebooks

notebook_id = 0
index = 0
handle_input = 0

def handle_input(scr, c):
    scr.addstr(6, 4, "Yay! v2")

    if c == ord("q"):
        return False

    redraw(scr)
    return True

def init(scr, n_id):
    global notebook_id
    n_id = notebook_id

    redraw(scr)

def redraw(scr):
    scr.erase()
    pos = [1, 2]
    draw_node(scr, notebooks.notebook_list[notebook_id].mother, pos)

def draw_node(scr, node, pos):
    pos[0] += 1

    scr.move(pos[0], 0)
    scr.clrtoeol()
    scr.addstr(pos[0], pos[1], node.get_symbol(), curses.color_pair(2))
    scr.addstr(" %s" % node.name)
    
    if node.expanded and len(node.children) > 0:
        for child in node.children:
            pos[1] += 2
            pos = draw_node(scr, child, pos)

    pos[1] -= 2
    return pos

