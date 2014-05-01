notebook_list = []

class Node(object):
    def __init__(self, name):
        self.expanded = True
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
    mother = Node("Mother")
    mother.children.append(Node("Child1"))
    mother.children[0].children.append(Node("Subchild1"))
    mother.children[0].children.append(Node("Subchild2"))
    mother.children[0].children.append(Node("Subchild3"))
    mother.children[0].children.append(Node("Subchild4"))

    mother.children.append(Node("Child2"))
    mother.children.append(Node("Child3"))
    mother.children.append(Node("Child4"))

    notebook_list.append(Notebook("Notebook1", mother))
    notebook_list.append(Notebook("Notebook2", mother))

