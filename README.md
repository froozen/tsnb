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

| Action              | vim | normal |
| :------------------ | --: | -----: |
| Move up             | k   | up     |
| Move down           | j   | down   |
| Open notebook       | l   | right  |
| Edit name           | a   | Enter  |
| New notebook        | o   | n      |
| Delete notebook     | d   | Del    |
| Quit tsnb           |     | q      |

### Notebook editing

| Action                   | vim | normal |
| :----------------------- | --: | -----: |
| Move up                  | k   | up     |
| Move down                | j   | down   |
| Move up in tree          | h   | left   |
| Move down in tree        | l   | right  |
| Toggle node              | t   | None   |
| Edit node                | a   | Enter  |
| New node                 | o   | n      |
| Delete node              | d   | Del    |
| Go to notebook selection |     | q      |
