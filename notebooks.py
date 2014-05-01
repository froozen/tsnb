import os
import json

notebook_list = []

class Node(object):
    def __init__(self, name):
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

        if len(pos) > 1:
            for index in pos[0:len(pos) - 1]:
                if len(node.children) > index:
                    node = node.children[index]

        if len(node.children) > pos[len(pos) - 1]:
            node.children.pop(pos[len(pos) - 1])

def init():
    home = os.path.expanduser("~")
    if os.path.exists(home + "/.tsnb"):
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
    home = os.path.expanduser("~")
    f = open(home + "/.tsnb", "w")

    json_notebook_list = []

    for notebook in notebook_list:
        notebook_dictionary = {"name": notebook.name, "mother": __dictionaryfy_node(notebook.mother)}
        json_notebook_list.append(notebook_dictionary)

    f.write(json.dumps(json_notebook_list))
    f.close()

def __load_notebooks():
    home = os.path.expanduser("~")
    f = open(home + "/.tsnb", "r")

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

