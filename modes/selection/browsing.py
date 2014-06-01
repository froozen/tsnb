import curses
import notebooks
import notebook_editing_scene
import notebook_selection_scene

def handle_input(scr, c):
    if c == ord("q"):
        # Quit program

        return False

    elif c in [ord("j"), curses.KEY_DOWN]:
        __move_index(1)

    elif c in [ord("k"), curses.KEY_UP]:
        __move_index(-1)

    elif c in [ord("l"), curses.KEY_RIGHT]:
        # Enter notebook_editing_scene of selected notebook

        import scene_handler

        notebook_editing_scene.init(scr, notebook_selection_scene.index)
        scene_handler.scene = notebook_editing_scene
        return True

    elif c in [ord("a"), curses.KEY_ENTER, 10]:
        # Start editing the name of the selected notebook

        from modes.selection import editing

        notebook_selection_scene.insert_index = len(notebook_selection_scene.__get_selected_notebook().name)
        notebook_selection_scene.mode = editing

    elif c in [ord("o"), ord("n")]:
        # Create new Notebook

        notebooks.notebook_list.append(notebooks.Notebook("", notebooks.Node()))
        notebook_selection_scene.index = len(notebooks.notebook_list) - 1

        from modes.selection import editing
        notebook_selection_scene.insert_index = len(notebook_selection_scene.__get_selected_notebook().name)
        notebook_selection_scene.mode = editing

    elif c in [ord("d"), 330]: #Delete key
        # Delete selected notebook

        notebooks.notebook_list.pop(notebook_selection_scene.index)
        if notebook_selection_scene.index == len(notebooks.notebook_list):
            notebook_selection_scene.index -= 1

    return True

def get_name():
    return "BROWSING"

def __move_index(n):
    # Move index <n> steps down (negative means up)

    notebook_selection_scene.index += n

    # index > max_index
    if notebook_selection_scene.index > len(notebooks.notebook_list) - 1:
        notebook_selection_scene.index = 0

    # index < 0
    elif notebook_selection_scene.index < 0:
        # Set index to max_index
        notebook_selection_scene.index = len(notebooks.notebook_list) -1

