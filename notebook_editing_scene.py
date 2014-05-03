import curses
import notebooks
from modes import browsing

notebook_id = 0
index = [0]

mode = 0

def handle_input(scr, c):
    ret = mode.handle_input(scr, c)
    __redraw(scr)

    if not ret:
        notebooks.save_notebooks()

    return ret

def init(scr, n_id):
    global notebook_id
    global mode

    notebook_id = n_id
    
    mode = browsing

    __redraw(scr)

def __redraw(scr):
    scr.erase()
    pos = [1, 2]
    __display_node_tree(scr, notebooks.notebook_list[notebook_id].mother, pos)
    __draw_mode(scr)

def __display_node_tree(scr, node, pos):
    INDENT = 4
    
    pos[0] += 1
    __draw_node(scr, node, pos)

    if (node.expanded or __node_in_path(node, index)) and len(node.children) > 0:
        for child in node.children:
            pos[1] += INDENT
            pos = __display_node_tree(scr, child, pos)

    pos[1] -= INDENT
    return pos

def __draw_mode(scr):
    global mode_name
    scr.move(scr.getmaxyx()[0] - 1, 0)
    mode_str = ("--%s--" % mode.get_name())[0:scr.getmaxyx()[1] - 1]
    scr.addstr(mode_str, curses.color_pair(1))

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

def change_mode(n_mode):
    mode = n_mode

def __draw_node(scr, node, pos):
    scr_max_pos = scr.getmaxyx()
    max_pos = []
    max_pos.append(scr_max_pos[0] - 1)
    max_pos.append(scr_max_pos[1] - 1)

    if not pos[0] >= max_pos[0] or pos[1] >= max_pos[1]:
        space = max_pos[1] - pos[1] + 1
        symb_len = len(node.get_symbol()) + 1

        if symb_len < space:
            scr.move(pos[0], pos[1])
            scr.addstr("%s " % node.get_symbol(), curses.color_pair(2))
            __draw_node_name(scr, node.name[0:space - symb_len], node == __get_selected_node()) 

def __draw_node_name(scr, name, is_selected):
    if is_selected:
        scr.addstr(name, curses.color_pair(1))
    else:
        scr.addstr(name)
