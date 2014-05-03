import curses
import notebooks
import scene_handler
import notebook_editing_scene

index = 0
editing = False

def handle_input(scr, c):
    global editing
    global index

    if not editing:
        if c == ord("q"):
            return False

        elif c in [ord("j"), curses.KEY_DOWN]:
            __move_index(1)

        elif c in [ord("k"), curses.KEY_UP]:
            __move_index(-1)

        elif c in [ord("l"), curses.KEY_RIGHT]:
            notebook_editing_scene.init(scr, index)
            scene_handler.handle_input = notebook_editing_scene.handle_input
            return True

        elif c in [ord("a"), curses.KEY_ENTER, 10]:
            editing = True

        elif c == [ord("o"), ord("n")]:
            notebooks.notebook_list.append(notebooks.Notebook("", notebooks.Node()))
            index = len(notebooks.notebook_list) - 1
            editing = True

    else:
        if c in range(32, 126): #normal characters
            __get_selected_notebook().name += chr(c)

        elif c == curses.KEY_BACKSPACE:
            __get_selected_notebook().name = __get_selected_notebook().name[0:len(__get_selected_notebook().name) - 1]

        elif c in [27, curses.KEY_ENTER, 10]: #Escape and Enter
            __get_selected_notebook().mother.name = __get_selected_notebook().name
            editing = False

    __redraw(scr)

    return True



def init(scr):
    scr.clear()
    __redraw(scr)

def __move_index(n):
    global index

    index += n

    if index > len(notebooks.notebook_list) - 1:
        index = 0

    elif index < 0:
        index = len(notebooks.notebook_list) -1

def __redraw(scr):
    __draw_notebooks(scr)
    __draw_mode(scr)

def __draw_notebooks(scr):
    pos = [2, 2]

    for notebook in notebooks.notebook_list:
        scr.move(pos[0], 0)
        scr.clrtoeol()

        if notebook is notebooks.notebook_list[index]:
            scr.addstr(pos[0], pos[1], "[ %s ]" % notebook.name, curses.color_pair(1))

        else:
            scr.addstr(pos[0], pos[1], "[ %s ]" % notebook.name)

        pos[0] += 1

def __draw_mode(scr):
    if editing:
        mode = "--EDITING--"
    else:
        mode = "--BROWSING--"

    scr.addstr(scr.getmaxyx()[0] - 1, 0, mode[0:scr.getmaxyx()[1] - 1], curses.color_pair(1))

def __get_selected_notebook():
    return notebooks.notebook_list[index]
