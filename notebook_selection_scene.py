import curses
import notebooks
import scene_handler
import notebook_editing_scene

index = 0

def handle_input(scr, c):

    if c == ord("q"):
        return False

    elif c == ord("j"):
        move_index(1)

    elif c == ord("k"):
        move_index(-1)

    elif c == ord("l"):
        notebook_editing_scene.init(scr, index)
        scene_handler.handle_input = notebook_editing_scene.handle_input
        return True

    redraw(scr)

    return True



def init(scr):
    scr.clear()
    redraw(scr)

def move_index(n):
    global index

    index += n

    if index > len(notebooks.notebook_list) - 1:
        index = 0

    elif index < 0:
        index = len(notebooks.notebook_list) -1

def redraw(scr):
    draw_notebooks(scr)

def draw_notebooks(scr):
    pos = [2, 2]

    for notebook in notebooks.notebook_list:
        scr.move(pos[0], 0)
        scr.clrtoeol()

        if notebook is notebooks.notebook_list[index]:
            scr.addstr(pos[0], pos[1], "[ %s ]" % notebook.name, curses.color_pair(1))

        else:
            scr.addstr(pos[0], pos[1], "[ %s ]" % notebook.name)

        pos[0] += 1

