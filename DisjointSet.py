class DisjointSet:
    size = 0
    ds = {}

    def __init__(self, *items):
        for item in items:
            if isinstance(item, int):
                assert not item < 0, "Items of DisjointSet cannot be negative integers."
            self.ds[item] = -1
        self.size = len(items)

    def __str__(self):
        s = ""
        flag = True
        for key in self.ds:
            val = self.ds[key]
            is_root = isinstance(val, int) and val < 0
            if is_root and flag:
                s += "{" + str(key)
                for k in self.ds:
                    if self.get_root(k) is key and k is not key:
                        s += " " + str(k)
                s += "}"
                flag = False
            elif is_root and not flag:
                s += " {" + str(key)
                for k in self.ds:
                    if self.get_root(k) is key and k is not key:
                        s += " " + str(k)
                s += "}"
        return s

    def __repr__(self):
        return str(self.ds)

    def get_root(self, a):
        to_cache = []
        p = a
        while (not isinstance(self.ds[p], int)) or (not self.ds[p] < 0):
            to_cache += [p]
            p = self.ds[p]
        for x in to_cache:
            self.ds[x] = p
        return p

    def get_weight(self, a):
        p = a
        while (not isinstance(self.ds[p], int)) or (not self.ds[p] < 0):
            p = self.ds[p]
        return -self.ds[p]

    def get_set(self, a):
        a_root = self.get_root(a)
        return [key for key in self.ds if self.get_root(key) == a_root]

    def connect(self, a, b):
        a_root = self.get_root(a)
        b_root = self.get_root(b)
        a_weight = self.get_weight(a_root)
        b_weight = self.get_weight(b_root)
        if a_weight < b_weight:
            self.ds[a_root] = b_root
            self.ds[b_root] = -(a_weight + b_weight)
        else:
            self.ds[b_root] = a_root
            self.ds[a_root] = -(a_weight + b_weight)

    def isConnected(self, a, b):
        return self.get_root(a) is self.get_root(b)
