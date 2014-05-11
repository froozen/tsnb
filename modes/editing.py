import notebook_editing_scene
import curses

def handle_input(scr, c):
    node_name = notebook_editing_scene.__get_selected_node().name
    insert_index = notebook_editing_scene.insert_index

    if c in range(32, 126): #normal characters
        insert_character(c)

    elif c == curses.KEY_BACKSPACE:
        remove_previous_character()

    elif c == 330: # Delete Key
        remove_character_at(insert_index)

    elif c == curses.KEY_LEFT:
        move_cursor(-1)

    elif c == curses.KEY_RIGHT:
        move_cursor(1)

    elif c in [27, curses.KEY_ENTER, 10]: #Escape and enter
        exit_editing_mode()

    return True

def get_name():
    return "EDITING"

def set_node_name(name):
    notebook_editing_scene.__get_selected_node().name = name

def insert_character(c):
    # Insert the character at cursor position

    node_name = notebook_editing_scene.__get_selected_node().name
    insert_index = notebook_editing_scene.insert_index

    set_node_name(node_name[:insert_index] + chr(c) + node_name[insert_index:])
    notebook_editing_scene.insert_index += 1

def remove_previous_character():
    # Delete character before cursor position

    insert_index = notebook_editing_scene.insert_index

    if notebook_editing_scene.insert_index > 0:
        remove_character_at(insert_index - 1)
        notebook_editing_scene.insert_index -= 1

def remove_character_at(index):
    # Remove the character at <index>

    node_name = notebook_editing_scene.__get_selected_node().name

    if index > -1:
        set_node_name(node_name[:index] + node_name[index + 1:])
 
def move_cursor(n):
    # Move cursor <n> steps to the right (negative means left)

    node_name = notebook_editing_scene.__get_selected_node().name

    if (notebook_editing_scene.insert_index + n) in range(0, len(node_name) + 1):
        notebook_editing_scene.insert_index += n

def exit_editing_mode():
# Exit editing mode

    from modes import browsing

    notebook_editing_scene.mode = browsing
    notebook_editing_scene.insert_index = -1
