import notebook_editing_scene
import curses

def handle_input(scr, c):

    if c in range(32, 126): #normal characters
        #notebook_editing_scene.__get_selected_node().name += chr(c)
        notebook_editing_scene.__get_selected_node().name = notebook_editing_scene.__get_selected_node().name[:notebook_editing_scene.insert_index] + chr(c) + notebook_editing_scene.__get_selected_node().name[notebook_editing_scene.insert_index:]
        notebook_editing_scene.insert_index += 1

    elif c == curses.KEY_BACKSPACE:
        if notebook_editing_scene.insert_index > 0:
            notebook_editing_scene.__get_selected_node().name = notebook_editing_scene.__get_selected_node().name[:notebook_editing_scene.insert_index - 1] + notebook_editing_scene.__get_selected_node().name[notebook_editing_scene.insert_index:]
            notebook_editing_scene.insert_index -= 1

    elif c == 330: # Delete Key
        if not notebook_editing_scene.insert_index == len(notebook_editing_scene.__get_selected_node().name):
            notebook_editing_scene.__get_selected_node().name = notebook_editing_scene.__get_selected_node().name[:notebook_editing_scene.insert_index] + notebook_editing_scene.__get_selected_node().name[notebook_editing_scene.insert_index + 1:]
            if notebook_editing_scene.insert_index > 0:
                notebook_editing_scene.insert_index -= 1

    elif c == curses.KEY_LEFT:
        if notebook_editing_scene.insert_index > 0:
            notebook_editing_scene.insert_index -= 1

    elif c == curses.KEY_RIGHT:
        if notebook_editing_scene.insert_index < len(notebook_editing_scene.__get_selected_node().name):
            notebook_editing_scene.insert_index += 1


    elif c in [27, curses.KEY_ENTER, 10]: #Escape and enter
        from modes import browsing

        notebook_editing_scene.mode = browsing
        notebook_editing_scene.insert_index = -1

    return True

def get_name():
    return "EDITING"
