import notebook_editing_scene
from notebooks import *

def handle_input(scr, c):

    if c == ord("j"):
        __index_scroll(1)

    elif c == ord("k"):
        __index_scroll(-1)

    elif c == ord("l"):
        __index_in()

    elif c == ord("h"):
        __index_out()

    elif c == ord("t"):
        __toggle_expand()

    elif c == ord("a"):
        __edit_node()

    elif c == ord("o"):
        __edit_new_node()

    elif c == ord("d"):
        notebook_editing_scene.__remove_selected_node()

    elif c == ord("q"):
        return False

    return True

def get_name():
    return "BROWSING"

def __index_scroll(distance):
    notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] += distance

    if notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] > len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) - 1:
        notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] = 0
    
    elif notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] < 0:
        notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] = len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) - 1

def __index_in():
    if len(notebook_editing_scene.__get_selected_node().children) == 0 and not notebook_editing_scene.__get_selected_node().name == "":
        notebook_editing_scene.__get_selected_node().children.append(Node(""))
        notebook_editing_scene.index.append(0)

    elif len(notebook_editing_scene.__get_selected_node().children) > 0:
        notebook_editing_scene.index.append(0)

def __index_out():
    if len(notebook_editing_scene.index) > 1:
        # The only node is "" (temporary node)
        if notebook_editing_scene.__get_selected_node().name == "" and len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) == 1:
            notebook_editing_scene.__remove_selected_node()

        notebook_editing_scene.index = notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]

def __toggle_expand():
    notebook_editing_scene.__get_selected_node().expanded = not notebook_editing_scene.__get_selected_node().expanded 

def __edit_node():
    from modes import editing

    notebook_editing_scene.mode = editing

def __edit_new_node():
    notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children.append(Node(""))
    notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] = len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) - 1
    __edit_node()
