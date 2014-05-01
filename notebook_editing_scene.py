import curses
import notebooks
from modes import browsing

notebook_id = 0
index = [0]

mode_handle_input = 0
mode_name = 0

def handle_input(scr, c):
    ret = mode_handle_input(scr, c)
    __redraw(scr)
    return ret

def init(scr, n_id):
    global notebook_id
    global mode_handle_input

    notebook_id = n_id
    
    browsing.init()
    mode_handle_input = browsing.handle_input

    __redraw(scr)

def __redraw(scr):
    scr.erase()
    pos = [1, 2]
    __draw_node(scr, notebooks.notebook_list[notebook_id].mother, pos)
    __draw_mode(scr)

def __draw_node(scr, node, pos):
    INDENT = 4

    pos[0] += 1

    scr.move(pos[0], 0)
    scr.clrtoeol()
    scr.addstr(pos[0], pos[1], "%s " % node.get_symbol(), curses.color_pair(2))

    if node == __get_selected_node():
        scr.addstr(node.name, curses.color_pair(1))
    else:
        scr.addstr(node.name)
    
    if (node.expanded or __node_in_path(node, index)) and len(node.children) > 0:
        for child in node.children:
            pos[1] += INDENT
            pos = __draw_node(scr, child, pos)

    pos[1] -= INDENT
    return pos

def __draw_mode(scr):
    global mode_name
    scr.addstr(scr.getmaxyx()[0] - 1, 0, "--%s--" % mode_name, curses.color_pair(1))

def __get_selected_node():
    return notebooks.notebook_list[notebook_id].get_node(index)

def __get_node(pos):
    return notebooks.notebook_list[notebook_id].get_node(pos)

def __node_in_path(node, path):
    for i in range(1, len(path)):
        if __get_node(path[0:i]) == node:
            return True
    
    return False

def __remove_selected_node():
    notebooks.notebook_list[notebook_id].remove_node(index)

def __remove_node(pos):
    notebooks.notebook_list[notebook_id].remove_node(pos)
