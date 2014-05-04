import os
import json

notebook_list = []
file_path = None

class Node(object):
    def __init__(self, name = None):
        if name == None:
            self.expanded = True
            self.name = ""
            self.children = [Node("")]
        else:
            self.expanded = False
            self.name = name
            self.children = []

    def get_symbol(self):
        if len(self.children) > 0:
            if self.expanded:
                return "-"
            else:
                return "+"

        else:
            return "*"

class Notebook(object):
    def __init__(self, name, mother):
        self.name = name
        self.mother = mother

    def get_node(self, pos):
        node = self.mother

        if len(pos) > 0:
            for index in pos:
                if len(node.children) > index:
                    node = node.children[index]

                else:
                    return -1

        return node
    
    def remove_node(self, pos):
        node = self.mother

        if not (len(pos) == 1 and len(self.mother.children) == 1):
            if len(pos) > 1:
                for index in pos[0:len(pos) - 1]:
                    if len(node.children) > index:
                        node = node.children[index]

            if len(node.children) > pos[len(pos) - 1]:
                node.children.pop(pos[len(pos) - 1])

def init(file_name):
    global file_path
    if file_name == None:
        home = os.path.expanduser("~")
        file_path = home + "/.tsnb"
    else:
        file_path = file_name
        
    if os.path.exists(file_path):
        __load_notebooks()

    else:
        __default()
        save_notebooks()


def __default():
    mother = Node("Mother")
    mother.children.append(Node("Child1"))
    mother.children[0].expanded = True
    mother.children[0].children.append(Node("Subchild1"))
    mother.children[0].children.append(Node("Subchild2"))
    mother.children[0].children.append(Node("Subchild3"))
    mother.children[0].children.append(Node("Subchild4"))

    mother.children.append(Node("Child2"))
    mother.children.append(Node("Child3"))
    mother.children.append(Node("Child4"))

    mother.expanded = True

    notebook_list.append(Notebook("Notebook1", mother))
    notebook_list.append(Notebook("Notebook2", mother))

def save_notebooks():
    f = open(file_path, "w")

    json_notebook_list = []

    for notebook in notebook_list:
        notebook_dictionary = {"name": notebook.name, "mother": __dictionaryfy_node(notebook.mother)}
        json_notebook_list.append(notebook_dictionary)

    f.write(json.dumps(json_notebook_list))
    f.close()

def __load_notebooks():
    f = open(file_path, "r")

    json_notebook_list = json.loads(f.read())

    for notebook_dictionary in json_notebook_list:
        notebook = Notebook(notebook_dictionary["name"], __nodeify_dictionary(notebook_dictionary["mother"]))
        notebook.mother.expanded = True
        notebook_list.append(notebook)

def __dictionaryfy_node(node):
    node_dictionary = {"name": node.name, "children": []}

    for child in node.children:
        node_dictionary["children"].append(__dictionaryfy_node(child))

    return node_dictionary

def __nodeify_dictionary(dictionary):
    node = Node(dictionary["name"])

    for child in dictionary["children"]:
        node.children.append(__nodeify_dictionary(child))

    return node

