# tsnb

tsnb (tree-style notebook) is a programm written in python using the curses-library for its interface. It aims to provide a pleasant notetaking experience by providing a tree-style format and vim-like keybinds.

## Installation

To install and run tsnb, run the following:

    git clone https://github.com/froozen/tsnb.git
    cd tsnb
    python main.py

## Keybinds

For most of the actions there is a vim-like and a "normal" keybind.

### Notebook selection

| Action                        | vim | normal |
| :---------------------------- | --: | -----: |
| Move up                       | k   | Up     |
| Move down                     | j   | Down   |
| Open notebook                 | l   | Right  |
| Edit name                     | a   | Enter  |
| New notebook below the cursor | o   | n      |
| New notebook above the cursor | O   | N      |
| Delete notebook               | d   | Del    |
| Quit tsnb                     |     | q      |

### Notebook editing

| Action                        | vim | normal |
| :---------------------------- | --: | -----: |
| Move up                       | k   | Up     |
| Move down                     | j   | Down   |
| Move up in tree               | h   | Left   |
| Move down in tree             | l   | Right  |
| Move to first node            | g   |        |
| Move to last node             | G   |        |
| Toggle node                   | t   |        |
| Edit node from at back        | A   | Enter  |
| Edit the not at the beginning | I   |        |
| New node below the cursor     | o   | n      |
| New node above the curosr     | O   | N      |
| Delete / Cut node             | d   | Del    |
| Yank / Copy node              | y   |        |
| Paste Node below cursor       | p   |        |
| Paste Node above cursor       | P   |        |
| Sort sibling nodes            | s   |        |
| Save notebooks                | w   | F2     |
| Undo last action              | u   |        |
| Go to notebook selection      |     | q      |
| Quit tsnb                     |     | Q      |

## Commandline options

tsnb provides a bunch of handy commandline options:

| Modifider        | Use                                                                                                  |
| :--------------- | :--------------------------------------------------------------------------------------------------- |
| -f <filename>    | Save and load from <filename> (default: ~/.tsnb)                                                     |
| -n <notebook id> | Start tsnb in notebook editing mode of notebook with id <notebook id> (Note that the ids start at 0) |

