import notebook_editing_scene
import curses

def handle_input(scr, c):

    if c in range(32, 126): #normal characters
        notebook_editing_scene.__get_selected_node().name += chr(c)

    elif c == curses.KEY_BACKSPACE:
        notebook_editing_scene.__get_selected_node().name = notebook_editing_scene.__get_selected_node().name[0:len(notebook_editing_scene.__get_selected_node().name) - 1]

    elif c in [27, curses.KEY_ENTER, 10]: #Escape and enter
        from modes import browsing

        notebook_editing_scene.mode_handle_input = browsing.handle_input
        browsing.init()

    return True

def init():
    notebook_editing_scene.mode_name = "EDITING"
