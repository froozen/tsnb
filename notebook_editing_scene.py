import curses
import math
import notebooks
from modes.editing import browsing
from modes.editing import editing

notebook_id = 0
index = [0]
insert_index = -1
insert_pos = [0, 0]

mode = 0

# NOTE: I adhered to the curses notation of positions [y, x] instead of the normal [x, y]

def handle_input(scr, c):
    ret = mode.handle_input(scr, c)
    notebooks.notebook_list[notebook_id].index = index

    return ret

def init(scr, n_id):
    global notebook_id
    global mode
    global index

    notebook_id = n_id
    mode = browsing
    insert_pos = [scr.getmaxyx()[0] - 1, scr.getmaxyx()[1] - 1]
    index = notebooks.notebook_list[n_id].index

def redraw(scr):
    # Redraw the scene

    scr.erase()
    __display_node_tree(scr)
    __draw_mode(scr)
    __place_cursor(scr)

    if "draw_mode" in dir(mode):
        mode.draw_mode(scr)

def __place_cursor(scr):
    # Move the cursor to the correct position

    # cursor should be moved to insert_pos
    if (not insert_index == -1) and scr.getmaxyx()[0] > insert_pos[0] and scr.getmaxyx()[1] > insert_pos[1]:
        scr.move(insert_pos[0], insert_pos[1])

    else:
        scr.move(scr.getmaxyx()[0] - 1, scr.getmaxyx()[1] - 1)

def __display_node_tree(scr):
    # Draw smart range of node tree

    node_list = []
    __generate_node_list(notebooks.notebook_list[notebook_id].mother, node_list, 0)

    selected_index = __index_in_node_list(node_list, __get_selected_node())
    max_node_count = scr.getmaxyx()[0] - 3

    if max_node_count < len(node_list):
        if 0 > selected_index - math.floor(max_node_count / 2):
            node_list = node_list[:max_node_count]

        elif len(node_list) < selected_index + math.ceil(max_node_count / 2):
            node_list = node_list[- max_node_count:]

        else:
            node_list = node_list[ int ( selected_index - math.floor(max_node_count / 2) ) : int ( selected_index + math.ceil(max_node_count / 2) ) ]

    y = 1
    for node_struct in node_list:
        __draw_node(scr, node_struct, y)
        y += 1


def __index_in_node_list(node_list, node):
    # Return index of struct representing node in node_list

    for struct in node_list:
        if struct[1] == node:
            return node_list.index(struct)

    return -1

def __draw_node(scr, node_struct, y):
    # Draw Node at <pos>

    global insert_pos

    INDENT = 4

    scr_max_pos = scr.getmaxyx()
    max_pos = [scr_max_pos[0] - 1, scr_max_pos[1] - 1]

    pos = [y, INDENT * node_struct[0] + 2]
    node = node_struct[1]

    # <pos> is not outside of screen
    if not pos[0] >= max_pos[0] or pos[1] >= max_pos[1]:
        space = max_pos[1] - pos[1] + 1
        symb_len = len(node.get_symbol()) + 1

        # There is enough space to display the Node.get_symbol()
        if symb_len < space:
            scr.move(pos[0], pos[1])
            scr.addstr("%s " % node.get_symbol(), curses.color_pair(2))
            __draw_node_name(scr, node.name[0:space - symb_len], node == __get_selected_node())

            # Node is selected_node and mode is editing
            if node == __get_selected_node() and mode == editing:
                # Set insert_pos correctly

                if insert_index < space - symb_len and insert_index > -1:
                    insert_pos = [pos[0], pos[1] + symb_len + insert_index]

                else:
                    insert_pos = [scr.getmaxyx()[0] - 1, scr.getmaxyx()[1] - 1]

def __generate_node_list(node, node_list, indent_level):
    # Generate a list of nodes and their indent_level

    # Add self to node_list
    node_list.append([indent_level, node])

    # Node has children and they should be in node_list
    if (node.expanded or __node_in_path(node, index)) and len(node.children) > 0:
        for child in node.children:
            __generate_node_list(child, node_list, indent_level + 1)

def __draw_mode(scr):
    # Draw modename

    global mode_name
    scr.move(scr.getmaxyx()[0] - 1, 0)
    mode_str = ("--%s--" % mode.get_name())[0:scr.getmaxyx()[1] - 1]
    scr.addstr(mode_str, curses.color_pair(1))

def __get_selected_node():
    # Return the Node at index

    return notebooks.notebook_list[notebook_id].get_node(index)

def __get_node(pos):
    # Return the Node at <pos>

    return notebooks.notebook_list[notebook_id].get_node(pos)

def __node_in_path(node, path):
    # Return wether Node is in <path>

    for i in range(1, len(path)):
        if __get_node(path[0:i]) == node:
            return True

    return False

def __remove_selected_node():
    # Remove the Node at index
    return notebooks.notebook_list[notebook_id].remove_node(index)

def __remove_node(pos):
    # Remove the Node at <pos>

    notebooks.notebook_list[notebook_id].remove_node(pos)

def __draw_node_name(scr, name, is_selected):
    # Draw Node.name

    if is_selected:
        if mode == editing:
            scr.addstr(name)
        else:
            scr.addstr(name, curses.color_pair(1))
    else:
        scr.addstr(name)
