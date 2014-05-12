import notebook_selection_scene
from modes import editing_core

def handle_input(scr, c):
    editing_state = editing_core.EditingState(notebook_selection_scene.__get_selected_notebook().name, notebook_selection_scene.insert_index)
    editing_state = editing_core.handle_input(scr, c, editing_state)

    notebook_selection_scene.insert_index = editing_state.index
    notebook_selection_scene.__get_selected_notebook().name = editing_state.name

    if editing_state.exit:
        exit_editing_mode()

    return True

def get_name():
    return "EDITING"

def exit_editing_mode():
    # Exit editing mode

    from modes.selection import browsing

    notebook_selection_scene.mode = browsing
    notebook_selection_scene.insert_index = -1
    notebook_selection_scene.__get_selected_notebook().mother.name = notebook_selection_scene.__get_selected_notebook().name
