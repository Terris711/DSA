from DSAGraphVertex import GraphVertex


class GraphEdge:

    def __init__(self, froM, to):
        self.froM = froM # from this EDGE to another EDGE ...
        self.to = to

    def getfroM(self):
        return self.froM

    def getTo(self):
        return self.to

    def __str__(self):
        return str(self.froM.label) + str(self.to.label)

