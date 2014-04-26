notebook_list = []

class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []

class Notebook(object):
    def __init__(self, name, nodes):
        self.name = name
        self.nodes = nodes

def init():
    node_list = [Node("1"), Node("2")]
    node_list[0].children.append(Node("Child1"))
    node_list[0].children.append(Node("Child2"))
    node_list[0].children.append(Node("Child3"))
    node_list[0].children.append(Node("Child4"))
    node_list[0].children.append(Node("Child5"))
    node_list[1].children.append(Node("Child1"))
    node_list[1].children.append(Node("Child2"))
    node_list[1].children.append(Node("Child3"))
    node_list[1].children.append(Node("Child4"))
    node_list[1].children.append(Node("Child5"))

    notebook_list.append(Notebook("Notebook1", node_list))
    notebook_list.append(Notebook("Notebook2", node_list))

