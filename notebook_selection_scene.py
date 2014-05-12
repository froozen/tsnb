import curses
import notebooks
import scene_handler
from modes.selection import browsing
from modes.selection import editing

index = 0
insert_index = -1
insert_pos = []
mode = 0

def handle_input(scr, c):
    ret = mode.handle_input(scr, c)

    return ret

def init(scr):
    global mode

    mode = browsing

def redraw(scr):
    # Redraw the scene

    scr.clear()
    __draw_notebooks(scr)
    __draw_mode(scr)

    if (not insert_index == -1) and scr.getmaxyx()[0] > insert_pos[0] and scr.getmaxyx()[1] > insert_pos[1]:
        scr.move(insert_pos[0], insert_pos[1])
    
    else:
        scr.move(scr.getmaxyx()[0] - 1, scr.getmaxyx()[1] - 1)

def __draw_notebooks(scr):
    # Draw the notebook_list

    global insert_pos

    pos = [2, 2]

    for notebook in notebooks.notebook_list:
        # pos is inside screen
        if pos[0] < scr.getmaxyx()[0] and pos[1] < scr.getmaxyx()[1]:
            notebook_str = ("[ %s ]" % notebook.name)[0:scr.getmaxyx()[1] - pos[1]]
            # notebook is selected_notebook
            if notebook is notebooks.notebook_list[index]:
                if not mode == editing:
                    scr.addstr(pos[0], pos[1], notebook_str, curses.color_pair(1))

                else:
                    scr.addstr(pos[0], pos[1], notebook_str)
                
                # cursor should be moved
                if editing and (not insert_index == -1):
                    insert_pos = [pos[0], pos[1] + 2 + insert_index]

            else:
                scr.addstr(pos[0], pos[1], notebook_str)

        pos[0] += 1

def __draw_mode(scr):
    # Draw mode

    scr.addstr(scr.getmaxyx()[0] - 1, 0, ("--%s--" % mode.get_name())[0:scr.getmaxyx()[1] - 1], curses.color_pair(1))

def __get_selected_notebook():
    # Return the Notebook in notebooks.index_list at index

    return notebooks.notebook_list[index]
