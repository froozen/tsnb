import notebook_editing_scene
from modes import editing_core

def handle_input(scr, c):
    editing_state = editing_core.EditingState(notebook_editing_scene.__get_selected_node().name, notebook_editing_scene.insert_index)
    editing_state = editing_core.handle_input(scr, c, editing_state)

    notebook_editing_scene.insert_index = editing_state.index
    notebook_editing_scene.__get_selected_node().name = editing_state.name

    if editing_state.exit:
        exit_editing_mode()

    return True

def get_name():
    return "EDITING"

def exit_editing_mode():
    # Exit editing mode

    from modes.editing import browsing

    notebook_editing_scene.mode = browsing
    notebook_editing_scene.insert_index = -1
