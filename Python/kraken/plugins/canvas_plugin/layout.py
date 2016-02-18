"""Kraken Canvas - Canvas Graph Layout.

Classes:
SpringLayout

"""

class SpringLayout(object):
    """Layout to position nodes in a directed graph"""

    __keys = None
    __nodes = None
    __edges = None

    def __init__(self):
        self.__keys = []
        self.__nodes = {}
        self.__edges = []

    def addNode(self, key):
        if self.__nodes.has_key(key):
            raise Exception("key '%s' already exists." % key)
        self.__keys.append(key)
        self.__nodes[key] = {}

    def addEdge(self, keyA, keyB):
        if not self.__nodes.has_key(keyA):
            raise Exception("key '%s' does not exist." % keyA)
        if not self.__nodes.has_key(keyB):
            raise Exception("key '%s' does not exist." % keyB)
        self.__edges.append([keyA, keyB])

    def compute(self, iterations = 50, scale = 1000):

        connections = {}
        for edge in self.__edges:
            c = connections.get(edge[1], [])
            c.append(edge[0])
            connections[edge[1]] = c

        degree = {}
        maxDegree = 0
        degreeIncreased = True
        while degreeIncreased:
          degreeIncreased = False
          for key in self.__keys:
              degree[key] = degree.get(key, 0)
              if not connections.has_key(key):
                  continue
              for c in connections[key]:
                  if degree.has_key(c):
                      if degree[key] > degree[c]:
                          continue
                      degree[key] = degree[c] + 1
                      degreeIncreased = True
                      if degree[key] > maxDegree:
                          maxDegree = degree[key]

        step = 1
        if maxDegree > 0:
            step = scale / float(maxDegree)

        pos = {}
        for key in self.__keys:
            pos[key] = [float(degree[key]) * step, 0]

        return pos
