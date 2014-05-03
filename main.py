#!/usr/bin/python2

import curses
import scene_handler

handle_input = 0

def main(stdscr):
    # Initialize the colors
    curses.use_default_colors()

    curses.init_pair(1, -1, curses.COLOR_BLUE) # Selection
    curses.init_pair(2, curses.COLOR_CYAN, -1) # Tree-Symbols

    import notebooks
    notebooks.init()

    import notebook_selection_scene
    notebook_selection_scene.init(stdscr)
    
    run = True
    while run:
        stdscr.move(stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1)
        c = stdscr.getch()

        run = scene_handler.handle_input(stdscr, c)
        stdscr.refresh()

    notebooks.save_notebooks()

if __name__ == "__main__":
    curses.wrapper(main)
