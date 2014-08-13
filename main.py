#!/usr/bin/python

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
        # Start off in notebook_selection_scene
        import notebook_selection_scene
        notebook_selection_scene.init(stdscr)
        scene_handler.scene = notebook_selection_scene

    else:
        # Start off in selected notebook_editing_scene
        import notebook_editing_scene
        notebook_editing_scene.init(stdscr, parsed_args.notebook_id)
        scene_handler.scene = notebook_editing_scene
    
    run = True
    while run:
        scene_handler.scene.redraw(stdscr)
        stdscr.refresh()

        c = stdscr.getch()

        run = scene_handler.scene.handle_input(stdscr, c)

    notebooks.save_notebooks()


if __name__ == "__main__":
    args = sys.argv[1:len(sys.argv)]
    parsed_args = args_parser.parse(args)

    curses.wrapper(tsnb, parsed_args)
