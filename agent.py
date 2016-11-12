
class Node:
    def __init__(self):
        self.pos = []
        self.value = None
        self.visible = None
        self.adjNodes = []

    def set_value(self, v):
        self.value = v

    def setVisible(self, isTrue):
        self.visible = isTrue

    def add_adjNode(self, n):
        self.adjNodes.append(n)

class Agent:
    def __init__(self, color, row, column):
        self.pos = [row, column]
        self.color = color
        self.speed = [0,0]
        self.graph = []
