import notebook_editing_scene

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

    return True

def init():
    notebook_editing_scene.mode_name = "BROWSING"

def __index_scroll(distance):
    notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] += distance

    if notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] > len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) - 1:
        notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] = 0
    
    elif notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] < 0:
        notebook_editing_scene.index[len(notebook_editing_scene.index) - 1] = len(notebook_editing_scene.__get_node(notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]).children) - 1

def __index_in():
    if len(notebook_editing_scene.__get_selected_node().children) > 0:
        notebook_editing_scene.index.append(0)

def __index_out():
    if len(notebook_editing_scene.index) > 1:
        notebook_editing_scene.index = notebook_editing_scene.index[0:len(notebook_editing_scene.index) - 1]

def __toggle_expand():
    notebook_editing_scene.__get_selected_node().expanded = not notebook_editing_scene.__get_selected_node().expanded 
