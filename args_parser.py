import notebooks
import argparse

class Parsed_args(object):
    def __init__(self):
        self.notebook_id = None

def parse(args):
    # Parse args into a Parsed_args object and return it

    parser = argparse.ArgumentParser ()
    parser.add_argument ( "-f", "--file", help="Specify, which file should be loaded" )
    parser.add_argument ( "-n", "--notebook", help="Specify, which notebook should be loaded", type=int)
    args = parser.parse_args ()

    parsed_args = Parsed_args()

    notebooks.init ( args.file )

    if not args.notebook == None:
        if args.notebook < len(notebooks.notebook_list) and args.notebook > -1:
            parsed_args.notebook_id = args.notebook
        else:
            print("Error: notebook id out of bounds")
            exit ()

    return parsed_args

