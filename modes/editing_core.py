import curses

class EditingState(object):
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.exit = False

def handle_input(scr, c, editing_state):
    if c in range(32, 126): #normal characters
        insert_character(editing_state, c)

    elif c == curses.KEY_BACKSPACE:
        remove_previous_character(editing_state)

    elif c == 330: # Delete Key
        remove_character_at(editing_state, editing_state.index)

    elif c == curses.KEY_LEFT:
        move_cursor(editing_state, -1)

    elif c == curses.KEY_RIGHT:
        move_cursor(editing_state, 1)

    elif c == 23: # Ctrl + w
        remove_word ( editing_state )

    elif c in [27, curses.KEY_ENTER, 10]: #Escape and enter
        exit(editing_state)

    return editing_state

def insert_character(editing_state, c):
    # Insert the character at cursor position

    editing_state.name = editing_state.name[:editing_state.index] + chr(c) + editing_state.name[editing_state.index:]
    editing_state.index += 1

def remove_previous_character(editing_state):
    # Delete character before cursor position

    if editing_state.index > 0:
        remove_character_at(editing_state, editing_state.index - 1)
        editing_state.index -= 1

def remove_character_at(editing_state, index):
    # Remove the character at <index>

    if editing_state.index > -1:
        editing_state.name = editing_state.name[:index] + editing_state.name[index + 1:]
 
def move_cursor(editing_state, n):
    # Move cursor <n> steps to the right (negative means left)

    if (editing_state.index + n) in range(0, len(editing_state.name) + 1):
        editing_state.index += n

def exit(editing_state):
# Exit editing mode

    editing_state.exit = True

def remove_word ( editing_state ):
    # Delete word before index ( similliar to i_c-W in vim )

    if len ( editing_state.name ) > 0:
        if ( editing_state.name [ editing_state.index - 1 ] == " " ):
            remove_previous_character ( editing_state )
        relevant_words = editing_state.name [ : editing_state.index ].split ( " " )
        relevant_words.pop ()

        if len ( relevant_words ) > 0:
            relevant_words = " ".join ( relevant_words ) + " "
        else:
            relevant_words = ""

        editing_state.name = relevant_words + editing_state.name [ editing_state.index : ]
        editing_state.index = len ( relevant_words )
