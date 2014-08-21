import notebook_editing_scene
import notebook_selection_scene
import notebooks
import curses
import scene_handler
import copy
from operator import attrgetter

clipboard = 0
saved = False
last_states = [ 0, 0, 0]

def handle_input(scr, c):
    if c in [ord("j"), curses.KEY_DOWN]:
        __index_scroll(1)

    elif c in [ord("k"), curses.KEY_UP]:
        __index_scroll(-1)

    elif c in [ord("l"), curses.KEY_RIGHT]:
        __index_in()

    elif c in [ord("h"), curses.KEY_LEFT]:
        __index_out()

    elif c == ord("t"):
        __toggle_expand()

    elif c in [ord("a"), curses.KEY_ENTER, 10]:
        # Back up current state
        __push_onto_last_states ()
        __edit_node()

    elif c in [ord("o"), ord("n")]:
        __edit_new_node_below()

    elif c in [ ord ( "O" ), ord ( "N" ) ]:
        __edit_new_node_above ()

    elif c in [ord("d"), 330]: #Delete key
        __delete_node()

    elif c == ord("p"):
        __paste_node( notebook_editing_scene.index [ - 1 ] + 1 )

    elif c == ord("P"):
        __paste_node( notebook_editing_scene.index [ - 1 ] )

    elif c == ord("y"):
        __yank_node()

    elif c in [ord("w"), curses.KEY_F2]:
        __save_notebooks()

    elif c == ord("q"):
        notebooks.save_notebooks()
        # Reset last_states
        global last_states
        last_states = [ 0, 0, 0 ]
        scene_handler.scene = notebook_selection_scene

    elif c == ord("g"):
        __goto_first_node()

    elif c == ord("G"):
        __goto_last_node()

    elif c == ord ( "s" ):
        __sort_elements ()

    elif c == ord ( "u" ):
        __undo ()

    elif c == ord("Q"):
        notebooks.save_notebooks()
        return False

    return True

def get_name():
    return "BROWSING"

def draw_mode(scr):
    global saved

    if saved:
        scr.move(0, 0)
        save_str = (" Saved notebooks to %s" % notebooks.file_path)[:scr.getmaxyx()[1]]
        scr.addstr(save_str, curses.color_pair(2))
        notebook_editing_scene.__place_cursor(scr)
        saved = False

def __index_scroll(distance):
    # Scroll <distance> indexes down (negative means up)

    parent_node = notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1])

    # index in acceptable range
    if notebook_editing_scene.index[-1] + distance in range(0, len(parent_node.children)):
        notebook_editing_scene.index[-1] += distance

def __index_in():
    # Move down in hierarchy

    # Node has no children and is not nameless
    if len(notebook_editing_scene.__get_selected_node().children) == 0 and not notebook_editing_scene.__get_selected_node().name == "":
        # Add temporary node
        notebook_editing_scene.__get_selected_node().children.append(notebooks.Node(""))
        notebook_editing_scene.index.append(0)

    # Node has children
    elif len(notebook_editing_scene.__get_selected_node().children) > 0:
        notebook_editing_scene.index.append(0)

def __index_out():
    # Move up in hierarchy

    # Node is not child of notebook.mother
    if len(notebook_editing_scene.index) > 1:
        # Node is temporary node
        if len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) == 1 and notebook_editing_scene.__get_selected_node().name == "":
            notebook_editing_scene.__remove_selected_node()

        notebook_editing_scene.index = notebook_editing_scene.index[:-1]

def __toggle_expand():
    # Invert node.expanded

    notebook_editing_scene.__get_selected_node().expanded = not notebook_editing_scene.__get_selected_node().expanded 

def __edit_node():
    # Enter editing mode
    
    from modes.editing import editing

    notebook_editing_scene.mode = editing
    notebook_editing_scene.insert_index = len(notebook_editing_scene.__get_selected_node().name)

def __edit_new_node_below():
    # Add new node below the cursor, if there is no temporary node and enter editing mode

    # Back up current state
    __push_onto_last_states ()
    # Node is not a temporary node
    if not (notebook_editing_scene.__get_selected_node().name == "" and len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) == 1):
        # Add a new Node
        notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children.insert ( notebook_editing_scene.index [ -1 ] + 1, notebooks.Node(""))
        notebook_editing_scene.index[-1] += 1

    __edit_node()

def __edit_new_node_above():
    # Add new node above the cursor, if there is no temporary node and enter editing mode

    # Back up current state
    __push_onto_last_states ()
    # Node is not a temporary node
    if not (notebook_editing_scene.__get_selected_node().name == "" and len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) == 1):
        # Add a new Node
        notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children.insert ( notebook_editing_scene.index [ -1 ], notebooks.Node(""))

    __edit_node()

def __delete_node():
    # Delete node and put it into clipboard

    global clipboard
    # Back up current state
    __push_onto_last_states ()
    clipboard = notebook_editing_scene.__remove_selected_node()

    # Last child was deleted
    if not len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) > 0:
        __index_out()

    else:
        __index_scroll(-1)

def __paste_node( insert_index ):
    # Add deepcopy of clipboard

    # Back up current state
    __push_onto_last_states ()
    # clipboard is not empty(0) or error(-1)
    if not type(clipboard) == int:
        # Node is temporary node
        if len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) == 1 and notebook_editing_scene.__get_selected_node().name == "":
            notebook_editing_scene.__remove_selected_node()

        # Insert deepcopy of clipboard
        notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children.insert( insert_index, copy.deepcopy(clipboard))

        if not (len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) == 1 and notebook_editing_scene.__get_selected_node().name == ""):
            __index_scroll( insert_index - notebook_editing_scene.index [ -1 ] )

def __yank_node():
    # Put deepcopy of node into clipboard

    global clipboard
    clipboard = copy.deepcopy(notebook_editing_scene.__get_selected_node())

def __save_notebooks():
    # Save notebooks

    global saved

    notebooks.save_notebooks()
    saved = True

def __goto_first_node():
    # Move index to first node

    notebook_editing_scene.index[-1] = 0

def __goto_last_node():
    # Move index to last node

    notebook_editing_scene.index[-1] = 0
    notebook_editing_scene.index[-1] = len(notebook_editing_scene.__get_node(notebook_editing_scene.index[:-1]).children) - 1

def __sort_elements ():
    # Sort the all the children of the parent of the current node

    # Back up current state
    __push_onto_last_states ()
    notebook_editing_scene.__get_node ( notebook_editing_scene.index [ : -1 ] ).children.sort ( key=attrgetter ( "name" ) )

def __undo ():
    # Undo the few last steps
    if len ( last_states ) > 0:
        if not last_states [ -1 ] == 0:
            notebook_editing_scene.index = last_states [ -1 ].index
            notebooks.notebook_list [ notebook_selection_scene.index ] = last_states.pop ()

def __push_onto_last_states ():
    # Push the current state onto last_states

    last_states.append ( copy.deepcopy ( notebook_selection_scene.__get_selected_notebook () ) )
    if len ( last_states ) > 3:
        last_states.pop ( 0 )
