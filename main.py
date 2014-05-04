#!/usr/bin/python2

import curses
import scene_handler
import sys
import args_parser
import notebooks

handle_input = 0

def tsnb(stdscr, parsed_args):
    # Initialize the colors
    curses.use_default_colors()

    curses.init_pair(1, -1, curses.COLOR_BLUE) # Selection
    curses.init_pair(2, curses.COLOR_CYAN, -1) # Tree-Symbols

    if parsed_args.notebook_id == None:
        import notebook_selection_scene
        notebook_selection_scene.init(stdscr)
        scene_handler.scene = notebook_selection_scene
    else:
        import notebook_editing_scene
        notebook_editing_scene.init(stdscr, parsed_args.notebook_id)
        scene_handler.scene = notebook_editing_scene
    
    run = True
    while run:
        scene_handler.scene.redraw(stdscr)
        stdscr.refresh()

        stdscr.move(stdscr.getmaxyx()[0] - 1, stdscr.getmaxyx()[1] - 1)
        c = stdscr.getch()

        run = scene_handler.scene.handle_input(stdscr, c)

    notebooks.save_notebooks()


if __name__ == "__main__":
    args = sys.argv[1:len(sys.argv)]
    parsed_args = args_parser.parse(args)

    if not parsed_args.failed:
        curses.wrapper(tsnb, parsed_args)
