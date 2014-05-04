import notebooks

class Parsed_args(object):
    def __init__(self):
        self.notebook_id = None
        self.failed = None

def parse(args):
    file_name = None
    notebook_id = None
    failed = False

    i = 0
    while i < len(args):
        if args[i] == "-f":
            if len(args) > i + 1:
                file_name = args[i + 1]
                i += 1
            else:
                print "Error: filename expected after -f"
                failed = True
        
        elif args[i] == "-n":
            if len(args) > i + 1:
                try:
                    notebook_id = int(args[i + 1])
                except ValueError:
                    print "Error: invalid argument after -n: %s" % args[i + 1]
                    failed = True

                i += 1
            else :
                print "Error: id expected after -n"
                failed = True

        i += 1

    parsed_args = Parsed_args()
    if failed:
        parsed_args.failed = True
        return parsed_args

    notebooks.init(file_name)
    
    if not notebook_id == None:
        if notebook_id < len(notebooks.notebook_list) and notebook_id > -1:
            parsed_args.notebook_id = notebook_id
        else:
            print "Error: notebook id out of bounds"
            parsed_args.failed = True
            return parsed_args

    parsed_args.failed = False
    return parsed_args

