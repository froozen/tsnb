import curses
import notebooks
import scene_handler
import notebook_editing_scene

index = 0
editing = False
insert_index = -1
insert_pos = []

def handle_input(scr, c):
    global editing
    global index
    global insert_index

    if not editing:
        if c == ord("q"):
            return False

        elif c in [ord("j"), curses.KEY_DOWN]:
            __move_index(1)

        elif c in [ord("k"), curses.KEY_UP]:
            __move_index(-1)

        elif c in [ord("l"), curses.KEY_RIGHT]:
            notebook_editing_scene.init(scr, index)
            scene_handler.scene = notebook_editing_scene
            return True

        elif c in [ord("a"), curses.KEY_ENTER, 10]:
            insert_index = len(__get_selected_notebook().name)
            editing = True

        elif c in [ord("o"), ord("n")]:
            notebooks.notebook_list.append(notebooks.Notebook("", notebooks.Node()))
            index = len(notebooks.notebook_list) - 1
            insert_index = len(__get_selected_notebook().name)
            editing = True

        elif c in [ord("d"), 330]: #Delete key
            notebooks.notebook_list.pop(index)
            if index == len(notebooks.notebook_list):
                index -= 1

    else:
        if c in range(32, 126): #normal characters
            __get_selected_notebook().name += chr(c)
            insert_index += 1

        elif c == curses.KEY_BACKSPACE:
            __get_selected_notebook().name = __get_selected_notebook().name[0:len(__get_selected_notebook().name) - 1]
            insert_index -= 1

        elif c in [27, curses.KEY_ENTER, 10]: #Escape and Enter
            __get_selected_notebook().mother.name = __get_selected_notebook().name
            editing = False
            insert_index = -1

        elif c == curses.KEY_LEFT:
            if insert_index > 0:
                insert_index -= 1

        elif c == curses.KEY_RIGHT:
            if insert_index < len(__get_selected_notebook().name):
                insert_index += 1

    return True



def init(scr):
    pass

def __move_index(n):
    global index

    index += n

    if index > len(notebooks.notebook_list) - 1:
        index = 0

    elif index < 0:
        index = len(notebooks.notebook_list) -1

def redraw(scr):
    scr.clear()
    __draw_notebooks(scr)
    __draw_mode(scr)

    if (not insert_index == -1) and scr.getmaxyx()[0] > insert_pos[0] and scr.getmaxyx()[1] > insert_pos[1]:
        scr.move(insert_pos[0], insert_pos[1])
    
    else:
        scr.move(scr.getmaxyx()[0] - 1, scr.getmaxyx()[1] - 1)

def __draw_notebooks(scr):
    global insert_pos

    pos = [2, 2]

    for notebook in notebooks.notebook_list:
        if pos[0] < scr.getmaxyx()[0] and pos[1] < scr.getmaxyx()[1]:
            notebook_str = ("[ %s ]" % notebook.name)[0:scr.getmaxyx()[1] - pos[1]]
            if notebook is notebooks.notebook_list[index]:
                scr.addstr(pos[0], pos[1], notebook_str, curses.color_pair(1))
                
                if editing and (not insert_index == -1):
                    insert_pos = [pos[0], pos[1] + 2 + insert_index]

            else:
                scr.addstr(pos[0], pos[1], notebook_str)

        pos[0] += 1

def __draw_mode(scr):
    if editing:
        mode = "--EDITING--"
    else:
        mode = "--BROWSING--"

    scr.addstr(scr.getmaxyx()[0] - 1, 0, mode[0:scr.getmaxyx()[1] - 1], curses.color_pair(1))

def __get_selected_notebook():
    return notebooks.notebook_list[index]
